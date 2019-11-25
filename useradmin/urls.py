from django.urls import path 

from useradmin import views

urlpatterns = [
    path('', views.admin_home, name='admin_home'),
    path('approve/', views.approve, name='approve'),
    path('medicine/add', views.add_medicine, name='add_medicine'),
    path('medicine/view', views.view_medicines, name='view_medicines'),
    path('shop/', views.shop, name='admin_shop_list'),
    path('company/', views.company, name='admin_company_list'),
]
