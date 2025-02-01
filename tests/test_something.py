import requests
from configuration import SERVICE_URL
from src.baseclasses.response import Response
from src.schemas.user import User


def test_getting_users():
    response = requests.get(SERVICE_URL)
    data = Response(response)
    data.assert_status_code(200).validate(User)
