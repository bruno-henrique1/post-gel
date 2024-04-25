from django.urls import path
from postt import views

app_name = 'postt'
urlpatterns = [
    path('home/', views.idx, name='postt'),
    path('post/<slug:slug>', views.post, name='post'),
    path('page/<slug:slug>', views.page, name='page'),
    path('created_by/<int:author_pk>', views.created_by, name='created_by'),
    path('category/<slug:slug>', views.categoryy, name='categoryy'),
    path('tag/<slug:slug>', views.tag, name='tag'),
    path('support/', views.about, name='support'),
    path('search/', views.search, name='search'),


    
    ]