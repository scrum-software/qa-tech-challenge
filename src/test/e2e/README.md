## Running the tests

### If you want to use a persisting docker instance (faster):
You need to have [chromedriver] and [python3] installed.

- See README.md at the root of this repo to run docker
- Modify the BASE_URL in src/test/e2e/config.py)
- Change directory to the one the README file is located at (i.e. `cd src/test/e2e`)
- (ONCE ONLY) ensure you have all the dependencies installed (`pip3 install -r requirements.txt`)
- Run `pytest3` to run the tests

### If you want to run and tear down docker automatically (slower, but more CI-friendly):
You need to have [chromedriver] and [python3] installed.

- Change directory to the one the README file is located at (i.e. `cd src/test/e2e`)
- (ONCE ONLY) ensure you have all the dependencies installed (`pip3 install -r requirements.txt`)
- Run `pytest3 --docker true` to run the tests with docker automatically started