from django.db import models
from django.utils.translation import ugettext_lazy as _
from customer.models import DcCustomer


class BasePolicy(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class DcPolicy(BasePolicy):
    ''' This model holds information about insurance policies by customer '''

    STATE_CHOICES = (
        ('new', 'New'),
        ('quoted', 'Quoted'),
        ('active', 'Active')
    )

    customer_id = models.ForeignKey(DcCustomer, related_name='my_policies', on_delete=models.CASCADE, db_index=True)
    type = models.CharField(_("Policy Type"), max_length=200, db_index=True)
    premium = models.DecimalField(_("Premium"), max_digits=200, decimal_places=3, default=200)
    cover = models.DecimalField(_("Cover"), max_digits=200, decimal_places=3, default=200000)
    state = models.CharField(_("State"), max_length=255, choices=STATE_CHOICES, default='new', blank=True, null=True)
    


    def __str__(self) -> str:
        return f"{self.type}"

    def state_histories(self):
        return self.histories.all()


class DcPolicyHistory(BasePolicy):
    ''' This model store history of policy from its creation day to when its active '''

    STATE_CHOICES = (
        ('new', 'New'),
        ('quoted', 'Quoted'),
        ('active', 'Active')
    )

    policy = models.ForeignKey(DcPolicy, related_name='histories', on_delete=models.CASCADE)
    state = models.CharField(_("State"), max_length=255, choices=STATE_CHOICES, default='new', blank=True, null=True)