from django.urls import path
from customer import api 

app_name = 'customer'

urlpatterns = [
    path('create_customer', api.newCustomerView.as_view(), name='create_customer')
]