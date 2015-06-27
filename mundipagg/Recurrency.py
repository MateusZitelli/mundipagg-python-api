class Recurrency:

    """Class that hold recurrency transaction information"""

    #: Date the first recurrency will be charged [Date]
    dateToStartBilling = None

    #: Indicating the recurrency frequency [String]
    frequencyEnum = None

    #: Recurrency interval [Integer]
    interval = None

    #: Indicates whether the One webservice will run a OneDollarAuth [Boolean]
    oneDollarAuth = None

    #: Number of recurrencies [Integer]
    recurrences = None

    class Frequency:
        Monthly = 'Monthly'
        Yearly = 'Yearly'
        Daily = 'Daily'

    def __init__(self):
        self.frequencyEnum = self.Frequency
