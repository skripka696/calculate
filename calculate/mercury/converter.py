class Converter(object):
    CUBIC_METER_TO_CUBIC_FOOT = 35.3146667

    def cubic_metric_to_cubic_foot_src(self, value):
        return value * self.CUBIC_METER_TO_CUBIC_FOOT

    def kg_acw_src(self, value):
        return value * 2.20462 / 10.4

    def cubic_metric_to_cubic_foot_dest(self, value):
        return value / self.CUBIC_METER_TO_CUBIC_FOOT

    def kg_acw_dest(self, value):
        return value * 10.4 / 2.20462

    def converter_volume(self, value, src_units, dest_units='cft'):
        choices_src = {
            'CBM': self.cubic_metric_to_cubic_foot_src,
            'cbm': self.cubic_metric_to_cubic_foot_src,
            'MT': self.cubic_metric_to_cubic_foot_src,
            'mt': self.cubic_metric_to_cubic_foot_src,
            'kg_acw': self.kg_acw_src,
            'KG_ACW': self.kg_acw_src,
        }

        choices_dest = {
            'CBM': self.cubic_metric_to_cubic_foot_dest,
            'cbm': self.cubic_metric_to_cubic_foot_dest,
            'MT': self.cubic_metric_to_cubic_foot_dest,
            'mt': self.cubic_metric_to_cubic_foot_dest,
            'kg_acw': self.kg_acw_dest,
            'KG_ACW': self.kg_acw_dest,
        }

        if src_units != dest_units:
            value = choices_src.get(src_units)(value)
            value = choices_dest.get(dest_units)(value)
        return value

    def kg_src(self, value):
        return value * 2.20462

    def cwt_src(self, value):
        return value * 100

    def kg_dest(self, value):
        return value / 2.20462

    def cwt_dest(self, value):
        return value / 100

    def convert_weight(self, value, src_units, dest_units='lb'):
        choices_src = {
            'KG': self.kg_src,
            'kg': self.kg_src,
            'CWT': self.cwt_src,
            'cwt': self.cwt_src,
        }

        choices_dest = {
            'KG': self.kg_dest,
            'kg': self.kg_dest,
            'CWT': self.cwt_dest,
            'cwt': self.cwt_dest,
        }

        if src_units != dest_units:
            value = choices_src.get(src_units)(value)
            value = choices_dest.get(dest_units)(value)

        return value

    def get_shipment_type(self, tarrif_type):
        tariff_types = {
            'fcl_c': 'fclCased',
            'FCL_C': 'fclCased',
            'fcl_l': 'fclLoose',
            'FCL_L': 'fclLoose',
            'Air': 'air',
            'AIR': 'air',
            'LCL': 'lcl',
            'lcl': 'lcl',
            'road': 'road',
            'Road': 'road',
        }
        return tariff_types.get(tarrif_type)

    def get_display_shipment_type(self, shipment_type):
        shipment_types = {
            'fcl_c': 'FCL (Cased)',
            'FCL_C': 'FCL (Cased)',
            'fcl_l': 'FCL (Loose)',
            'FCL_L': 'FCL (Loose)',
            'Air': 'Air',
            'AIR': 'Air',
            'LCL': 'LCL',
            'lcl': 'LCL',
            'road': 'Road',
            'Road': 'Road',
        }
        return shipment_types.get(shipment_type)

    def get_shipment_type_value(self, value='default'):
        choices_value = {
            'fclCased': 'FCL_C',
            'FCL (Cased)': 'FCL_C',
            'fclLoose': 'FCL_L',
            'FCL (Loose)': 'FCL_L',
            'air': 'Air',
            'AIR': 'Air',
            'LCL': 'LCL',
            'lcl': 'LCL',
            'road': 'Road',
            'Road': 'Road',
            'default': 'FCL_L'
        }
        return choices_value.get(value)
