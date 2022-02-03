from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

class DcCustomer(models.Model):
    ''' This is model info for customer. its can be extended further '''

    REQUIRED_FIELDS = ['first_name', 'last_name', 'dob']
    email = models.EmailField(_('Email Address'), max_length=254, unique=True, null=True)
    first_name = models.CharField(_("First Name"), max_length=200, db_index=True)
    last_name = models.CharField(_("First Name"), max_length=200)
    dob = models.DateField(_("Date of birth"))
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @property
    def fullname(self) -> str:
        return self.first_name + ' ' +self.last_name
