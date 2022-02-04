from .models import DcPolicy
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=DcPolicy)
def update_policy_state_history(sender, instance, **kwargs):
    instance.histories.get_or_create(state = instance.state)
