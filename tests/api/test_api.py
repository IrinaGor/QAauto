import pytest


@pytest.mark.change
def test_remove_name(user):
    user.name = ''
    assert user.name == ''

@pytest.mark.check
def test_name(user):
    assert user.name == 'Iryna'

@pytest.mark.check
def second_name (user):
    assert second_name == 'Gorenko'
