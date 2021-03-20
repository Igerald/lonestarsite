from django.urls import include, path
from .views import video


urlpatterns = [
    path('', video),
    path('live', video),
    path('paypal/', include('paypal.standard.ipn.urls')),
]
