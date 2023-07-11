from django.urls import path
from . import views

urlpatterns = [
    path('studentapi/', views.studentapi_view, name='studentapi'),
]
