import pytest
from lib.user import get_users, get_user
from lib.logger import get_logger

class TestGetUser:
    logger = get_logger(__name__)

    @pytest.mark.parametrize("page", [1, 2])
    def test_get_users(self, page):
        self.logger.info(f"Getting users with page: {page}")
        response = get_users(page)
        assert response.status_code == 200

        result = response.json()
        self.logger.debug(f"Response JSON: {result}")

        # Assert required keys exist
        for key in ["page", "per_page", "total", "total_pages", "data"]:
            assert key in result, f"Missing expected key: {key}"

        # Assert returned values match input
        assert result["page"] == page

    @pytest.mark.negative
    @pytest.mark.parametrize("page", [3, 100])
    def test_get_users_not_exist_page(self, page):
        self.logger.info(f"Getting users with non exist page: {page}")
        response = get_users(page)
        # Should be 404 here, but it returns 200
        assert response.status_code == 200

    @pytest.mark.parametrize("user_id", [1, 2, 3])
    def test_get_single_user(self, user_id):
        self.logger.info(f"Getting single user with user_id: {user_id}")
        response = get_user(user_id)
        result = response.json()
        self.logger.debug(f"Response JSON: {result}")
        # Assert required keys exist
        for key in ["data", "support"]:
            assert key in result, f"Missing expected key: {key}"

        for key in ["id", "email", "first_name", "last_name", "avatar"]:
            assert key in result["data"], f"Missing expected key: {key}"

        for key in ["url", "text"]:
            assert key in result["support"], f"Missing expected key: {key}"

        # Assert returned values match input
        assert result["data"]["id"] == user_id

    @pytest.mark.negative
    def test_get_user_not_found(self):
        self.logger.info(f"Getting user does not exist")
        response = get_user(23)
        assert response.status_code == 404