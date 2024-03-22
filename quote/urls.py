from django.urls import path
from . import views

urlpatterns = [
    path('par_themes/', views.citations_view, name='citations'),
    path('liker/', views.quotes_view, name='liker')
]