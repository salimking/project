from django.urls import path

from usercompany import views

urlpatterns = [
    path('home/', views.company_home, name='company_home'),
    path('stock/add', views.add_stock, name='add_stock_company'),
    path('stock/view', views.view_stocks, name='view_stock_company'),
    path('stock/avail_view', views.view_avail_stocks, name='view_avail_stock_company'),
    path('stock/<int:pk>/edit', views.edit_stock, name='edit_stock_company'),
    path('stock/<int:pk>/delete', views.delete_stock, name='delete_stock_company'),

    path('order/view', views.view_orders, name='view_order_company'),
    path('order/<int:pk>/accept', views.accept_order, name='accept_order_company'),
    path('order/<int:pk>/decline', views.decline_order, name='decline_order_company'),

    path('transactions/view', views.view_transactions, name='view_transactions_company'),
]
