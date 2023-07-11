from django.urls import path
from . import views

urlpatterns = [
    path('get_data/<int:id>', views.get_data_view, name='getdata'),
    path('get_alldata/', views.all_data_view , name='alldata'),
]


