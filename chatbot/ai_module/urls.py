from .views import answer_from_a_template
from django.urls import path
# ALL THIS FILE WAS ADDED BY ME
app_name = 'ai-module'
urlpatterns = [
    path('', answer_from_a_template, name='hello'),

]