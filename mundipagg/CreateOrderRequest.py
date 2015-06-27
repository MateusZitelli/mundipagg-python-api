class CreateOrderRequest:

    """Class that hold an CreateOrderRequest information"""

    #: Order amount in cents [long]
    amountInCents = None

    #: Amount (in cents) to consider the order paid
    amountInCentsToConsiderPaid = None

    #: Order amount currency [String]
    currencyIsoEnum = None

    #: Buyer instance
    buyer = None

    #: Mundipagg merchant identification
    merchantKey = None
<<<<<<< HEAD

    #: If merchant not send OrderReference, Mundipagg will generate and return in the response.
    #: @return [String] Custom order identification.
    orderReference = None

    #: list with all credit card transaction [List]
    creditCardTransactionCollection = []

    #: List with all boleto transaction [List]
    boletoTransactionCollection = []

    #: If not send, it will be generate automatically in the webservice and returned in response.
    #: Web service request identification, it is used for investigate problems with webservice requests.
    #: @return [Guid] Globally Unique Identifier.
    requestKey = None

    #: Not used
    emailUpdateToBuyerEnum = 'No'

    #: Not used
    FirstCreditCardResult = None

    class DinheiroIsoEnum:

        """Currency Iso Enum"""
        BrazillianReal = 'BRL'
        AmericanDollar = 'USD'

    def __init__(self):
        self.currencyIsoEnum = self.DinheiroIsoEnum.BrazillianReal
        self.target_env = 'dev'
        self.merchantKey = '00000000-0000-0000-0000-000000000000'
=======

    #: If merchant not send OrderReference, Mundipagg will generate and return in the response.
#: @return [String] Custom order identification.
    orderReference = None

    #: list with all credit card transaction [List]
    creditCardTransactionCollection = []

    #: List with all boleto transaction [List]
    boletoTransactionCollection = []

    #: If not send, it will be generate automatically in the webservice and returned in response.
#: Web service request identification, it is used for investigate problems with webservice requests.
#: @return [Guid] Globally Unique Identifier.
    requestKey = None

    #: Not used
    emailUpdateToBuyerEnum = 'No'

    class CurrencyIsoEnum:

        """Currency Iso Enum"""
        BrazillianReal = 'BRL'
        AmericanDollar = 'USD'

    def __init__(self):
        self.requestKey = '00000000-0000-0000-0000-000000000000'
        self.currencyIsoEnum = self.CurrencyIsoEnum.BrazillianReal
>>>>>>> mz/master
