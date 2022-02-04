from django.urls import path
from policy import api 

app_name = 'policy'

urlpatterns = [
    path('quote', api.PolicyQuoteView.as_view(), name='new_quote'),
    path('', api.PolicyListView.as_view(), name='list_policy'),
    path('<id>', api.PolicyDetailView.as_view(), name='policy_detail'),
    path('<id>/history', api.PolicyHistoryDetailView.as_view(), name='policy_history')
]