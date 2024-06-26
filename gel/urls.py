from django.urls import path
from gel import views

app_name = 'gel'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_views, name='login'),
    path('logout/', views.logout_views, name='logout'),
    path('update/', views.update_views, name='update'),
    path('retorna_total_faq/', views.retorna_total_faq, name='retorna_total_faq'),
    path('get_category_counts/', views.get_category_counts, name='get_category_counts'),
    path('get_location_counts/', views.get_location_counts, name='get_location_counts'),
    path('create_faq/', views.create_faq, name='create_faq'),
]
