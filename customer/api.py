from rest_framework import permissions, generics, filters, status, views
from customer import serializers


class newCustomerView(generics.CreateAPIView):
    serializer_class = serializers.DcCustomerSerializer
    permission_classes = (permissions.AllowAny,)