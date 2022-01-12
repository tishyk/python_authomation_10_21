import pytest

from lesson_21.human import Human
from lesson_21.race import Race


@pytest.fixture
def asiat() -> Race:
    yield Race("Asiat")


@pytest.fixture
def negroid() -> Race:
    yield Race("Negroid")


@pytest.fixture
def john_asiat(asiat) -> Human:
    human = Human("John", 23, "male", asiat)
    yield human


@pytest.fixture
def john_negro(negroid) -> Human:
    yield Human("John", 33, negroid)
