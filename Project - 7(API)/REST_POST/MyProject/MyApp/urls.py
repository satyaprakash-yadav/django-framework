from django.urls import path
from . import views

urlpatterns = [
    path('post_data/', views.post_data, name='post_data'),
]

