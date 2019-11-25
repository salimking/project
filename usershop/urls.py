from django.urls import path

from usershop import views

urlpatterns = [
    path('home/', views.shop_home, name='shop_home'),
    path('stock/add', views.add_stock, name='add_stock_shop'),
    path('stock/view', views.view_stocks, name='view_stock_shop'),
    path('stock/avail_view', views.view_avail_stocks, name='view_avail_stock_shop'),
    path('stock/<int:pk>/edit', views.edit_stock, name='edit_stock_shop'),
    path('stock/<int:pk>/delete', views.delete_stock, name='delete_stock_shop'),

    path('order/view', views.view_orders, name='view_order_shop'),
    path('order/<int:pk>/delete', views.delete_order, name='delete_order_shop'),

    path('transactions/view', views.view_transactions, name='view_transactions_shop'),

    path('note/view', views.view_note, name='view_note_shop'),
]
