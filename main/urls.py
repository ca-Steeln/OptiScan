
from django.urls import path
from .views import main_view, info_view,contact_view


urlpatterns = [
    path('', main_view, name='main'),
    path('service/', main_view, name='main'),
    path('info/', info_view, name='info'),
    path('contact/', contact_view, name='contact'),

]
