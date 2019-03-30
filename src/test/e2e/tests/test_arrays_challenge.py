from modules.challenges.challenge_one import ChallengeOne
from modules.base import InitialPage
from modules.test_helpers import TableToDictionary


def test_arrays_challenge(browser):
    array = ['23', '50', '63', '90', '10', '30', '155', '23', '18']
    initial_page = InitialPage(browser)

    assert initial_page.render_challenge_button.text == 'RENDER THE CHALLENGE'

    initial_page.go_to_challenge()
    assert initial_page.submit_button.text == 'SUBMIT ANSWERS'

    challenge_one = ChallengeOne(browser)
    completed_rows_dict = TableToDictionary().convert_table_to_dict(challenge_one.table.table_rows)


    pass
