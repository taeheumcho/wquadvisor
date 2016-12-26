# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=80)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(null=True, blank=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(unique=True, max_length=150)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(null=True, blank=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(serialize=False, max_length=40, primary_key=True)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EtfCategory',
            fields=[
                ('idx', models.AutoField(db_column='IDX', serialize=False, primary_key=True)),
                ('code', models.CharField(unique=True, db_column='CODE', null=True, blank=True, max_length=45)),
                ('name', models.CharField(db_column='NAME', null=True, blank=True, max_length=255)),
                ('crtn_time', models.DateTimeField(db_column='CRTN_TIME', null=True, blank=True)),
                ('update_time', models.DateTimeField(db_column='UPDATE_TIME', null=True, blank=True)),
            ],
            options={
                'db_table': 'ETF_CATEGORY',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EtfData',
            fields=[
                ('idx', models.AutoField(db_column='IDX', serialize=False, primary_key=True)),
                ('dt', models.CharField(db_column='DT', max_length=8)),
                ('ticker', models.CharField(db_column='TICKER', max_length=45)),
                ('price_close', models.FloatField(db_column='PRICE_CLOSE', null=True, blank=True)),
                ('price_open', models.FloatField(db_column='PRICE_OPEN', null=True, blank=True)),
                ('price_high', models.FloatField(db_column='PRICE_HIGH', null=True, blank=True)),
                ('price_low', models.FloatField(db_column='PRICE_LOW', null=True, blank=True)),
                ('volume', models.FloatField(db_column='VOLUME', null=True, blank=True)),
                ('crtn_time', models.DateTimeField(db_column='CRTN_TIME', null=True, blank=True)),
                ('update_time', models.DateTimeField(db_column='UPDATE_TIME', null=True, blank=True)),
            ],
            options={
                'db_table': 'ETF_DATA',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EtfInfo',
            fields=[
                ('idx', models.AutoField(db_column='IDX', serialize=False, primary_key=True)),
                ('ticker', models.CharField(unique=True, db_column='TICKER', null=True, blank=True, max_length=45)),
                ('name', models.CharField(db_column='NAME', null=True, blank=True, max_length=255)),
                ('category_code', models.CharField(db_column='CATEGORY_CODE', null=True, blank=True, max_length=10)),
                ('fund_family', models.CharField(db_column='FUND_FAMILY', null=True, blank=True, max_length=90)),
                ('exchange', models.CharField(db_column='EXCHANGE', null=True, blank=True, max_length=10)),
                ('country', models.CharField(db_column='COUNTRY', null=True, blank=True, max_length=10)),
                ('ccy_cd', models.CharField(db_column='CCY_CD', null=True, blank=True, max_length=10)),
                ('crtn_time', models.DateTimeField(db_column='CRTN_TIME', null=True, blank=True)),
                ('update_time', models.DateTimeField(db_column='UPDATE_TIME', null=True, blank=True)),
            ],
            options={
                'db_table': 'ETF_INFO',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FuturesData',
            fields=[
                ('idx', models.AutoField(db_column='IDX', serialize=False, primary_key=True)),
                ('dt', models.CharField(db_column='DT', null=True, blank=True, max_length=8)),
                ('ticker', models.CharField(db_column='TICKER', null=True, blank=True, max_length=45)),
                ('overnight_cd', models.CharField(db_column='OVERNIGHT_CD', null=True, blank=True, max_length=2)),
                ('close_price', models.FloatField(db_column='CLOSE_PRICE', null=True, blank=True)),
                ('open_price', models.FloatField(db_column='OPEN_PRICE', null=True, blank=True)),
                ('high_price', models.FloatField(db_column='HIGH_PRICE', null=True, blank=True)),
                ('low_price', models.FloatField(db_column='LOW_PRICE', null=True, blank=True)),
                ('volume', models.IntegerField(db_column='VOLUME', null=True, blank=True)),
                ('settlement_price', models.FloatField(db_column='SETTLEMENT_PRICE', null=True, blank=True)),
                ('spot_price', models.FloatField(db_column='SPOT_PRICE', null=True, blank=True)),
                ('outstanding_volume', models.IntegerField(db_column='OUTSTANDING_VOLUME', null=True, blank=True)),
                ('crtn_time', models.DateTimeField(db_column='CRTN_TIME', null=True, blank=True)),
                ('update_time', models.DateTimeField(db_column='UPDATE_TIME', null=True, blank=True)),
            ],
            options={
                'db_table': 'FUTURES_DATA',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FuturesInfo',
            fields=[
                ('idx', models.AutoField(db_column='IDX', serialize=False, primary_key=True)),
                ('ticker', models.CharField(unique=True, db_column='TICKER', null=True, blank=True, max_length=45)),
                ('name', models.CharField(db_column='NAME', null=True, blank=True, max_length=255)),
                ('short_ticker', models.CharField(db_column='SHORT_TICKER', null=True, blank=True, max_length=45)),
                ('expire_dt', models.CharField(db_column='EXPIRE_DT', null=True, blank=True, max_length=6)),
                ('spread_type', models.CharField(db_column='SPREAD_TYPE', null=True, blank=True, max_length=2)),
                ('type_cd', models.CharField(db_column='TYPE_CD', null=True, blank=True, max_length=45)),
                ('crtn_time', models.DateTimeField(db_column='CRTN_TIME', null=True, blank=True)),
                ('update_time', models.DateTimeField(db_column='UPDATE_TIME', null=True, blank=True)),
            ],
            options={
                'db_table': 'FUTURES_INFO',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FuturesInvestor',
            fields=[
                ('idx', models.AutoField(db_column='IDX', serialize=False, primary_key=True)),
                ('dt', models.CharField(db_column='DT', null=True, blank=True, max_length=8)),
                ('ticker', models.CharField(db_column='TICKER', null=True, blank=True, max_length=45)),
                ('overnight_cd', models.CharField(db_column='OVERNIGHT_CD', null=True, blank=True, max_length=2)),
                ('investor_cd', models.CharField(db_column='INVESTOR_CD', null=True, blank=True, max_length=4)),
                ('buy_amount', models.FloatField(db_column='BUY_AMOUNT', null=True, blank=True)),
                ('buy_volume', models.FloatField(db_column='BUY_VOLUME', null=True, blank=True)),
                ('sell_amount', models.FloatField(db_column='SELL_AMOUNT', null=True, blank=True)),
                ('sell_volume', models.FloatField(db_column='SELL_VOLUME', null=True, blank=True)),
                ('crtn_time', models.DateTimeField(db_column='CRTN_TIME', null=True, blank=True)),
                ('update_time', models.DateTimeField(db_column='UPDATE_TIME', null=True, blank=True)),
            ],
            options={
                'db_table': 'FUTURES_INVESTOR',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FxData',
            fields=[
                ('idx', models.AutoField(db_column='IDX', serialize=False, primary_key=True)),
                ('dt', models.CharField(db_column='DT', null=True, blank=True, max_length=8)),
                ('ticker', models.CharField(db_column='TICKER', null=True, blank=True, max_length=45)),
                ('price_close', models.FloatField(db_column='PRICE_CLOSE', null=True, blank=True)),
                ('price_open', models.FloatField(db_column='PRICE_OPEN', null=True, blank=True)),
                ('price_high', models.FloatField(db_column='PRICE_HIGH', null=True, blank=True)),
                ('price_low', models.FloatField(db_column='PRICE_LOW', null=True, blank=True)),
                ('volume', models.FloatField(db_column='VOLUME', null=True, blank=True)),
                ('crtn_time', models.DateTimeField(db_column='CRTN_TIME', null=True, blank=True)),
                ('update_time', models.DateTimeField(db_column='UPDATE_TIME', null=True, blank=True)),
            ],
            options={
                'db_table': 'FX_DATA',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FxInfo',
            fields=[
                ('idx', models.AutoField(db_column='IDX', serialize=False, primary_key=True)),
                ('ticker', models.CharField(unique=True, db_column='TICKER', null=True, blank=True, max_length=45)),
                ('name', models.CharField(db_column='NAME', null=True, blank=True, max_length=255)),
                ('ccy1', models.CharField(db_column='CCY1', null=True, blank=True, max_length=10)),
                ('ccy2', models.CharField(db_column='CCY2', null=True, blank=True, max_length=10)),
                ('crtn_time', models.DateTimeField(db_column='CRTN_TIME', null=True, blank=True)),
                ('update_time', models.DateTimeField(db_column='UPDATE_TIME', null=True, blank=True)),
            ],
            options={
                'db_table': 'FX_INFO',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IndexData',
            fields=[
                ('idx', models.AutoField(db_column='IDX', serialize=False, primary_key=True)),
                ('dt', models.CharField(db_column='DT', null=True, blank=True, max_length=8)),
                ('ticker', models.CharField(db_column='TICKER', null=True, blank=True, max_length=45)),
                ('price_close', models.FloatField(db_column='PRICE_CLOSE', null=True, blank=True)),
                ('price_open', models.FloatField(db_column='PRICE_OPEN', null=True, blank=True)),
                ('price_high', models.FloatField(db_column='PRICE_HIGH', null=True, blank=True)),
                ('price_low', models.FloatField(db_column='PRICE_LOW', null=True, blank=True)),
                ('volume', models.FloatField(db_column='VOLUME', null=True, blank=True)),
                ('crtn_time', models.DateTimeField(db_column='CRTN_TIME', null=True, blank=True)),
                ('update_time', models.DateTimeField(db_column='UPDATE_TIME', null=True, blank=True)),
            ],
            options={
                'db_table': 'INDEX_DATA',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IndexInfo',
            fields=[
                ('idx', models.AutoField(db_column='IDX', serialize=False, primary_key=True)),
                ('ticker', models.CharField(unique=True, db_column='TICKER', null=True, blank=True, max_length=45)),
                ('name', models.CharField(db_column='NAME', null=True, blank=True, max_length=255)),
                ('exchange', models.CharField(db_column='EXCHANGE', null=True, blank=True, max_length=10)),
                ('country', models.CharField(db_column='COUNTRY', null=True, blank=True, max_length=10)),
                ('crtn_time', models.DateTimeField(db_column='CRTN_TIME', null=True, blank=True)),
                ('update_time', models.DateTimeField(db_column='UPDATE_TIME', null=True, blank=True)),
            ],
            options={
                'db_table': 'INDEX_INFO',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IrData',
            fields=[
                ('idx', models.AutoField(db_column='IDX', serialize=False, primary_key=True)),
                ('dt', models.CharField(db_column='DT', null=True, blank=True, max_length=8)),
                ('ticker', models.CharField(db_column='TICKER', null=True, blank=True, max_length=45)),
                ('value1', models.FloatField(db_column='VALUE1', null=True, blank=True)),
                ('value2', models.FloatField(db_column='VALUE2', null=True, blank=True)),
                ('crtn_time', models.DateTimeField(db_column='CRTN_TIME', null=True, blank=True)),
                ('update_time', models.DateTimeField(db_column='UPDATE_TIME', null=True, blank=True)),
            ],
            options={
                'db_table': 'IR_DATA',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IrInfo',
            fields=[
                ('idx', models.AutoField(db_column='IDX', serialize=False, primary_key=True)),
                ('ticker', models.CharField(unique=True, db_column='TICKER', null=True, blank=True, max_length=45)),
                ('irc_cd', models.CharField(db_column='IRC_CD', null=True, blank=True, max_length=45)),
                ('mrty_cd', models.CharField(db_column='MRTY_CD', null=True, blank=True, max_length=10)),
                ('name', models.CharField(db_column='NAME', null=True, blank=True, max_length=255)),
                ('crtn_time', models.DateTimeField(db_column='CRTN_TIME', null=True, blank=True)),
                ('update_time', models.DateTimeField(db_column='UPDATE_TIME', null=True, blank=True)),
            ],
            options={
                'db_table': 'IR_INFO',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StockData',
            fields=[
                ('idx', models.AutoField(db_column='IDX', serialize=False, primary_key=True)),
                ('dt', models.CharField(db_column='DT', max_length=8)),
                ('ticker', models.CharField(db_column='TICKER', max_length=45)),
                ('price_close', models.FloatField(db_column='PRICE_CLOSE', null=True, blank=True)),
                ('price_open', models.FloatField(db_column='PRICE_OPEN', null=True, blank=True)),
                ('price_high', models.FloatField(db_column='PRICE_HIGH', null=True, blank=True)),
                ('price_low', models.FloatField(db_column='PRICE_LOW', null=True, blank=True)),
                ('volume', models.FloatField(db_column='VOLUME', null=True, blank=True)),
                ('amount', models.BigIntegerField(db_column='AMOUNT', null=True, blank=True)),
                ('marketcap', models.BigIntegerField(db_column='MARKETCAP', null=True, blank=True)),
                ('listed_shares', models.IntegerField(db_column='LISTED_SHARES', null=True, blank=True)),
                ('crtn_time', models.DateTimeField(db_column='CRTN_TIME', null=True, blank=True)),
                ('update_time', models.DateTimeField(db_column='UPDATE_TIME', null=True, blank=True)),
            ],
            options={
                'db_table': 'STOCK_DATA',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StockDetail',
            fields=[
                ('idx', models.AutoField(db_column='IDX', serialize=False, primary_key=True)),
                ('dt', models.CharField(db_column='DT', null=True, blank=True, max_length=8)),
                ('ticker', models.CharField(db_column='TICKER', null=True, blank=True, max_length=45)),
                ('ma_200', models.FloatField(db_column='MA_200', null=True, blank=True)),
                ('ma_50', models.FloatField(db_column='MA_50', null=True, blank=True)),
                ('book_value', models.FloatField(db_column='BOOK_VALUE', null=True, blank=True)),
                ('volume_avg', models.FloatField(db_column='VOLUME_AVG', null=True, blank=True)),
                ('ebitda', models.FloatField(db_column='EBITDA', null=True, blank=True)),
                ('dividend_yield', models.FloatField(db_column='DIVIDEND_YIELD', null=True, blank=True)),
                ('market_cap', models.FloatField(db_column='MARKET_CAP', null=True, blank=True)),
                ('year_high', models.FloatField(db_column='YEAR_HIGH', null=True, blank=True)),
                ('year_low', models.FloatField(db_column='YEAR_LOW', null=True, blank=True)),
                ('crtn_time', models.DateTimeField(db_column='CRTN_TIME', null=True, blank=True)),
                ('update_time', models.DateTimeField(db_column='UPDATE_TIME', null=True, blank=True)),
            ],
            options={
                'db_table': 'STOCK_DETAIL',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StockInfo',
            fields=[
                ('idx', models.AutoField(db_column='IDX', serialize=False, primary_key=True)),
                ('ticker', models.CharField(unique=True, db_column='TICKER', null=True, blank=True, max_length=45)),
                ('short_ticker', models.CharField(db_column='SHORT_TICKER', null=True, blank=True, max_length=45)),
                ('name', models.CharField(db_column='NAME', null=True, blank=True, max_length=255)),
                ('exchange', models.CharField(db_column='EXCHANGE', null=True, blank=True, max_length=10)),
                ('country', models.CharField(db_column='COUNTRY', null=True, blank=True, max_length=10)),
                ('ccy_cd', models.CharField(db_column='CCY_CD', null=True, blank=True, max_length=10)),
                ('data_source', models.CharField(db_column='DATA_SOURCE', null=True, blank=True, max_length=5)),
                ('crtn_time', models.DateTimeField(db_column='CRTN_TIME', null=True, blank=True)),
                ('update_time', models.DateTimeField(db_column='UPDATE_TIME', null=True, blank=True)),
            ],
            options={
                'db_table': 'STOCK_INFO',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StockInvestor',
            fields=[
                ('idx', models.AutoField(db_column='IDX', serialize=False, primary_key=True)),
                ('dt', models.CharField(db_column='DT', null=True, blank=True, max_length=8)),
                ('ticker', models.CharField(db_column='TICKER', null=True, blank=True, max_length=45)),
                ('investor_cd', models.CharField(db_column='INVESTOR_CD', null=True, blank=True, max_length=4)),
                ('buy_amount', models.BigIntegerField(db_column='BUY_AMOUNT', null=True, blank=True)),
                ('buy_volume', models.IntegerField(db_column='BUY_VOLUME', null=True, blank=True)),
                ('sell_amount', models.BigIntegerField(db_column='SELL_AMOUNT', null=True, blank=True)),
                ('sell_volume', models.IntegerField(db_column='SELL_VOLUME', null=True, blank=True)),
                ('crtn_time', models.DateTimeField(db_column='CRTN_TIME', null=True, blank=True)),
                ('update_time', models.DateTimeField(db_column='UPDATE_TIME', null=True, blank=True)),
            ],
            options={
                'db_table': 'STOCK_INVESTOR',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StockShort',
            fields=[
                ('idx', models.AutoField(db_column='IDX', serialize=False, primary_key=True)),
                ('dt', models.CharField(db_column='DT', null=True, blank=True, max_length=8)),
                ('ticker', models.CharField(db_column='TICKER', null=True, blank=True, max_length=45)),
                ('volume', models.IntegerField(db_column='VOLUME', null=True, blank=True)),
                ('amount', models.BigIntegerField(db_column='AMOUNT', null=True, blank=True)),
                ('total_volume', models.IntegerField(db_column='TOTAL_VOLUME', null=True, blank=True)),
                ('total_amount', models.BigIntegerField(db_column='TOTAL_AMOUNT', null=True, blank=True)),
                ('total_shares', models.BigIntegerField(db_column='TOTAL_SHARES', null=True, blank=True)),
                ('crtn_time', models.DateTimeField(db_column='CRTN_TIME', null=True, blank=True)),
                ('update_time', models.DateTimeField(db_column='UPDATE_TIME', null=True, blank=True)),
            ],
            options={
                'db_table': 'STOCK_SHORT',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StockSuspension',
            fields=[
                ('idx', models.AutoField(db_column='IDX', serialize=False, primary_key=True)),
                ('dt', models.CharField(db_column='DT', null=True, blank=True, max_length=8)),
                ('ticker', models.CharField(db_column='TICKER', null=True, blank=True, max_length=45)),
                ('start_dt', models.CharField(db_column='START_DT', null=True, blank=True, max_length=8)),
                ('reason', models.CharField(db_column='REASON', null=True, blank=True, max_length=255)),
                ('crtn_time', models.DateTimeField(db_column='CRTN_TIME', null=True, blank=True)),
                ('update_time', models.DateTimeField(db_column='UPDATE_TIME', null=True, blank=True)),
            ],
            options={
                'db_table': 'STOCK_SUSPENSION',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='XpathData',
            fields=[
                ('idx', models.AutoField(db_column='IDX', serialize=False, primary_key=True)),
                ('code', models.CharField(unique=True, db_column='CODE', null=True, blank=True, max_length=45)),
                ('xpath_code', models.CharField(db_column='XPATH_CODE', null=True, blank=True, max_length=45)),
                ('xpath', models.CharField(db_column='XPATH', null=True, blank=True, max_length=255)),
                ('xpath_index', models.IntegerField(db_column='XPATH_INDEX', null=True, blank=True)),
                ('use', models.CharField(db_column='USE', null=True, blank=True, max_length=1)),
                ('insert_column', models.CharField(db_column='INSERT_COLUMN', null=True, blank=True, max_length=45)),
                ('description', models.CharField(db_column='DESCRIPTION', null=True, blank=True, max_length=255)),
                ('crtn_time', models.DateTimeField(db_column='CRTN_TIME', null=True, blank=True)),
                ('update_time', models.DateTimeField(db_column='UPDATE_TIME', null=True, blank=True)),
            ],
            options={
                'db_table': 'XPATH_DATA',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='XpathInfo',
            fields=[
                ('idx', models.AutoField(db_column='IDX', serialize=False, primary_key=True)),
                ('code', models.CharField(unique=True, db_column='CODE', null=True, blank=True, max_length=45)),
                ('sitecode', models.CharField(db_column='SITECODE', null=True, blank=True, max_length=10)),
                ('url', models.CharField(db_column='URL', null=True, blank=True, max_length=255)),
                ('description', models.CharField(db_column='DESCRIPTION', null=True, blank=True, max_length=255)),
            ],
            options={
                'db_table': 'XPATH_INFO',
                'managed': False,
            },
        ),
    ]
