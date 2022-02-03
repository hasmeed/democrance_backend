from policy.models import DcPolicy, DcPolicyHistory
from rest_framework import serializers


class DcPolicyStateHistorySerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d %B, %Y %H:%M:%S")

    class Meta:
        model = DcPolicyHistory
        fields = ('state','created_at')


class DcPolicySerializer(serializers.ModelSerializer):
    state_history = serializers.SerializerMethodField(read_only=True)

    def get_state_history(self, obj):
        policy_history = DcPolicyHistory.objects.filter(policy=obj)
        return DcPolicyStateHistorySerializer(policy_history, many=True).data

    class Meta:
        model = DcPolicy
        fields = ('id', 'customer_id', 'type', 'premium','cover', 'state_history',)