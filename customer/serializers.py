from customer.models import DcCustomer
from rest_framework import serializers
import datetime 

class DcCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = DcCustomer
        fields = '__all__'

    def validate_dob(self, dob):
        try:
            datetime.datetime.strptime(dob, '%d-%m-%Y')
        except:
            raise serializers.ValidationError("invalid dob format supported(d-m-Y)!!")
        return dob
