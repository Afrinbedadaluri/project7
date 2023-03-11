from app1.views import *
from django.urls import path
app_name='something'
urlpatterns = [
    path('one_one/',one_one,name='one_one'),
    path('one_two/',one_two,name='one_two'),
]

