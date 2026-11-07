from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('equipments/', views.equipment_list, name='equipment_list'),
    path('equipments/add/', views.equipment_add, name='equipment_add'),
    path('equipments/edit/<int:pk>/', views.equipment_edit, name='equipment_edit'),
    path('equipments/delete/<int:pk>/', views.equipment_delete, name='equipment_delete'),
]