from django.contrib import admin
from policy.models import DcPolicy, DcPolicyHistory

admin.site.register(DcPolicy)
admin.site.register(DcPolicyHistory)