from rest_framework import serializers, viewsets

from . import models


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = "__all__"


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = models.Customer.objects.all()
    serializer_class = CustomerSerializer
