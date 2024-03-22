from django.urls import path, include 
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('methodo/', views.methodo, name='methodo'),
    path('par_themes/', include('quote.urls')),
    path('liker/', include('quote.urls')),
    ]




