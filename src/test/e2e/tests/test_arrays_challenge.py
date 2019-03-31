from modules.challenges.challenge_one import ChallengeOne
from modules.base import InitialPage
from modules.test_helpers import ListParser, TableToDictionary


def test_arrays_challenge(browser, docker_app):
    initial_page = InitialPage(browser)
    assert initial_page.render_challenge_button.text == 'RENDER THE CHALLENGE'

    initial_page.go_to_challenge()

    challenge_one = ChallengeOne(browser)
    cell_values_object = TableToDictionary().convert_table_to_dict(challenge_one.table.table_rows)

    completed_answers = ListParser().derive_answers(cell_values_object)
    # Temporarily disabled the below to ensure the slack isn't spammed
    # challenge_one.populate_answers_and_submit(completed_answers)

    
    pass
