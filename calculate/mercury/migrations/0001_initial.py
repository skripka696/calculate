# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-11 14:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('office_address_1', models.CharField(max_length=50)),
                ('office_address_2', models.CharField(max_length=50)),
                ('office_city', models.CharField(max_length=50)),
                ('office_postal_code', models.CharField(max_length=50)),
                ('office_country', models.CharField(max_length=50)),
                ('mailing_address_1', models.CharField(max_length=50)),
                ('mailing_address_2', models.CharField(max_length=50)),
                ('mailing_city', models.CharField(max_length=50)),
                ('mailing_postal_code', models.CharField(max_length=50)),
                ('mailing_country', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('fax', models.CharField(max_length=50)),
                ('website', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=50)),
                ('import_contact', models.CharField(max_length=50)),
                ('warehouse_address_1', models.CharField(max_length=50)),
                ('warehouse_address_2', models.CharField(max_length=50)),
                ('warehouse_city', models.CharField(max_length=50)),
                ('warehouse_postal_code', models.CharField(max_length=50)),
                ('warehouse_country', models.CharField(max_length=50)),
                ('import_email', models.CharField(max_length=50)),
                ('import_phone', models.CharField(max_length=50)),
                ('export_contact', models.CharField(max_length=50)),
                ('export_email', models.CharField(max_length=50)),
                ('export_phone', models.CharField(max_length=50)),
                ('manager_contact', models.CharField(max_length=50)),
                ('manager_email', models.CharField(max_length=50)),
                ('manager_phone', models.CharField(max_length=50)),
                ('customs_info', models.TextField()),
                ('consignment_info', models.TextField()),
                ('office_phone', models.CharField(max_length=50)),
                ('office_fax', models.CharField(max_length=50)),
                ('additional_info', models.TextField()),
                ('last_modified', models.DateTimeField(blank=True, null=True)),
                ('freight_contact', models.CharField(blank=True, max_length=50, null=True)),
                ('freight_email', models.CharField(blank=True, max_length=50, null=True)),
                ('freight_phone', models.CharField(blank=True, max_length=50, null=True)),
                ('booking_info', models.TextField(blank=True, null=True)),
                ('freight_office_address_1', models.CharField(blank=True, max_length=50, null=True)),
                ('freight_office_address_2', models.CharField(blank=True, max_length=50, null=True)),
                ('freight_office_city', models.CharField(blank=True, max_length=50, null=True)),
                ('freight_office_postal_code', models.CharField(blank=True, max_length=50, null=True)),
                ('freight_office_country', models.CharField(blank=True, max_length=50, null=True)),
                ('freight_office_fax', models.CharField(blank=True, max_length=50, null=True)),
                ('freight_office_phone', models.CharField(blank=True, max_length=50, null=True)),
                ('freight_office_website', models.CharField(blank=True, max_length=200, null=True)),
                ('freight_manager_contact', models.CharField(blank=True, max_length=50, null=True)),
                ('freight_manager_email', models.CharField(blank=True, max_length=50, null=True)),
                ('freight_manager_phone', models.CharField(blank=True, max_length=50, null=True)),
                ('freight_fcl_service', models.IntegerField(blank=True, null=True)),
                ('freight_lcl_service', models.IntegerField(blank=True, null=True)),
                ('freight_air_service', models.IntegerField(blank=True, null=True)),
                ('freight_road_service', models.IntegerField(blank=True, null=True)),
                ('strict_privacy', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Agentdocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_file', models.CharField(max_length=100)),
                ('notes', models.CharField(blank=True, max_length=400, null=True)),
                ('timestamp', models.DateTimeField()),
                ('is_freight', models.IntegerField()),
                ('archived', models.IntegerField()),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Agentrating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_rating', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Airfreighttariff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField()),
                ('archived', models.IntegerField()),
                ('archive_time', models.DateTimeField(blank=True, null=True)),
                ('expiry', models.DateField(blank=True, null=True)),
                ('comment', models.CharField(blank=True, max_length=5000, null=True)),
                ('dthc', models.IntegerField()),
                ('transit', models.CharField(blank=True, max_length=7, null=True)),
                ('addon', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Airtariffpricepoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_units', models.FloatField()),
                ('unit_price', models.FloatField()),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Corporateaccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('symbol', models.CharField(max_length=200)),
                ('price_in_usd', models.FloatField()),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Currencyhistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_in_usd', models.FloatField()),
                ('archived', models.IntegerField()),
                ('timestamp', models.DateTimeField()),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('multiplier', models.FloatField()),
                ('flc_l_o', models.FloatField(blank=True, null=True)),
                ('flc_c_o', models.FloatField(blank=True, null=True)),
                ('lcl_o', models.FloatField(blank=True, null=True)),
                ('air_o', models.FloatField(blank=True, null=True)),
                ('perm_o', models.FloatField(blank=True, null=True)),
                ('flc_l_d', models.FloatField(blank=True, null=True)),
                ('flc_c_d', models.FloatField(blank=True, null=True)),
                ('lcl_d', models.FloatField(blank=True, null=True)),
                ('air_d', models.FloatField(blank=True, null=True)),
                ('perm_d', models.FloatField(blank=True, null=True)),
                ('freight_increase', models.IntegerField(blank=True, null=True)),
                ('fcl_f', models.FloatField(blank=True, null=True)),
                ('lcl_f', models.FloatField(blank=True, null=True)),
                ('air_f', models.FloatField(blank=True, null=True)),
                ('road_f', models.FloatField(blank=True, null=True)),
                ('multiplier_backup', models.FloatField(blank=True, null=True)),
                ('road_o', models.FloatField(blank=True, null=True)),
                ('road_d', models.FloatField(blank=True, null=True)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Fclfreighttariff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField()),
                ('archived', models.IntegerField()),
                ('archive_time', models.DateTimeField(blank=True, null=True)),
                ('fcl_20_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('fcl_40_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('fcl_40hc_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('expiry', models.DateField(blank=True, null=True)),
                ('comment', models.CharField(blank=True, max_length=5000, null=True)),
                ('dthc', models.IntegerField()),
                ('transit', models.CharField(blank=True, max_length=7, null=True)),
                ('addon', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Freighttariffsettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lcl_col1', models.FloatField()),
                ('lcl_col2', models.FloatField()),
                ('lcl_col3', models.FloatField()),
                ('air_col1', models.FloatField()),
                ('air_col2', models.FloatField()),
                ('air_col3', models.FloatField()),
                ('air_col4', models.FloatField()),
                ('air_col5', models.FloatField()),
                ('air_col6', models.FloatField()),
                ('road_basis', models.CharField(max_length=20)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Globalsetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_timestamp', models.DateTimeField()),
                ('tariff_rules', models.CharField(max_length=100)),
                ('user_tutorial', models.CharField(max_length=100)),
                ('privacy_pledge', models.CharField(max_length=100)),
                ('warehouse_notes', models.CharField(blank=True, max_length=1024, null=True)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Lane',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row', models.IntegerField()),
                ('archived', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Lclfreighttariff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField()),
                ('archived', models.IntegerField()),
                ('archive_time', models.DateTimeField(blank=True, null=True)),
                ('expiry', models.DateField(blank=True, null=True)),
                ('comment', models.CharField(blank=True, max_length=5000, null=True)),
                ('dthc', models.IntegerField()),
                ('transit', models.CharField(blank=True, max_length=7, null=True)),
                ('addon', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Lcltariffpricepoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_units', models.FloatField()),
                ('unit_price', models.FloatField()),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('fcl_port', models.CharField(max_length=200)),
                ('lcl_port', models.CharField(max_length=200)),
                ('air_port', models.CharField(max_length=200)),
                ('notes', models.CharField(blank=True, max_length=1024, null=True)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Move',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('spouse_name', models.CharField(max_length=50)),
                ('create_time', models.DateTimeField()),
                ('estimate_date', models.DateField(blank=True, null=True)),
                ('active', models.IntegerField()),
                ('complete_time', models.DateTimeField(blank=True, null=True)),
                ('origin_address_1', models.CharField(max_length=50)),
                ('origin_address_2', models.CharField(max_length=50)),
                ('origin_city', models.CharField(max_length=50)),
                ('origin_postal_code', models.CharField(max_length=50)),
                ('origin_country', models.CharField(max_length=50)),
                ('destination_address_1', models.CharField(max_length=50)),
                ('destination_address_2', models.CharField(max_length=50)),
                ('destination_city', models.CharField(max_length=50)),
                ('destination_postal_code', models.CharField(max_length=50)),
                ('destination_country', models.CharField(max_length=50)),
                ('survey_estimator_score', models.IntegerField(blank=True, null=True)),
                ('survey_origin_coordinator_score', models.IntegerField(blank=True, null=True)),
                ('survey_packing_crew_score', models.IntegerField(blank=True, null=True)),
                ('survey_customs_consultation_score', models.IntegerField(blank=True, null=True)),
                ('survey_destination_coordinator_score', models.IntegerField(blank=True, null=True)),
                ('survey_delivery_crew_score', models.IntegerField(blank=True, null=True)),
                ('survey_facilitator_score', models.IntegerField(blank=True, null=True)),
                ('survey_comment', models.CharField(max_length=200)),
                ('allowance_notes', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Peraccountdiscount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('multiplier', models.FloatField()),
                ('flc_l_o', models.FloatField(blank=True, null=True)),
                ('flc_c_o', models.FloatField(blank=True, null=True)),
                ('lcl_o', models.FloatField(blank=True, null=True)),
                ('air_o', models.FloatField(blank=True, null=True)),
                ('perm_o', models.FloatField(blank=True, null=True)),
                ('flc_l_d', models.FloatField(blank=True, null=True)),
                ('flc_c_d', models.FloatField(blank=True, null=True)),
                ('lcl_d', models.FloatField(blank=True, null=True)),
                ('air_d', models.FloatField(blank=True, null=True)),
                ('perm_d', models.FloatField(blank=True, null=True)),
                ('freight_increase', models.IntegerField(blank=True, null=True)),
                ('fcl_f', models.FloatField(blank=True, null=True)),
                ('lcl_f', models.FloatField(blank=True, null=True)),
                ('air_f', models.FloatField(blank=True, null=True)),
                ('road_f', models.FloatField(blank=True, null=True)),
                ('multiplier_backup', models.FloatField(blank=True, null=True)),
                ('road_o', models.FloatField(blank=True, null=True)),
                ('road_d', models.FloatField(blank=True, null=True)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Port',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roadfreighttariff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField()),
                ('archived', models.IntegerField()),
                ('archive_time', models.DateTimeField(blank=True, null=True)),
                ('basis', models.CharField(max_length=20)),
                ('expiry', models.DateField(blank=True, null=True)),
                ('comment', models.CharField(blank=True, max_length=1000, null=True)),
                ('transit', models.CharField(blank=True, max_length=7, null=True)),
                ('addon', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roadtariffpricepoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_units', models.FloatField()),
                ('unit_price', models.FloatField()),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode', models.CharField(max_length=20)),
                ('approval_status', models.CharField(max_length=20)),
                ('tariff_export_id', models.IntegerField(blank=True, null=True)),
                ('tariff_import_id', models.IntegerField(blank=True, null=True)),
                ('freight_cost', models.FloatField()),
                ('pre_survey_volume', models.FloatField()),
                ('pre_survey_weight', models.FloatField()),
                ('survey_volume', models.FloatField()),
                ('survey_weight', models.FloatField()),
                ('actual_volume', models.FloatField()),
                ('actual_weight', models.FloatField()),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tariff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
                ('create_time', models.DateTimeField()),
                ('archived', models.IntegerField()),
                ('archive_time', models.DateTimeField(blank=True, null=True)),
                ('basis', models.CharField(max_length=20)),
                ('minimum_density', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('thc', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('thc_40', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('basket_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('agent_name_local', models.CharField(blank=True, max_length=200, null=True)),
                ('market_name_local', models.CharField(blank=True, max_length=200, null=True)),
                ('thc_40_format', models.CharField(blank=True, max_length=20, null=True)),
                ('thc_format', models.CharField(blank=True, max_length=20, null=True)),
                ('hold', models.IntegerField()),
                ('origin_basket_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('destination_basket_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('basis_dest', models.CharField(blank=True, max_length=20, null=True)),
                ('minimum_density_dest', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tariffpricepoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_units', models.FloatField()),
                ('unit_price', models.FloatField()),
                ('export', models.IntegerField()),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tariffroad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_units', models.FloatField(blank=True, null=True)),
                ('unit_price_blanket', models.FloatField(blank=True, null=True)),
                ('unit_price_export', models.FloatField(blank=True, null=True)),
                ('export', models.IntegerField()),
                ('is_warehouse', models.IntegerField()),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tariffroadparams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('warehouse', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('warehouse_format', models.CharField(blank=True, max_length=20, null=True)),
                ('custom_clearance', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('custom_clearance_format', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tariffsupplement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('rate_basis', models.CharField(blank=True, max_length=300, null=True)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tariffsupplementtype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('position', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Userlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(blank=True, max_length=100, null=True)),
                ('calculator_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mercury.Currency')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
