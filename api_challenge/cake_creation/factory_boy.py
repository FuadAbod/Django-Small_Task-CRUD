import factory
from cake_creation.models import Cake

class CakeFactory(factory.django.DjangoModelFactory):
    """Factory boy to help generate test data"""
    class Meta:
        model = Cake
    

