import os
import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def docker_app(docker_services):
    if pytest.config.getoption("docker") == 'true':
        docker_services.start('app')
        public_port = docker_services.wait_for_service("app", 3000)
        url = "http://{docker_services.docker_ip}:{public_port}".format(**locals())
    else:
        url = "http://localhost:3000"
    
    return url


@pytest.fixture(scope='session')
def docker_compose_files(pytestconfig):
    """Get the docker-compose.yml absolute path.
    Override this fixture in your tests if you need a custom location.
    """
    return ['docker-compose.yml']


@pytest.yield_fixture()
def browser(request, docker_services):
    driver = webdriver.Chrome()
    driver.get('{}/'.format(docker_app(docker_services)))
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--docker",
        action="store",
        default="false",
        help="Specify whether to launch docker or not"
    )

@pytest.fixture
def docker(request):
    return request.config.getoption("--docker")