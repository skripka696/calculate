# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desidered behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models


class Accountdetails(models.Model):
    account = models.ForeignKey('Corporateaccount', models.DO_NOTHING)
    email = models.CharField(max_length=75)

    class Meta:
        managed = False


class Agent(models.Model):
    name = models.CharField(max_length=200)
    office_address_1 = models.CharField(max_length=50)
    office_address_2 = models.CharField(max_length=50)
    office_city = models.CharField(max_length=50)
    office_postal_code = models.CharField(max_length=50)
    office_country = models.CharField(max_length=50)
    mailing_address_1 = models.CharField(max_length=50)
    mailing_address_2 = models.CharField(max_length=50)
    mailing_city = models.CharField(max_length=50)
    mailing_postal_code = models.CharField(max_length=50)
    mailing_country = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    fax = models.CharField(max_length=50)
    website = models.CharField(max_length=200)
    currency_id = models.IntegerField()
    email = models.CharField(max_length=50)
    import_contact = models.CharField(max_length=50)
    warehouse_address_1 = models.CharField(max_length=50)
    warehouse_address_2 = models.CharField(max_length=50)
    warehouse_city = models.CharField(max_length=50)
    warehouse_postal_code = models.CharField(max_length=50)
    warehouse_country = models.CharField(max_length=50)
    import_email = models.CharField(max_length=50)
    import_phone = models.CharField(max_length=50)
    export_contact = models.CharField(max_length=50)
    export_email = models.CharField(max_length=50)
    export_phone = models.CharField(max_length=50)
    manager_contact = models.CharField(max_length=50)
    manager_email = models.CharField(max_length=50)
    manager_phone = models.CharField(max_length=50)
    customs_info = models.TextField()
    consignment_info = models.TextField()
    office_phone = models.CharField(max_length=50)
    office_fax = models.CharField(max_length=50)
    additional_info = models.TextField()
    last_modified = models.DateTimeField(blank=True, null=True)
    freight_contact = models.CharField(max_length=50, blank=True, null=True)
    freight_email = models.CharField(max_length=50, blank=True, null=True)
    freight_phone = models.CharField(max_length=50, blank=True, null=True)
    booking_info = models.TextField(blank=True, null=True)
    freight_office_address_1 = models.CharField(max_length=50, blank=True, null=True)
    freight_office_address_2 = models.CharField(max_length=50, blank=True, null=True)
    freight_office_city = models.CharField(max_length=50, blank=True, null=True)
    freight_office_postal_code = models.CharField(max_length=50, blank=True, null=True)
    freight_office_country = models.CharField(max_length=50, blank=True, null=True)
    freight_office_fax = models.CharField(max_length=50, blank=True, null=True)
    freight_office_phone = models.CharField(max_length=50, blank=True, null=True)
    freight_office_website = models.CharField(max_length=200, blank=True, null=True)
    freight_manager_contact = models.CharField(max_length=50, blank=True, null=True)
    freight_manager_email = models.CharField(max_length=50, blank=True, null=True)
    freight_manager_phone = models.CharField(max_length=50, blank=True, null=True)
    freight_fcl_service = models.IntegerField(blank=True, null=True)
    freight_lcl_service = models.IntegerField(blank=True, null=True)
    freight_air_service = models.IntegerField(blank=True, null=True)
    freight_road_service = models.IntegerField(blank=True, null=True)
    service_country_id = models.IntegerField(blank=True, null=True)
    strict_privacy = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False


class AgentAssociations(models.Model):
    agent_id = models.IntegerField()
    agentassociations_id = models.IntegerField()

    class Meta:
        managed = False
        unique_together = (('agent_id', 'agentassociations_id'),)


class AgentCertifications(models.Model):
    agent_id = models.IntegerField()
    agentcertifications_id = models.IntegerField()

    class Meta:
        managed = False
        unique_together = (('agent_id', 'agentcertifications_id'),)


class AgentFreightServiceCountries(models.Model):
    agent = models.ForeignKey(Agent, models.DO_NOTHING)
    country_id = models.IntegerField()

    class Meta:
        managed = False
        unique_together = (('agent', 'country_id'),)


class AgentUsers(models.Model):
    agent_id = models.IntegerField()
    user_id = models.IntegerField()

    class Meta:
        managed = False


class Agentassociations(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        managed = False


class Agentcertifications(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        managed = False


class Agentdocument(models.Model):
    agent = models.ForeignKey(Agent, models.DO_NOTHING)
    upload_file = models.CharField(max_length=100)
    notes = models.CharField(max_length=400, blank=True, null=True)
    timestamp = models.DateTimeField()
    is_freight = models.IntegerField()
    archived = models.IntegerField()

    class Meta:
        managed = False


class Agentlogo(models.Model):
    agent = models.ForeignKey(Agent, models.DO_NOTHING)
    logo = models.CharField(max_length=100)

    class Meta:
        managed = False


class Agentrating(models.Model):
    user_rating = models.IntegerField(blank=True, null=True)
    agent_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False


class Airfreighttariff(models.Model):
    currency_id = models.IntegerField()
    create_time = models.DateTimeField()
    archived = models.IntegerField()
    archive_time = models.DateTimeField(blank=True, null=True)
    lane = models.ForeignKey('Lane', models.DO_NOTHING)
    expiry = models.DateField(blank=True, null=True)
    comment = models.CharField(max_length=5000, blank=True, null=True)
    dthc = models.IntegerField()
    transit = models.CharField(max_length=7, blank=True, null=True)
    addon = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False


class Airtariffpricepoint(models.Model):
    tariff = models.ForeignKey(Airfreighttariff, models.DO_NOTHING)
    min_units = models.FloatField()
    unit_price = models.FloatField()

    class Meta:
        managed = False


class Clientuser(models.Model):
    client_id = models.IntegerField()
    user_id = models.IntegerField()

    class Meta:
        managed = False


class ClientuserCountries(models.Model):
    clientuser = models.ForeignKey(Clientuser, models.DO_NOTHING)
    country_id = models.IntegerField()

    class Meta:
        managed = False
        unique_together = (('clientuser', 'country_id'),)


class ClientuserPreferredAgents(models.Model):
    clientuser = models.ForeignKey(Clientuser, models.DO_NOTHING)
    agent = models.ForeignKey(Agent, models.DO_NOTHING)

    class Meta:
        managed = False
        unique_together = (('clientuser', 'agent'),)


class Continent(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        managed = False


class ContinentCountries(models.Model):
    continent = models.ForeignKey(Continent, models.DO_NOTHING)
    country_id = models.IntegerField()

    class Meta:
        managed = False
        unique_together = (('continent', 'country_id'),)


class Conversation(models.Model):
    ofs_id = models.IntegerField()
    message = models.TextField()
    author_id = models.IntegerField()
    datetime = models.DateTimeField()

    class Meta:
        managed = False


class Corporateaccount(models.Model):
    account_id = models.IntegerField(unique=True)

    class Meta:
        managed = False


class CorporateaccountClient(models.Model):
    corporateaccount_id = models.IntegerField()
    user_id = models.IntegerField()

    class Meta:
        managed = False
        unique_together = (('corporateaccount_id', 'user_id'),)


class Country(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        managed = False

class Currency(models.Model):
    name = models.CharField(max_length=200)
    symbol = models.CharField(max_length=200)
    price_in_usd = models.FloatField()

    class Meta:
        managed = False


class Currencyhistory(models.Model):
    currency_id = models.IntegerField()
    price_in_usd = models.FloatField()
    archived = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        unique_together = (('currency_id', 'timestamp'),)


class Discount(models.Model):
    agent_id = models.IntegerField()
    user_id = models.IntegerField()
    multiplier = models.FloatField()
    flc_l_o = models.FloatField(blank=True, null=True)
    flc_c_o = models.FloatField(blank=True, null=True)
    lcl_o = models.FloatField(blank=True, null=True)
    air_o = models.FloatField(blank=True, null=True)
    perm_o = models.FloatField(blank=True, null=True)
    flc_l_d = models.FloatField(blank=True, null=True)
    flc_c_d = models.FloatField(blank=True, null=True)
    lcl_d = models.FloatField(blank=True, null=True)
    air_d = models.FloatField(blank=True, null=True)
    perm_d = models.FloatField(blank=True, null=True)
    freight_increase = models.IntegerField(blank=True, null=True)
    fcl_f = models.FloatField(blank=True, null=True)
    lcl_f = models.FloatField(blank=True, null=True)
    air_f = models.FloatField(blank=True, null=True)
    road_f = models.FloatField(blank=True, null=True)
    multiplier_backup = models.FloatField(blank=True, null=True)
    road_o = models.FloatField(blank=True, null=True)
    road_d = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False


class Discounts(models.Model):
    agent_id = models.IntegerField()
    user_id = models.IntegerField()
    multiplier = models.FloatField()

    class Meta:
        managed = False


class Document(models.Model):
    move_id = models.IntegerField()
    name = models.CharField(max_length=200)
    file = models.CharField(max_length=100)

    class Meta:
        managed = False


class Fclfreighttariff(models.Model):
    currency_id = models.IntegerField()
    create_time = models.DateTimeField()
    archived = models.IntegerField()
    archive_time = models.DateTimeField(blank=True, null=True)
    lane = models.ForeignKey('Lane', models.DO_NOTHING)
    fcl_20_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fcl_40_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fcl_40hc_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    expiry = models.DateField(blank=True, null=True)
    comment = models.CharField(max_length=5000, blank=True, null=True)
    dthc = models.IntegerField()
    transit = models.CharField(max_length=7, blank=True, null=True)
    addon = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False


class Freighttariff(models.Model):
    type = models.CharField(max_length=20)
    agent = models.ForeignKey(Agent, models.DO_NOTHING)
    origin_port = models.ForeignKey('Port', models.DO_NOTHING)
    destination_port = models.ForeignKey('Port', models.DO_NOTHING)
    currency_id = models.IntegerField()
    rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    create_time = models.DateTimeField()
    archived = models.IntegerField()
    archive_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False


class Freighttariffsettings(models.Model):
    agent = models.ForeignKey(Agent, models.DO_NOTHING)
    lcl_col1 = models.FloatField()
    lcl_col2 = models.FloatField()
    lcl_col3 = models.FloatField()
    air_col1 = models.FloatField()
    air_col2 = models.FloatField()
    air_col3 = models.FloatField()
    air_col4 = models.FloatField()
    air_col5 = models.FloatField()
    air_col6 = models.FloatField()
    currency_id = models.IntegerField()
    road_basis = models.CharField(max_length=20)

    class Meta:
        managed = False


class Globalsetting(models.Model):
    code_timestamp = models.DateTimeField()
    tariff_rules = models.CharField(max_length=100)
    user_tutorial = models.CharField(max_length=100)
    privacy_pledge = models.CharField(max_length=100)
    warehouse_notes = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False


class GlobalsettingEqDisabledAgents(models.Model):
    globalsetting = models.ForeignKey(Globalsetting, models.DO_NOTHING)
    agent = models.ForeignKey(Agent, models.DO_NOTHING)

    class Meta:
        managed = False
        unique_together = (('globalsetting', 'agent'),)


class Lane(models.Model):
    agent = models.ForeignKey(Agent, models.DO_NOTHING)
    origin_port = models.ForeignKey('Port', models.DO_NOTHING)
    destination_port = models.ForeignKey('Port', models.DO_NOTHING)
    row = models.IntegerField()
    archived = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False


class Lclfreighttariff(models.Model):
    currency_id = models.IntegerField()
    create_time = models.DateTimeField()
    archived = models.IntegerField()
    archive_time = models.DateTimeField(blank=True, null=True)
    lane = models.ForeignKey(Lane, models.DO_NOTHING)
    expiry = models.DateField(blank=True, null=True)
    comment = models.CharField(max_length=5000, blank=True, null=True)
    dthc = models.IntegerField()
    transit = models.CharField(max_length=7, blank=True, null=True)
    addon = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False


class Lcltariffpricepoint(models.Model):
    tariff = models.ForeignKey(Lclfreighttariff, models.DO_NOTHING)
    min_units = models.FloatField()
    unit_price = models.FloatField()

    class Meta:
        managed = False


class Location(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        managed = False


class LocationMarkets(models.Model):
    market_id = models.IntegerField()
    location_id = models.IntegerField()

    class Meta:
        managed = False


class Market(models.Model):
    name = models.CharField(max_length=200)
    country_id = models.IntegerField()
    fcl_port = models.CharField(max_length=200)
    lcl_port = models.CharField(max_length=200)
    air_port = models.CharField(max_length=200)
    notes = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False


class Marketstats(models.Model):
    market_id = models.IntegerField(unique=True)
    import_view_count = models.IntegerField()
    export_view_count = models.IntegerField()

    class Meta:
        managed = False


class Milestone(models.Model):
    shipment_id = models.IntegerField()
    template_id = models.IntegerField()
    scheduled = models.DateField(blank=True, null=True)
    actual = models.DateField(blank=True, null=True)

    class Meta:
        managed = False


class Milestonetemplate(models.Model):
    name = models.CharField(max_length=200)
    mode = models.CharField(max_length=20)
    ordering = models.IntegerField()

    class Meta:
        managed = False


class Move(models.Model):
    name = models.CharField(max_length=200)
    spouse_name = models.CharField(max_length=50)
    create_time = models.DateTimeField()
    estimate_date = models.DateField(blank=True, null=True)
    active = models.IntegerField()
    complete_time = models.DateTimeField(blank=True, null=True)
    origin_market_id = models.IntegerField()
    destination_market_id = models.IntegerField()
    export_agent_id = models.IntegerField(blank=True, null=True)
    import_agent_id = models.IntegerField(blank=True, null=True)
    origin_address_1 = models.CharField(max_length=50)
    origin_address_2 = models.CharField(max_length=50)
    origin_city = models.CharField(max_length=50)
    origin_postal_code = models.CharField(max_length=50)
    origin_country = models.CharField(max_length=50)
    destination_address_1 = models.CharField(max_length=50)
    destination_address_2 = models.CharField(max_length=50)
    destination_city = models.CharField(max_length=50)
    destination_postal_code = models.CharField(max_length=50)
    destination_country = models.CharField(max_length=50)
    survey_estimator_score = models.IntegerField(blank=True, null=True)
    survey_origin_coordinator_score = models.IntegerField(blank=True, null=True)
    survey_packing_crew_score = models.IntegerField(blank=True, null=True)
    survey_customs_consultation_score = models.IntegerField(blank=True, null=True)
    survey_destination_coordinator_score = models.IntegerField(blank=True, null=True)
    survey_delivery_crew_score = models.IntegerField(blank=True, null=True)
    survey_facilitator_score = models.IntegerField(blank=True, null=True)
    survey_comment = models.CharField(max_length=200)
    allowance_notes = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False


class Namedmodel(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        managed = False


class Newshipment(models.Model):
    ofs = models.ForeignKey('Orderforservice', models.DO_NOTHING)
    mode = models.CharField(max_length=20)
    declared_volume = models.FloatField()
    declared_weight = models.FloatField()
    tariff_id = models.IntegerField(blank=True, null=True)
    freight_quote = models.FloatField()
    discount = models.FloatField(blank=True, null=True)
    freight_quote_requested = models.IntegerField(blank=True, null=True)
    freight_quote_currency_id = models.IntegerField(blank=True, null=True)
    container_size = models.CharField(max_length=20, blank=True, null=True)
    fcl_tariff = models.ForeignKey(Fclfreighttariff, models.DO_NOTHING, blank=True, null=True)
    lcl_tariff = models.ForeignKey(Lclfreighttariff, models.DO_NOTHING, blank=True, null=True)
    air_tariff = models.ForeignKey(Airfreighttariff, models.DO_NOTHING, blank=True, null=True)
    service_type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False


class Ofsdocument(models.Model):
    ofs_id = models.IntegerField()
    author_id = models.IntegerField()
    upload_file = models.CharField(max_length=100)
    notes = models.CharField(max_length=400, blank=True, null=True)
    timestamp = models.DateTimeField()
    block_agent = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False


class Ofsfollower(models.Model):
    ofs = models.ForeignKey('Orderforservice', models.DO_NOTHING)
    email = models.CharField(max_length=50)
    send_notification = models.IntegerField()
    added_by = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        unique_together = (('ofs', 'email'),)


class Ofsnotificationlist(models.Model):
    user_id = models.IntegerField()
    email = models.CharField(max_length=50)
    default_notify = models.IntegerField()

    class Meta:
        managed = False


class Orderforservice(models.Model):
    is_import = models.IntegerField()
    status = models.CharField(max_length=20, blank=True, null=True)
    source_market_id = models.IntegerField(blank=True, null=True)
    destination_market_id = models.IntegerField(blank=True, null=True)
    transferee_name = models.CharField(max_length=100, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    weight_unit = models.CharField(max_length=20, blank=True, null=True)
    volume_unit = models.CharField(max_length=20, blank=True, null=True)
    archived = models.IntegerField()
    user_id = models.IntegerField(blank=True, null=True)
    agent_id = models.IntegerField(blank=True, null=True)
    corporate_account_id = models.IntegerField(blank=True, null=True)
    cost_selected_agent = models.FloatField(blank=True, null=True)
    cost_market_average = models.FloatField(blank=True, null=True)
    metric = models.FloatField(blank=True, null=True)
    discount = models.FloatField()
    rating = models.IntegerField()
    fxrate_timestamp = models.DateTimeField(blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    exclude_dthc = models.IntegerField(blank=True, null=True)
    external_quote = models.IntegerField(blank=True, null=True)
    is_freight = models.IntegerField(blank=True, null=True)
    subuser_id = models.IntegerField(blank=True, null=True)
    is_dtd = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False


class Penaltycard(models.Model):
    agent_id = models.IntegerField()
    type = models.CharField(max_length=10)
    create_time = models.DateTimeField()
    reason = models.TextField()

    class Meta:
        managed = False


class Peraccountdiscount(models.Model):
    account = models.ForeignKey(Corporateaccount, models.DO_NOTHING)
    discount_id = models.IntegerField()
    multiplier = models.FloatField()
    flc_l_o = models.FloatField(blank=True, null=True)
    flc_c_o = models.FloatField(blank=True, null=True)
    lcl_o = models.FloatField(blank=True, null=True)
    air_o = models.FloatField(blank=True, null=True)
    perm_o = models.FloatField(blank=True, null=True)
    flc_l_d = models.FloatField(blank=True, null=True)
    flc_c_d = models.FloatField(blank=True, null=True)
    lcl_d = models.FloatField(blank=True, null=True)
    air_d = models.FloatField(blank=True, null=True)
    perm_d = models.FloatField(blank=True, null=True)
    freight_increase = models.IntegerField(blank=True, null=True)
    fcl_f = models.FloatField(blank=True, null=True)
    lcl_f = models.FloatField(blank=True, null=True)
    air_f = models.FloatField(blank=True, null=True)
    road_f = models.FloatField(blank=True, null=True)
    multiplier_backup = models.FloatField(blank=True, null=True)
    road_o = models.FloatField(blank=True, null=True)
    road_d = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        unique_together = (('account', 'discount_id'),)


class Port(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        managed = False


class PortLocations(models.Model):
    port_id = models.IntegerField()
    location_id = models.IntegerField()

    class Meta:
        managed = False


class PortMarkets(models.Model):
    port = models.ForeignKey(Port, models.DO_NOTHING)
    market_id = models.IntegerField()

    class Meta:
        managed = False
        unique_together = (('port', 'market_id'),)


class Pricinglog(models.Model):
    user_id = models.IntegerField()
    request = models.CharField(max_length=4096)
    create_time = models.DateTimeField()

    class Meta:
        managed = False


class Pricinglogdata(models.Model):
    user_id = models.IntegerField()
    pricing_log_id = models.IntegerField()
    weight_unit = models.CharField(max_length=10, blank=True, null=True)
    volume_unit = models.CharField(max_length=10, blank=True, null=True)
    currency = models.IntegerField()
    import_market = models.IntegerField(blank=True, null=True)
    export_market = models.IntegerField(blank=True, null=True)
    account = models.CharField(max_length=10, blank=True, null=True)
    include_dthc = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField()

    class Meta:
        managed = False


class Rfpcalculation(models.Model):
    calculation_type = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    row_number = models.IntegerField()
    setup = models.ForeignKey('Rfpsetup', models.DO_NOTHING)

    class Meta:
        managed = False


class Rfpextracalculation(models.Model):
    calculation_type = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    row_number = models.IntegerField()
    rfp_lane = models.ForeignKey('Rfplane', models.DO_NOTHING)

    class Meta:
        managed = False


class Rfpextravalue(models.Model):
    value = models.FloatField()
    size = models.ForeignKey('Rfpsize', models.DO_NOTHING)
    row_number = models.IntegerField()
    rfp_lane = models.ForeignKey('Rfplane', models.DO_NOTHING)

    class Meta:
        managed = False


class Rfpfile(models.Model):
    client_id = models.IntegerField()
    assignee_id = models.IntegerField(blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=60)
    account = models.ForeignKey(Corporateaccount, models.DO_NOTHING, blank=True, null=True)
    currency_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False


class Rfplane(models.Model):
    origin_id = models.IntegerField(blank=True, null=True)
    destination_id = models.IntegerField(blank=True, null=True)
    origin_agent = models.IntegerField(blank=True, null=True)
    destination_agent = models.IntegerField(blank=True, null=True)
    freight_agent = models.IntegerField(blank=True, null=True)
    file = models.ForeignKey(Rfpfile, models.DO_NOTHING)
    setup = models.ForeignKey('Rfpsetup', models.DO_NOTHING)
    row_number = models.FloatField()

    class Meta:
        managed = False


class Rfpsetup(models.Model):
    weight_unit = models.CharField(max_length=4)
    volume_unit = models.CharField(max_length=4)
    rfp_type = models.CharField(max_length=8)
    rfp_file = models.ForeignKey(Rfpfile, models.DO_NOTHING)
    show_total_as = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    column_number = models.IntegerField()

    class Meta:
        managed = False


class Rfpsize(models.Model):
    weight = models.FloatField()
    volume = models.FloatField()
    setup = models.ForeignKey(Rfpsetup, models.DO_NOTHING)

    class Meta:
        managed = False


class Rfpvalue(models.Model):
    value = models.FloatField()
    size = models.ForeignKey(Rfpsize, models.DO_NOTHING)
    row_number = models.IntegerField()

    class Meta:
        managed = False

class Roadfreighttariff(models.Model):
    currency_id = models.IntegerField()
    create_time = models.DateTimeField()
    archived = models.IntegerField()
    archive_time = models.DateTimeField(blank=True, null=True)
    lane = models.ForeignKey(Lane, models.DO_NOTHING)
    basis = models.CharField(max_length=20)
    expiry = models.DateField(blank=True, null=True)
    comment = models.CharField(max_length=1000, blank=True, null=True)
    transit = models.CharField(max_length=7, blank=True, null=True)
    addon = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False


class Roadtariffpricepoint(models.Model):
    tariff = models.ForeignKey(Roadfreighttariff, models.DO_NOTHING)
    min_units = models.FloatField()
    unit_price = models.FloatField()

    class Meta:
        managed = False


class Shipment(models.Model):
    move_id = models.IntegerField()
    mode = models.CharField(max_length=20)
    approval_status = models.CharField(max_length=20)
    tariff_export_id = models.IntegerField(blank=True, null=True)
    tariff_import_id = models.IntegerField(blank=True, null=True)
    freight_cost = models.FloatField()
    pre_survey_volume = models.FloatField()
    pre_survey_weight = models.FloatField()
    survey_volume = models.FloatField()
    survey_weight = models.FloatField()
    actual_volume = models.FloatField()
    actual_weight = models.FloatField()

    class Meta:
        managed = False


class Shipmentallowance(models.Model):
    move_id = models.IntegerField()
    mode = models.CharField(max_length=20)
    unit_a = models.CharField(max_length=20)
    quantity_a = models.FloatField()
    unit_b = models.CharField(max_length=20, blank=True, null=True)
    quantity_b = models.FloatField()

    class Meta:
        managed = False


class Shipmentmilestone(models.Model):
    shipment_id = models.IntegerField()
    template_id = models.IntegerField()
    scheduled = models.DateField(blank=True, null=True)
    actual = models.DateField(blank=True, null=True)

    class Meta:
        managed = False


class Shipmentparams(models.Model):
    pricing_log_data_id = models.IntegerField()
    slot = models.IntegerField()
    type = models.CharField(max_length=10)
    weight = models.CharField(max_length=10, blank=True, null=True)
    volume = models.CharField(max_length=10, blank=True, null=True)
    container = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False


class Statusentry(models.Model):
    move_id = models.IntegerField()
    user_id = models.IntegerField()
    timestamp = models.DateTimeField()
    details = models.CharField(max_length=1024)
    type = models.CharField(max_length=20)

    class Meta:
        managed = False


class Subscriber(models.Model):
    move_id = models.IntegerField()
    user_id = models.IntegerField()
    role = models.CharField(max_length=20)

    class Meta:
        managed = False


class Subscribers(models.Model):
    move_id = models.IntegerField()
    user_id = models.IntegerField()
    role = models.CharField(max_length=20)

    class Meta:
        managed = False


class Survey(models.Model):

    class Meta:
        managed = False


class Tariff(models.Model):
    type = models.CharField(max_length=20)
    agent_id = models.IntegerField()
    market_id = models.IntegerField()
    create_time = models.DateTimeField()
    archived = models.IntegerField()
    archive_time = models.DateTimeField(blank=True, null=True)
    basis = models.CharField(max_length=20)
    minimum_density = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    currency_id = models.IntegerField(blank=True, null=True)
    thc = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    thc_40 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    basket_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    agent_name_local = models.CharField(max_length=200, blank=True, null=True)
    market_name_local = models.CharField(max_length=200, blank=True, null=True)
    thc_40_format = models.CharField(max_length=20, blank=True, null=True)
    thc_format = models.CharField(max_length=20, blank=True, null=True)
    hold = models.IntegerField()
    origin_basket_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    destination_basket_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    basis_dest = models.CharField(max_length=20, blank=True, null=True)
    minimum_density_dest = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False


class Tariffpricepoint(models.Model):
    tariff_id = models.IntegerField()
    min_units = models.FloatField()
    unit_price = models.FloatField()
    export = models.IntegerField()

    class Meta:
        managed = False


class Tariffroad(models.Model):
    tariff_id = models.IntegerField()
    min_units = models.FloatField(blank=True, null=True)
    unit_price_blanket = models.FloatField(blank=True, null=True)
    unit_price_export = models.FloatField(blank=True, null=True)
    export = models.IntegerField()
    is_warehouse = models.IntegerField()

    class Meta:
        managed = False


class Tariffroadparams(models.Model):
    tariff_id = models.IntegerField()
    warehouse = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    warehouse_format = models.CharField(max_length=20, blank=True, null=True)
    custom_clearance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    custom_clearance_format = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False


class Tariffsupplement(models.Model):
    tariff_id = models.IntegerField()
    type_id = models.IntegerField()
    rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    rate_basis = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False


class Tariffsupplementtype(models.Model):
    name = models.CharField(max_length=200)
    position = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False


class Task(models.Model):
    move_id = models.IntegerField()
    template_id = models.IntegerField()
    due_date = models.DateField(blank=True, null=True)
    completed_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False


class Tasktemplate(models.Model):
    actor = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    task_trigger_id = models.IntegerField(blank=True, null=True)
    shipment_mode = models.CharField(max_length=20, blank=True, null=True)
    trigger_condition = models.CharField(max_length=20, blank=True, null=True)
    ordering = models.IntegerField()
    default_delay = models.IntegerField()
    hidden = models.IntegerField()
    milestone = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False


class Userlist(models.Model):
    name = models.CharField(max_length=30)
    setting = models.ForeignKey(Globalsetting)

    class Meta:
        managed = False


class UserlistUsers(models.Model):
    userlist = models.ForeignKey(Userlist)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        unique_together = (('userlist', 'user_id'),)


class UserProfile(models.Model):
    user_id = models.ForeignKey(User)
    company = models.CharField(max_length=100, blank=True, null=True)
    calculator_currency_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
