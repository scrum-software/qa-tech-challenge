from pages import InitialPage
from config import PASSWORD


def test_arrays_challenge(browser):
    initial_page = InitialPage(browser)
    assert initial_page.render_challenge_button.text == 'RENDER THE CHALLENGE'

    initial_page.go_to_challenge()
    assert initial_page.submit_button.text == 'SUBMIT ANSWERS'


    pass
