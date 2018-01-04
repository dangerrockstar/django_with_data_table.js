from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'1/', views.OrderListJson.as_view(), name='order_list_json'),
    url(r'2/', views.OrderList1.as_view(), name='order_list_json2'),
    

]