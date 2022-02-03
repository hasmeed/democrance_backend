from django.urls import path
from policy import api 

app_name = 'policy'

urlpatterns = [
    path('quote', api.PolicyQuoteView.as_view(), name='new_quote')
]