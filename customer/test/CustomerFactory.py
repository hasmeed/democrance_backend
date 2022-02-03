import django
from factory import django, Faker
from customer.models import DcCustomer

class CustomerFactory(django.DjangoModelFactory):
    class Meta:
        model = DcCustomer

    email = Faker('email')
    first_name = Faker('first_name')
    last_name = Faker('last_name')
    dob = Faker('date')

    