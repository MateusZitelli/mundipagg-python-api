class BoletoTransaction:

    """
    Class that hold an BoletoTransaction information
    """

    #: Transaction amount in cents [Long]
    amountInCents = 0

    #: Bank code [Int]
    bankNumber = None

    #: How many days after the creation the boleto will be valid [Int]
    daysToAddInBoletoExpirationDate = None

    #: Number used to identify the boleto
    nossoNumero = None

    #: Text with payment instruction. Limit: 120 characteres [String]
    instructions = None

    #: Custom transaction identifier
    transactionReference = None

    def __init__(self):
        self.daysToAddInBoletoExpirationDate = 7
