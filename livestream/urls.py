from django.urls import include, path
from .views import video


urlpatterns = [
    path(r'', video),
    path(r'live/', video),
    path(r'paypal/', include('paypal.standard.ipn.urls')),
]
