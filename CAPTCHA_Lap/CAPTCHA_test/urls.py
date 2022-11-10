from django.urls import path
from . import views
urlpatterns = [
    path('', views.register, name="registration"), #
    path('login/', views.login, name='login'), #
    path('logout/', views.logout, name="logout"), #
    path('create-new-account', views.register, name='registration'), #
    path('main/', views.main, name='main-site' ), #
]