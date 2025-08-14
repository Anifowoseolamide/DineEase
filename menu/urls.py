from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.MenuListView.as_view(), name='menu_list'),
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    path('item/<slug:slug>/', views.MenuDetailView.as_view(), name='menu_detail'),
]
