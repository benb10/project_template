import pytest


@pytest.mark.django_db(transaction=True)
@pytest.fixture(autouse=True)
def setup_db(transactional_db):
    pass
