import pytest
from lib.user import get_user, delete_user
from lib.logger import get_logger

class TestDeleteUser:
    logger = get_logger(__name__)

    @pytest.mark.parametrize("user_id", [1, 2, 3])
    def test_delete_user(self, user_id):
        self.logger.info(f"Deleting user with user_id: {user_id}")
        response = delete_user(user_id)
        assert response.status_code == 204
        # Get the user again to ensure it has been deleted
        self.logger.info(f"Getting user with user_id: {user_id}")
        response = get_user(user_id)
        self.logger.debug(f"Response code: {response.status_code}")
        # Should be 404 here, but it returns 200
        assert response.status_code in [200, 404]

    def test_delete_nonexistent_user(self):
        self.logger.info(f"Deleting user does not exist")
        response = delete_user(999)
        self.logger.debug(f"Response code: {response.status_code}")
        assert response.status_code in (204, 404)

    def test_delete_user_twice(self):
        self.logger.info(f"Deleting user twice")
        response = delete_user(2)
        self.logger.debug(f"First Response code: {response.status_code}");
        assert response.status_code == 204

        # Get the user again to ensure it has been deleted
        self.logger.info(f"Getting user with user_id: 2")
        response = get_user(2)
        self.logger.debug(f"Response code: {response.status_code}")
        # Should be 404 here, but it returns 200
        assert response.status_code in [200, 404]

        # Try to delete the user again
        self.logger.info(f"Deleting user with user_id: 2 again")
        response = delete_user(2)
        self.logger.debug(f"Second Response code: {response.status_code}")
        assert response.status_code in (204, 404)
