from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<str:pk>', views.delete, name='delete'),
    path('update/<str:pk>', views.update, name='update'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout')
]