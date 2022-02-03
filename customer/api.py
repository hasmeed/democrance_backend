from rest_framework import permissions, generics, filters, status, views
from customer import serializers


class newCustomerView(generics.CreateAPIView):
    ''' This view function handle creating of a 
    new customer using generic class based view 
    '''
    serializer_class = serializers.DcCustomerSerializer
    permission_classes = (permissions.AllowAny,)