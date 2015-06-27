class BuyerAddress:

    """	Class that represents a Buyer Address """

    #: Address type [String]
    addressTypeEnum = None

    #: City [String]
    city = None

    #: Address complement [String]
    complement = None

    #: Address Country
    countryEnum = None

    #: District [String]
    district = None

    #: Address number [String]
    number = None

    #: Address State [String]
    state = None

    #: Street [String]
    street = None

    #: Zip Code [String]
    zipCode = None

    #: Address Enum defined on init
    AddressEnum = None

    #: Country Enum defined on init
    Country = None

    class AddressTypeEnum:

        """Address Type Enum"""
        Billing = 'Billing'
        Shipping = 'Shipping'
        Work = 'Comercial'
        Home = 'Residential'

    class CountryEnum:

        """Country Enum"""
        Brazil = 'Brazil'
        UnitedStates = 'USA'
        Argentina = 'Argentina'
        Bolivia = 'Bolivia'
        Chile = 'Chile'
        Colombia = 'Colombia'
        Uruguay = 'Uruguay'
        Mexico = 'Mexico'
        Paraguay = 'Paraguay'

    def __init__(self):
        self.Country = self.CountryEnum
        self.AddressEnum = self.AddressTypeEnum
        self.countryEnum = self.CountryEnum.Brazil
        self.addressTypeEnum = self.AddressTypeEnum.Home
