#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    Copyright (c) 2017, 2018 Ying Jun <WandyYing@users.noreply.github.com>

import time
from sys import exc_info
from time import sleep
from robot import utils
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.expected_conditions import staleness_of, visibility_of
from selenium.webdriver.support.ui import WebDriverWait
from SeleniumLibrary.keywords import WaitingKeywords
from SeleniumLibrary.base import keyword
from SeleniumLibraryExtension.decorators import DocInherit
from SeleniumLibraryExtension.config import settings


@DocInherit
class WaitingKeywordsExtension(WaitingKeywords):
    """WaitingKeywordsExtension are waiting related execution towards the requested browser."""


    def __init__(self, ctx):
        super(WaitingKeywordsExtension, self).__init__(ctx)

    @keyword
    def wait_for_ready_state_complete(self, timeout=settings.EXTREME_TIMEOUT):
        if self.timeout_multiplier and timeout == settings.EXTREME_TIMEOUT:
            timeout = self._get_new_timeout(timeout)
        is_ready = self._wait_for_ready_state_complete(timeout)
        self.wait_for_angularjs()
        return is_ready

    def _wait_for_ready_state_complete(self, timeout=settings.EXTREME_TIMEOUT):
        """
        The DOM (Document Object Model) has a property called "readyState".
        When the value of this becomes "complete", page resources are considered
        fully loaded (although AJAX and other loads might still be happening).
        This method will wait until document.readyState == "complete".
        """

        start_ms = time.time() * 1000.0
        stop_ms = start_ms + (timeout * 1000.0)
        for x in range(int(timeout * 10)):
            try:
                ready_state = self.driver.execute_script("return document.readyState")
            except WebDriverException:
                # Bug fix for: [Permission denied to access property "document"]
                time.sleep(0.03)
                return True
            if ready_state == u'complete':
                time.sleep(0.01)  # Better be sure everything is done loading
                return True
            else:
                now_ms = time.time() * 1000.0
                if now_ms >= stop_ms:
                    break
                time.sleep(0.1)
        raise Exception(
            "Page elements never fully loaded after %s seconds!" % timeout)

    def wait_for_angularjs(self, timeout=settings.LARGE_TIMEOUT, error=None, **kwargs):
        if not settings.WAIT_FOR_ANGULARJS:
            return

        if not error:
            error = 'AngularJS is not ready in %s' % self._format_timeout(timeout)

        timeout = self._get_timeout_value(timeout, self.ctx.implicit_wait)
        NG_WRAPPER = settings.NG_WRAPPER

        def_pre = 'var cb=arguments[arguments.length-1];if(window.angular){'
        prefix = kwargs.pop('prefix', def_pre)
        handler = kwargs.pop('handler', 'function(){cb(true)}')
        suffix = kwargs.pop('suffix', '}else{cb(false)}')
        script = NG_WRAPPER % {'prefix': prefix,
                               'handler': handler,
                               'suffix': suffix}

        browser = self.driver
        browser.set_script_timeout(timeout)

        poll_frequency = kwargs.pop("poll_frequency", settings.POLL_FREQUENCY)
        browser_breath_delay = kwargs.pop("browser_breath_delay", settings.BROWSER_BREATH_DELAY)
        try:
            WebDriverWait(browser, timeout, poll_frequency). \
                until(lambda driver: driver.execute_async_script(script), error)
        except TimeoutException:
            # prevent double wait
            pass
        except:
            self.debug(exc_info()[0])
            # still inflight, second chance. let the browser take a deep breath...
            sleep(browser_breath_delay)
            try:
                WebDriverWait(browser, timeout, poll_frequency). \
                    until(lambda driver: driver.execute_async_script(script), error)
            except:
                # instead of halting the process because AngularJS is not ready
                # in <TIMEOUT>, we try our luck...
                self.debug(exc_info()[0])
            finally:
                browser.set_script_timeout(self.ctx.timeout)
        finally:
            browser.set_script_timeout(self.ctx.timeout)
            # lets hope things are better when we try to use it

    def _wait_until_script_ready(self, browser, timeout, script, *args):
        response = None
        # pylint: disable=no-member
        selenium_timeout = self.timeout
        try:
            # pylint: disable=no-member
            if timeout != selenium_timeout:
                browser.set_script_timeout(timeout)
            response = browser.execute_async_script(script, *args)
        except TimeoutException:
            # instead of halting the process because document is not ready
            # in <TIMEOUT>, we try our luck...
            # pylint: disable=no-member
            self.debug(exc_info()[0])
        finally:
            if timeout != selenium_timeout:
                # pylint: disable=no-member
                browser.set_script_timeout(selenium_timeout)
        return response

    @staticmethod
    def _get_timeout_value(timeout, default):
        """Returns default timeout when timeout is None."""
        return default if timeout is None else utils.timestr_to_secs(timeout)