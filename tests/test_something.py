from src.baseclasses.response import Response
from src.schemas.user import User
import pytest
from src.schemas.computer import Computer
from computer_json import computer


def test_getting_users(get_users):
    data = Response(get_users)
    data.assert_status_code(200).validate(User)


@pytest.mark.skip('Заблокированно задачей OMNI-17456')
def test_another():
    assert 1 == 1


def test_another_faild():
    assert 1 == 2


@pytest.mark.dev
@pytest.mark.parametrize('first_value, second_value, result', [
    (1, 2, 3),
    ('text1', 'text2', None),
    ('text', 2, None),
    (2, 'text', None)
])
def test_calculate(first_value, second_value, result, calculate):
    assert calculate(first_value, second_value) == result


def test_pydantic_object():
    comp = Computer.parse_obj(computer)
    print(comp.detailed_info.owners)