from django.urls import path
from menu import views

app_name = 'menu'

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>/', views.category, name='category'),
    path('<slug:slug>/<slug:sub_slug>/', views.sub_category, name='sub_category')
]