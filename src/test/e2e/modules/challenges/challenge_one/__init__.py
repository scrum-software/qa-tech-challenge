from selenium.webdriver.support.wait import WebDriverWait

from modules.base import Page
from config import NAME


class ChallengeOne(Page):
    def __init__(self, driver):
        self.driver = driver

    def wait_until_page_is_loaded(self):
        WebDriverWait(self.driver, 5).until(
            lambda _: self.table
        )

    @property
    def table(self):
        table = self.driver.find_element_by_css_selector('tbody')
        return Table(self.driver, table)

    @property
    def submit_button(self):
        return self.driver.find_element_by_xpath('//*[contains(text(), "Submit Answers")]')

    @staticmethod
    def populate_name(submission_field):
        submission_field.send_keys(NAME)

    def populate_answers_and_submit(self, answers_array):
        submission_fields = self.submission_fields
        assert len(submission_fields) == len(answers_array) + 1, 'Check that table size corresponds to submissions size'
        for idx, submission_field in enumerate(submission_fields):
            submission_field.send_keys(answers_array[idx]) if idx < len(answers_array) \
                else self.populate_name(submission_field)        

        self.submit_button.click()

    @property
    def submission_fields(self):
        submission_fields = self.driver.find_elements_by_css_selector('[data-test-id^="submit"]')
        return [SubmissionField(self.driver, submission_field) for submission_field in submission_fields]


class Table(Page):
    def wait_until_page_is_loaded(self):
        pass

    def __init__(self, driver, table):
        self.driver = driver
        self.table = table

    @property
    def table_rows(self):
        table_rows = self.driver.find_elements_by_css_selector('tr')
        return [TableRow(self.driver, table_row) for table_row in table_rows]


class TableRow(Table):
    def __init__(self, driver, table_row):
        self.driver = driver
        self.table_row = table_row

    @property
    def row_cells(self):
        row_cells = self.table_row.find_elements_by_css_selector('td')
        return [RowCell(self.driver, row_cell) for row_cell in row_cells]


class RowCell(TableRow):
    def __init__(self, driver, row_cell):
        self.driver = driver
        self.row_cell = row_cell

    @property
    def cell_value(self):
        return int(self.row_cell.text)


class SubmissionField(ChallengeOne):
    def __init__(self, driver, submission_field):
        self.driver = driver
        self.submission_field = submission_field

    def send_keys(self, value_to_enter):
        self.submission_field.send_keys(value_to_enter)
