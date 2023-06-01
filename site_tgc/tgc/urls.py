from django.urls import path

from tgc.views import SiteHome

urlpatterns = [
    path('', SiteHome.as_view(), name='home'),
]
