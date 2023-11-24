import pytest
from django.urls import reverse
from rest_framework import status
from cake_creation.factory_boy import CakeFactory
from cake_creation.models import Cake

@pytest.mark.django_db
class TestOperationApi:
    def test_get_list_of_cakes(self,client,create_batch_of_cakes):
        """Test endpoint is able to retrieve all created cake"""
        url = reverse("cake-list")
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == 3

    def test_add_another_cake(self,client):
        url = reverse("cake-list")
        data = {
            "name":"tasty_cake",
            "comment":"Tasty",
            "imageUrl":"http://random.com",
            "yumFactor":5,
        }
        response = client.post(url,data
        )
        assert response.status_code == status.HTTP_201_CREATED

    def test_delete_cake(self,client):
        cake = CakeFactory(name="random_cake",yumFactor=5,comment="Delicious",imageUrl="http://random.com")
        url = reverse("cake-detail",kwargs={"pk":cake.pk})
        response = client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not Cake.objects.filter(id=cake.id).exists()