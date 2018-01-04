from __future__ import unicode_literals

from django.db import models

class Internalorder(models.Model):
    order_id = models.AutoField(primary_key=True)
    ordertime = models.TextField(blank=True, null=True)
    last_updated = models.TextField(blank=True, null=True)
    ordertype = models.TextField(blank=True, null=True)
    ticker = models.TextField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    action = models.TextField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    trigger_price = models.FloatField(blank=True, null=True)
    fixed_stoploss_points = models.FloatField(blank=True, null=True)
    trailing_stoploss_points = models.IntegerField(blank=True, null=True)
    take_profit_points = models.FloatField(blank=True, null=True)
    takeprofit_price = models.IntegerField(blank=True, null=True)
    stoploss_price = models.IntegerField(blank=True, null=True)
    broker = models.TextField(blank=True, null=True)
    parent_order_id = models.TextField(blank=True, null=True)
    lotsize = models.IntegerField(blank=True, null=True)
    ticksize = models.FloatField(blank=True, null=True)
    broker_order_tag = models.BigIntegerField(unique=True, blank=True, null=True)
    broker_parent_order_id = models.TextField(blank=True, null=True)
    twap_leg_count = models.IntegerField(blank=True, null=True)
    twap_leg_no = models.IntegerField(blank=True, null=True)
    time_in_force = models.TextField(blank=True, null=True)
    exit_time = models.TextField(blank=True, null=True)
    entry_status = models.TextField(blank=True, null=True)
    exit_status = models.TextField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    strategy_id = models.TextField(blank=True, null=True)
    dealer_id = models.TextField(blank=True, null=True)
    client_id = models.TextField(blank=True, null=True)
    currency = models.TextField(blank=True, null=True)
    quantity_filled = models.IntegerField(blank=True, null=True)
    quantity_exited = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'internalorder'


# class Trades(models.Model):
#     index = models.IntegerField(blank=True, null=True)
#     average_price = models.FloatField(blank=True, null=True)
#     exchange_order_id = models.BigIntegerField(blank=True, null=True)
#     exchange_timestamp = models.TextField(blank=True, null=True)
#     broker_order_id = models.BigIntegerField(blank=True, null=True)
#     order_timestamp = models.TextField(blank=True, null=True)
#     quantity = models.IntegerField(blank=True, null=True)
#     broker_trade_id = models.IntegerField(blank=True, null=True)
#     ticker = models.TextField(blank=True, null=True)
#     action = models.TextField(blank=True, null=True)
#     broker_order_tag = models.ForeignKey(Internalorder, models.DO_NOTHING, db_column='broker_order_tag', blank=True, null=True)
#     broker = models.TextField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'trades'