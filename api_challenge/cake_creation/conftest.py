import pytest 
from cake_creation.factory_boy import CakeFactory


@pytest.fixture
def create_batch_of_cakes():
    """Dummy data for generating cake instances"""

    CakeFactory.create_batch(
        3,
        name="random_cake",
        yumFactor=5,
        comment="Delicious",imageUrl="http://random.com"
    )