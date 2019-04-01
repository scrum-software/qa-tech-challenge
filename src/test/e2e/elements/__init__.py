from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from modules.base import InitialPage


class ChallengeOneTable(InitialPage):
    def wait_until_page_is_loaded(self):
        self.wait_until(self.render_challenge_button.is_displayed())

    @property
    def render_challenge_button(self):
        return self.driver.find_element_by_css_selector('[data-test-id=render-challenge]')

    @property
    def submit_button(self):
        return self.driver.find_element_by_xpath('//*[contains(text(), "Submit Answers")]')

    @property
    def page_height(self):
        return self.driver.execute_script('return document.body.scrollHeight;')

    @property
    def current_scroll_position(self):
        return self.driver.execute_script('return window.pageYOffset;')

    def go_to_challenge(self):
        page_height = self.page_height
        self.render_challenge_button.click()
        try:
            WebDriverWait(self.driver, 5).until(
               lambda _: self.current_scroll_position >= page_height
            )
        except TimeoutException:
            raise Exception("Bottom of the page could not be scrolled to")


