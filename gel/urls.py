from django.urls import path
from gel import views

app_name = 'gel'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('loguin/', views.index, name='login')
]
