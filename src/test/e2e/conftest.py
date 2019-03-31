import os
import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def docker_app(docker_services):
    docker_services.start('app')
    public_port = docker_services.wait_for_service("app", 3000)    
    url = "http://{docker_services.docker_ip}:{public_port}".format(**locals())
    
    return url

@pytest.fixture(scope='session')
def docker_compose_files(pytestconfig):
    """Get the docker-compose.yml absolute path.
    Override this fixture in your tests if you need a custom location.
    """
    return ['docker-compose.yml']

# import ipdb; ipdb.set_trace()
@pytest.yield_fixture()
def browser(request, docker_services):
    driver = webdriver.Chrome()
    driver.get('{}/'.format(docker_app(docker_services)))
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()
