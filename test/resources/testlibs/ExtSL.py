from SeleniumLibraryExtension import SeleniumLibraryExtension
from SeleniumLibrary.base import keyword


class ExtSL(SeleniumLibraryExtension):

    @keyword
    def ext_web_element(self, locator):
        return self.get_webelements(locator)

    @keyword
    def ext_page_should_contain(self, text):
        self.page_should_contain(text)
