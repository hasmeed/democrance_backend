from rest_framework import permissions, generics, filters, status, views
from policy import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from policy.models import DcPolicy, DcPolicyHistory
from django.shortcuts import get_object_or_404, get_list_or_404


class PolicyQuoteView(APIView):
    ''' api view for handling policy related endpoint.
     override patch and post function
    '''
    serializer_class = serializers.DcPolicySerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(context={'request':request}, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)     

    def patch(self, request):
        quote_id = request.data.get('quote_id', None)
        policy_status = request.data.get('status', None)
        if quote_id:
            policy = get_object_or_404(DcPolicy, id=quote_id)
            if policy_status == 'accepted':
                policy.state = DcPolicy.STATE_CHOICES[1][0]
                policy.save()

            # check to be sure the status is active and its previously accepted 
            elif policy_status == 'active' and policy.state == DcPolicy.STATE_CHOICES[1][0]:
                policy.state = DcPolicy.STATE_CHOICES[2][0]
                policy.save()

            return Response(data=serializers.DcPolicySerializer(policy).data, 
                            status=status.HTTP_200_OK)     
        return Response(data={}, status=status.HTTP_400_BAD_REQUEST)     


class PolicyListView(generics.ListAPIView):
    serializer_class = serializers.DcPolicySerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        qs = DcPolicy.objects.all()
        customer_id = self.request.GET.get('customer_id', None)
        if customer_id:
            qs = qs.filter(customer_id=customer_id)
        return qs


class PolicyDetailView(generics.RetrieveAPIView):
    serializer_class = serializers.DcPolicySerializer
    permission_classes = (permissions.AllowAny,)

    def get_object(self):
        id = self.kwargs.get('id')
        if id:
            policy = get_object_or_404(DcPolicy, id=id)
            return policy


class PolicyHistoryDetailView(generics.ListAPIView):
    serializer_class = serializers.DcPolicyStateHistorySerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        id = self.kwargs.get('id')
        policy = get_object_or_404(DcPolicy, id=id)
        return policy.histories.all()