"""Auto-generated file, do not edit by hand. DM metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_DM = PhoneMetadata(id='DM', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[39]\\d\\d', possible_length=(3,)),
    emergency=PhoneNumberDesc(national_number_pattern='333|9(?:11|99)', example_number='999', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='333|9(?:11|99)', example_number='999', possible_length=(3,)),
    short_data=True)
