from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('gallery/', views.gallery_view, name='gallery'),
    path('add/', views.add_view, name='add'),
    path('category/<int:id>', views.category_view, name='category'),
]

