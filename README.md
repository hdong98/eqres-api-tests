# eqres-api-tests
# ReqRes API Test Suite

This project tests the ReqRes user management API using pytest.

reqres-api-tests/
│
├── tests/ # Test cases
├── lib/ # Common utilities (e.g., API requests, config, logging)
├── reports/ # Generated test reports
├── config.ini # Configuration for base URL and API key
├── conftest.py # Pytest hooks and fixtures
├── pytest.ini # Pytest configuration
├── requirements.txt # Project dependencies
├── .github/workflows/ci.yml # GitHub Actions CI
└── README.md

# Set up instructions:

1. Clone the repo: 
git clone https://github.com/hdong98/reqres-api-tests.git

2. Create virtual environment and activate
python3 -m venv venv
source venv/bin/activate

3. Install dependencies:
pip install -r requirements.txt

4. Update config.ini if web_base_url and api_key are different

5. Running all tests on one level up from tests (will generate html report and json report):
pytest -v tests --json-report --json-report-file=reports/report.json


# CI integration with Github Actions:
This project uses GitHub Actions for automated testing. CI is triggered on:
1. Pushes to the main branch
2. Pull requests targeting the main branch

CI Tasks Performed:
1. Sets up a Python environment (version 3.10)
2. Installs all dependencies from requirements.txt
3. Runs tests using pytest
4. Generates an HTML test report (pytest-html)
5. Uploads the report as an artifact for review

CI Workflow File:
Located at: .github/workflows/python-reqres-api-tests.yml

Artifacts:
HTML test report is saved as reports/report.html and attached to each workflow run.
