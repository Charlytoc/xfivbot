from .views import say_hello
from django.urls import path
# ALL THIS FILE WAS ADDED BY ME
app_name = 'ai-module'
urlpatterns = [
    path('', say_hello, name='hello'),

]