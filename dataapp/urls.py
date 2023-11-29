from django.urls import path
from dataapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('create/', views.create, name = 'create'),
    path('retrieve/', views.retrieve, name = 'retrieve'),
    path('update/<str:id>/', views.update, name = 'update'),
    path('delete/<str:id>/', views.delete, name = 'delete'),
    path('login/', auth_views.LoginView.as_view(), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
    path('register/',views.register, name = 'register'),
]

