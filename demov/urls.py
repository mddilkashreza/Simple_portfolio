from django.urls import path
from demov.views import Home,About,Contact,Form,Gallery,Service



app_name = "demov"


urlpatterns = [
    path('home/', Home, name="home"),
    path('about/', About, name="about"),
    path('contact/', Contact, name="contact"),
    path('form/', Form, name="form"),
    path('gallery/', Gallery, name="gallery"),
    path('service/', Service, name="service"),
]