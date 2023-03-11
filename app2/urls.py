from app2.views import *
from django.urls import path
app_name='nothiong'
urlpatterns = [
    path('two_one/',two_one,name='two_one'),
    path('two_two/',two_two,name='two_two'),
   
    
]
