from rest_framework import serializers
from cake_creation.models import Cake

class CakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cake
        fields = "__all__"