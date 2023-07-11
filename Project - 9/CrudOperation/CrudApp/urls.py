from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view, name='home'),
    path('add/',views.add_view, name='add'),
    path('edit/',views.edit_view, name='edit'),
    path('update/<str:id>',views.update_view, name='update'),
    path('delete/<str:id>',views.delete_view, name='delete'),
    path('deleteall/',views.deleteAll_view, name='deleteAll'),
]
