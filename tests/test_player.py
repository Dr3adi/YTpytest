import pytest
from src.generators.player_localize import PlayesrLocalize


@pytest.mark.parametrize('status', [
    'ACTIVE',
    'BANNED',
    'DELETED',
    'INACTIVE'
])
@pytest.mark.parametrize('balance', [
    1, 4, 6, 'sdfs'
])
def test_player(status, balance, get_player_generator):
    print(get_player_generator.set_status(status).set_balance(balance).build())


def test_player_second(get_player_generator):
    object_to_send = get_player_generator.update_inner_value('localize', PlayesrLocalize('fr_FR').set_number(15).build()).build()
    print(object_to_send)


@pytest.mark.parametrize('delete_key', [
    'account_status',
    'avatar',
    'balance',
    'localize'
])
def test_player_without_key(delete_key, get_player_generator):
    object_to_send = get_player_generator.build()
    del object_to_send[delete_key]
    print(object_to_send)