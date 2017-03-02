# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class ApiInfo(models.Model):
    idx = models.IntegerField(db_column='IDX', primary_key=True)  # Field name made lowercase.
    api_name = models.CharField(max_length=45, blank=True, null=True)
    table = models.CharField(db_column='TABLE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    table_description = models.CharField(db_column='TABLE_DESCRIPTION', max_length=225, blank=True, null=True)  # Field name made lowercase.
    column = models.CharField(db_column='COLUMN', max_length=45, blank=True, null=True)  # Field name made lowercase.
    column_description = models.CharField(db_column='COLUMN_DESCRIPTION', max_length=225, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'api_info'


class MarketInfo(models.Model):
    idx = models.IntegerField(db_column='IDX', primary_key=True)  # Field name made lowercase.
    ticker = models.CharField(db_column='TICKER', unique=True, max_length=45, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=255, blank=True, null=True)  # Field name made lowercase.
    exchange = models.CharField(db_column='EXCHANGE', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'market_info'


class StockData(models.Model):
    idx = models.AutoField(db_column='IDX', primary_key=True)  # Field name made lowercase.
    dt = models.CharField(db_column='DT', max_length=8)  # Field name made lowercase.
    ticker = models.CharField(db_column='TICKER', max_length=45)  # Field name made lowercase.
    price_close = models.FloatField(db_column='PRICE_CLOSE', blank=True, null=True)  # Field name made lowercase.
    price_open = models.FloatField(db_column='PRICE_OPEN', blank=True, null=True)  # Field name made lowercase.
    price_high = models.FloatField(db_column='PRICE_HIGH', blank=True, null=True)  # Field name made lowercase.
    price_low = models.FloatField(db_column='PRICE_LOW', blank=True, null=True)  # Field name made lowercase.
    volume = models.FloatField(db_column='VOLUME', blank=True, null=True)  # Field name made lowercase.
    amount = models.BigIntegerField(db_column='AMOUNT', blank=True, null=True)  # Field name made lowercase.
    marketcap = models.BigIntegerField(db_column='MARKETCAP', blank=True, null=True)  # Field name made lowercase.
    listed_shares = models.IntegerField(db_column='LISTED_SHARES', blank=True, null=True)  # Field name made lowercase.
    crtn_time = models.DateTimeField(db_column='CRTN_TIME', blank=True, null=True)  # Field name made lowercase.
    update_time = models.DateTimeField(db_column='UPDATE_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stock_data'


class StockInfo(models.Model):
    idx = models.AutoField(primary_key=True)
    ticker = models.CharField(db_column='TICKER', unique=True, max_length=45, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    exchange = models.CharField(db_column='EXCHANGE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='COUNTRY', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ccy_cd = models.CharField(db_column='CCY_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    data_source = models.CharField(db_column='DATA_SOURCE', max_length=5, blank=True, null=True)  # Field name made lowercase.
    crtn_time = models.DateTimeField(db_column='CRTN_TIME', blank=True, null=True)  # Field name made lowercase.
    update_time = models.DateTimeField(db_column='UPDATE_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stock_info'