from django.urls import path
from gel import views

app_name = 'gel'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_views, name='login'),
    path('logout/', views.logout_views, name='logout')
]
