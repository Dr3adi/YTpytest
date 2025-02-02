from src.baseclasses.response import Response
from src.schemas.user import User


def test_getting_users(get_users):
    data = Response(get_users)
    data.assert_status_code(200).validate(User)
