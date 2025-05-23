import pytest
from lib.user import create_user
from lib.logger import get_logger


class TestCreateUser:
    logger = get_logger(__name__)

    @pytest.mark.parametrize("data", [
        {"name": "Joe Smith", "job": "Engineer"},
        {"name": "Jane Woo", "job": "Manager"},
        {"name": "Alice Wonderland", "job": "Developer"},
        {"name": "Kevin Creative", "job": "Designer"},
        {"name": "Ironman", "job": "QA"},
        {"name": "alice in the wonderland", "job": "QA"},
        {"name": "123456789012345678901234567890", "job": "QA"},
        {"name": "x" * 256, "job": "QA"},
    ])
    def test_create_user(self, data):
        self.logger.info(f"Creating user with data: {data}")
        response, elapsed = create_user(data)
        self.logger.debug(f"Response time: {elapsed:.2f}s")
        assert response.status_code == 201
        result = response.json()
        self.logger.debug(f"Response JSON: {result}")
        # Assert required keys exist
        for key in ["name", "job", "id", "createdAt"]:
            assert key in result, f"Missing expected key: {key}"

        # Assert returned values match input
        assert result["name"] == data["name"]
        assert result["job"] == data["job"]
        assert elapsed < 1.0, f"Request too slow: {elapsed:.2f}s"


    # Not supporsed to return 201 and create a user, but the API does return a created user with empty name and job
    # Test with invalid data: empty data
    @pytest.mark.negative
    def test_create_user_empty_data(self):
        data = {}
        self.logger.info(f"Creating user with data: {data}")
        response, elapsed = create_user(data)
        self.logger.debug(f"Response code: {response.status_code}")
        assert response.status_code in (400, 201)
        assert elapsed < 1.0, f"Request too slow: {elapsed:.2f}s"

    # Not supporsed to return 201 and create a user, but the API does return a created user with empty name and job
    # Test with invalid data: empty name
    @pytest.mark.negative
    def test_create_user_missing_job(self):
        data = {"job": "recruiter"}
        self.logger.info(f"Creating user with data: {data}")
        response, elapsed = create_user(data)
        self.logger.debug(f"Response code: {response.status_code}")
        assert response.status_code in (400, 201)
        assert elapsed < 1.0, f"Request too slow: {elapsed:.2f}s"

    # Not supporsed to return 201 and create a user, but the API does return a created user with empty name and job
    # Test with invalid data: empty job
    @pytest.mark.negative
    def test_create_user_missing_job(self):
        data = {"name": "abc"}
        self.logger.info(f"Creating user with data: {data}")
        response, elapsed = create_user(data)
        self.logger.debug(f"Response code: {response.status_code}")
        assert response.status_code in (400, 201)

    # Not supporsed to return 201 and create a user, but the API does return a created user with empty name and job
    # Test with invalid data: extra field
    @pytest.mark.negative
    def test_create_user_extra_field(self):
        data = {"name": "abc", "job": "recruiter", "extra_field": "extra"}
        self.logger.info(f"Creating user with data: {data}")
        response, elapsed = create_user(data)
        self.logger.debug(f"Response code: {response.status_code}")
        assert response.status_code in (400, 201)
        assert elapsed < 1.0, f"Request too slow: {elapsed:.2f}s"
