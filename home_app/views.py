from django.shortcuts import render
from django.http import HttpResponse
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.views.generic import TemplateView
from .models import Internalorder
# Create your views here.

class OrderListJson(BaseDatatableView):
    model = Internalorder

    columns = ['order_id','ordertime','last_updated','ordertype','ticker','quantity','action',
    'price','trigger_price','fixed_stoploss_points','trailing_stoploss_points','take_profit_points',
    'takeprofit_price','stoploss_price','broker','parent_order_id','lotsize']

    order_columns = ['order_id','ordertime','last_updated','ordertype','ticker','quantity','action',
    'price','trigger_price','fixed_stoploss_points','trailing_stoploss_points','take_profit_points',
    'takeprofit_price','stoploss_price','broker','parent_order_id','lotsize']


    max_display_length = 50

    def render_column(self, row, column):
    	return super(OrderListJson, self).render_column(row, column)

class OrderList1(TemplateView):
    template_name  = "home_app/order_list_json.html"


# class model_fields():
#     new=Internalorder._meta.get_fields(include_parents=True, include_hidden=False)
#     def fields_name(self):
#         return HttpResponse(new)
        
        