from customer.models import DcCustomer
from rest_framework import serializers

class DcCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = DcCustomer
        fields = '__all__'

    # def validate(self, attrs):
    #     return attrs