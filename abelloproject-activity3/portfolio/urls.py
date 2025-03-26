from django.urls import path
from . import views, api_views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('api/items/', api_views.item_list, name='item-list'),
    path('api/items/add/', api_views.add_item, name='add-item'),
    path('api/items/<int:item_id>/', api_views.get_item, name='get-item'),
    path('api/items/update/<int:item_id>/', api_views.update_item, name='update-item'),
    path('api/items/delete/<int:item_id>/', api_views.delete_item, name='delete-item'),
]