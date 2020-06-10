from django.urls import path, include
from . import views
from django.contrib import admin

admin.site.site_header = 'Restaurant Ordering'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('customer_signup', views.customer_signup, name='customer_signup'),
    path('customer_login', views.customer_login, name='customer_login'),
    path('customer_home/<int:pk>', views.customer_home, name='customer_home'),
    path('customer_home_ads/<int:pk>', views.customer_home_ads, name='customer_home_ads'),
    path('manager_signup', views.manager_signup, name='manager_signup'),
    path('manager_home/<int:pk>', views.manager_home, name='manager_home'),
    path('manager_login', views.manager_login, name='manager_login'),

    path('owner_signup', views.owner_signup, name='owner_signup'),
    path('owner_home/<int:pk>', views.owner_home, name='owner_home'),
    path('owner_login', views.owner_login, name='owner_login'),

    path('about/', views.about, name='about'),
    path('delete_restaurant/<int:pk>', views.delete_restaurant, name='delete_restaurant'),
    path('register_restaurant/<int:pk>', views.register_restaurant, name='register_restaurant'),
    path('reg_restaurant_home/<int:pk>', views.reg_restaurant_home, name='reg_restaurant_home'),
    path('view_my_order/<int:pk>', views.view_my_order, name='view_my_order'),
    path('add_item/<int:pk>', views.add_item, name='add_item'),
    path('restaurant_home/<int:pk>', views.restaurant_home, name='restaurant_home'),
    path('place_order/<int:rest_id>/<int:cust_id>', views.place_order, name='place_order'),
    path('placed/<int:pk>', views.placed, name='placed'),
    path('placed_man/<int:pk>', views.placed_man, name='placed_man'),
    path('bill_pdf/<int:pk>', views.bill_pdf, name='bill_pdf'),
    path('restaurant_view_orders/<int:pk>', views.restaurant_view_orders, name='restaurant_view_orders'),
    path('search_by_city/<int:pk>', views.search_by_city, name='search_by_city'),
    path('search_by_name/<int:pk>', views.search_by_name, name='search_by_name'),
    path('delete_item/<int:pk>', views.delete_item, name='delete_item'),
    path('feedback/<int:rest_id>/<int:cust_id>/<int:bill_id>', views.feedback, name='feedback'),
    path('feedback_man/<int:pk>', views.feedback_man, name='feedback_man'),
    path('close_ad/<int:pk>', views.close_ad, name='close_ad'),
    path('upgrade_to_premium/<int:pk>', views.upgrade_to_premium, name='upgrade_to_premium'),
    path('get_offer/<int:pk>', views.get_offer, name='get_offer'),
    path('upgrade_to_gold/<int:pk>', views.upgrade_to_gold, name='upgrade_to_gold'),

]
