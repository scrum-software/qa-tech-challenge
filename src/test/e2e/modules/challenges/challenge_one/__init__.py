from selenium.webdriver.support.wait import WebDriverWait

from modules.base import Page


class ChallengeOne(Page):
    def __init__(self, driver):
        self.driver = driver

    def wait_until_page_is_loaded(self):
        WebDriverWait(self.driver, 5).until(
            lambda _: self.challenge_table
        )

    @property
    def table(self):
        table = self.driver.find_element_by_css_selector('tbody')
        return Table(self.driver, table)

    @property
    def submit_one_button(self):
        return self.driver.find_element_by_css_selector('#submit-1')

    def populate_answers(self):
        answers = [4, 3, 5]
        self.submit_one_button.send_keys('test')

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

