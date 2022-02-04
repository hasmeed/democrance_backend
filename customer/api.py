from rest_framework import permissions, generics, filters, status, views
from customer import serializers
from customer.models import DcCustomer
from django.db.models import Q


class newCustomerView(generics.CreateAPIView):
    ''' This view function handle creating of a 
    new customer using generic class based view 
    '''
    serializer_class = serializers.DcCustomerSerializer
    permission_classes = (permissions.AllowAny,)


class CustomerListingView(generics.ListAPIView):
    ''' Customer Listing view with search and filter functionality 
    Note: We can use django filter and search feature as shown below or 
    have a custom search and filter in get queryset 
    '''
    serializer_class = serializers.DcCustomerSerializer
    # filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    # search_fields = ('first_name', 'last_name','dob')
    # ordering_fields = ('first_name', 'last_name')
    ordering = ('created_at',)  

    def get_queryset(self):
        qs = DcCustomer.objects.all()
        try:
            search = self.request.GET.get('search', None)
            if search:
                qs = qs.filter(Q (first_name__icontains=search) |
                                Q(last_name__icontains=search) |
                                Q(dob__icontains=search) |
                                Q(my_policies__type__icontains=search)
                                )
        except DcCustomer.DoesNotExist:
            return DcCustomer.DoesNotExist
        return qs
