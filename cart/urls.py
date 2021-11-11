from django.urls import path
from . import views
app_name = 'cart'


urlpatterns = [
 path('', views.cartDetail, name='cart_detail'),
 path('add/<int:product_id>/', views.cartAdd, name='cart_add'),
]