import pytest
from lib.user import update_user
from lib.logger import get_logger

class TestUpdateUser:
    logger = get_logger(__name__)

    @pytest.mark.parametrize("data", [
        {"user_id": 1, "name": "John Davis", "job": "Software Engineer"},
        {"user_id": 2, "name": "Jane Woo", "job": "Manager"},
        {"user_id": 3, "name": "x" * 256, "job": "QA"},
    ])
    def test_update_user(self, data):
        self.logger.info(f"Updating user with: {data}")
        payload = {"name": data["name"], "job": data["job"]}
        response = update_user(data["user_id"], payload)
        assert response.status_code == 200

        result = response.json()
        self.logger.debug(f"Response JSON: {result}")

        # Assert required keys exist
        for key in ["name", "job", "updatedAt"]:
            assert key in result, f"Missing expected key: {key}"

        # Assert returned values match input
        assert result["name"] == data["name"]
        assert result["job"] == data["job"]

    def test_update_nonexistent_user(self):
        self.logger.info(f"Updating user does not exist")
        data = {"name": "Ghost"}
        response = update_user(999, data)
        assert response.status_code in (200, 404)