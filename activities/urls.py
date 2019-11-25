from django.urls import path

from activities import views

urlpatterns = [
    path('orders/create', views.create_order, name='create_order'),
    path('orders/get_company_list', views.get_company_list, name='get_company_list_order'),
]
