from django.urls import path
from webside.views import index, about, services, contact, one_page

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('contact/', contact, name='contact'),
    path('one-page/', one_page, name='one-page'),
    
]