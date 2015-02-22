# -*- coding: UTF-8 -*-
__author__ = 'Arcarius Engenharia'

from cStringIO import StringIO
from mundipagg.CreateOrderRequest import CreateOrderRequest
from mundipagg.CreditCardTransaction import CreditCardTransaction
from suds.client import Client
import uuid
import logging


class CreditCardTransactionReponse():
    """Essa classe está aqui apenas para documentar os objetos que compõem a coleção 
       CreditCardTransactionResultCollection na resposta arcCreateOrderResponse do mundipagg
    """
    AcquirerMessage = ""
    AcquirerReturnCode = "0"
    AmountInCents = 0
    AuthorizationCode = ""
    AuthorizedAmountInCents = 0
    CapturedAmountInCents = 0
    CreditCardNumber = ""
    CreditCardOperationEnum = ""
    CreditCardTransactionStatusEnum = ""
    CustomStatus = 0
    DueDate = None
    ExternalTimeInMilliseconds = 0
    InstantBuyKey = "00000000-0000-0000-0000-000000000000"
    RefundedAmountInCents = 0
    Success = False
    TransactionIdentifier = ""
    TransactionKey = "00000000-0000-0000-0000-000000000000"
    TransactionReference = ""
    UniqueSequentialNumber = ""
    VoidedAmountInCents = None
    OriginalAcquirerReturnCollection = None


class CreateOrderResponse():
    """Essa classe está aqui apenas para documentar o objeto de resposta do método CreateCreditCardTransactionCollection"""
    BuyerKey = "00000000-0000-0000-0000-000000000000"
    MerchantKey = "00000000-0000-0000-0000-000000000000"
    MundiPaggTimeInMilliseconds = 0
    OrderKey = "00000000-0000-0000-0000-000000000000"
    OrderReference = "0"
    OrderStatusEnum = "Paid"
    RequestKey = "00000000-0000-0000-0000-000000000000"
    Success = True
    Version = "1.0"
    CreditCardTransactionResultCollection = []
    BoletoTransactionResultCollection = []
    MundiPaggSuggestion = None
    ErrorReport = None
    FirstCreditCardResult = None

class Gateway:
    """Class responsable for comunicating with the service via SOAP"""

    last_sent = ""
    last_received = ""

    def __init__(self, environment="test"):
        """This method creates an CreateBuyer object
        :param environment: test/production
        @type environment: string
        """
        self.environment = environment
        logging.basicConfig(level=logging.ERROR)
        # logging.getLogger('suds.client').setLevel(logging.DEBUG)
        # logging.getLogger('suds.transport').setLevel(logging.DEBUG)

    def getUrl(self):
        return "https://transaction.mundipaggone.com/MundiPaggService.svc?wsdl"

    def CreateBuyer(self, request):
        """This method creates an CreateBuyer object
        :param request: A CreateOrderRequest
        @type environment: string
        :returns: Buyer object
        """
        url = self.getUrl()
        client = Client(url)
        buyer = client.factory.create('ns0:Buyer')
        buyerAddress = client.factory.create('ns0:BuyerAddress')
        addressCollection = []
        for address in request.buyer.addressCollection:
            buyerAddress.AddressTypeEnum = address.addressTypeEnum
            buyerAddress.City = address.city
            buyerAddress.Complement = address.complement
            buyerAddress.CountryEnum = address.countryEnum
            buyerAddress.District = address.district
            buyerAddress.Number = address.number
            buyerAddress.State = address.state
            buyerAddress.Street = address.street
            buyerAddress.ZipCode = address.zipCode

            addressCollection.append(buyerAddress)

        buyer.BuyerKey = request.buyer.buyerKey
        buyer.BuyerReference = request.buyer.buyerReference
        buyer.Email = request.buyer.email
        buyer.FacebookId = request.buyer.facebookId
        buyer.GenderEnum = request.buyer.genderEnum
        buyer.HomePhone = request.buyer.homePhone
        buyer.IpAddress = request.buyer.ipAddress
        buyer.MobilePhone = request.buyer.mobilePhone
        buyer.Name = request.buyer.name
        buyer.PersonTypeEnum = request.buyer.personTypeEnum
        buyer.TaxDocumentNumber = request.buyer.taxDocumentNumber
        buyer.TaxDocumentTypeEnum = request.buyer.taxDocumentTypeEnum
        buyer.WorkPhone = request.buyer.workPhone
        buyer.BuyerAddressCollection = addressCollection

        return buyer

    def CreateBoletoTransaction(self, request):
        """Para criar um objeto CreateBoletoTransaction.
        :param request: A CreateOrderRequest
        :type request: CreateOrderRequest
        :returns: BoletoTransaction object
        """
        url = self.getUrl()
        client = Client(url)
        transactionCollection = []
        boletoTransactionRequest = client.factory.create('ns0:BoletoTransaction')
        for boleto in request.boletoTransactionCollection:
            boletoTransactionRequest.AmountInCents = boleto.amountInCents
            boletoTransactionRequest.BankNumber = boleto.bankNumber
            boletoTransactionRequest.DaysToAddInBoletoExpirationDate = boleto.daysToAddInBoletoExpirationDate
            boletoTransactionRequest.Instructions = boleto.instructions
            boletoTransactionRequest.NossoNumero = boleto.nossoNumero
            boletoTransactionRequest.TransactionReference = boleto.transactionReference
            transactionCollection.append(boletoTransactionRequest)
        return boletoTransactionRequest

    def CreateCreditCardTransactionCollection(self, request):
        """Para criar um objeto CreateBoletoTransactionCollection, contendo  object.
        :param request: A CreateOrderRequest
        :type request: CreateOrderRequest
        :returns: BoletoTransaction object
        """
        url = self.getUrl()
        client = Client(url)
        transactionCollection = []
        arrayOfCreditCardTransaction = client.factory.create('ns0:ArrayOfCreditCardTransaction')

        if request.creditCardTransactionCollection is not None and len(request.creditCardTransactionCollection) > 0:
            for transaction in request.creditCardTransactionCollection:
                creditCardTransaction = client.factory.create('ns0:CreditCardTransaction')
                creditCardTransaction.AmountInCents = transaction.amountInCents
                creditCardTransaction.CreditCardBrandEnum = transaction.creditCardBrandEnum
                creditCardTransaction.CreditCardNumber = transaction.creditCardNumber
                creditCardTransaction.CreditCardOperationEnum = transaction.creditCardOperationEnum
                creditCardTransaction.ExpMonth = transaction.expirationMonth
                creditCardTransaction.ExpYear = transaction.expirationYear
                creditCardTransaction.HolderName = transaction.holderName
                creditCardTransaction.InstallmentCount = transaction.installmentCount
                creditCardTransaction.PaymentMethodCode = transaction.paymentMethodCode
                creditCardTransaction.SecurityCode = transaction.securityCode
                creditCardTransaction.TransactionReference = transaction.transactionReference
                if transaction.InstantBuyKey is not None and len(transaction.InstantBuyKey) > 1:
                    creditCardTransaction.InstantBuyKey = transaction.InstantBuyKey
                if transaction.recurrency is not None:
                    creditCardTransaction.Recurrency.DateToStartBilling = transaction.recurrency.dateToStartBilling
                    creditCardTransaction.Recurrency.FrequencyEnum = transaction.recurrency.frequencyEnum
                    creditCardTransaction.Recurrency.Interval = transaction.recurrency.interval
                    creditCardTransaction.Recurrency.OneDollarAuth = transaction.recurrency.oneDollarAuth
                    creditCardTransaction.Recurrency.Recurrences = transaction.recurrency.recurrences

                transactionCollection.append(creditCardTransaction)

        arrayOfCreditCardTransaction.CreditCardTransaction = transactionCollection
        return arrayOfCreditCardTransaction


    def CreateCreditCardTransaction(self, request):
        """Para criar um objeto CreateCreditCardTransaction
        Não deve ser usado senão excepcionalmente por quem realmente saiba o que está fazendo...
        Está aqui Para fins de documentação apenas
        :param request: A CreateOrderRequest
        :type request: CreateOrderRequest
        :returns: CreateCreditCardTransaction object
        """
        url = self.getUrl()
        client = Client(url)
        transactionCollection = []
        creditCardTransaction = client.factory.create('ns0:CreditCardTransaction')
        for transaction in request.creditCardTransactionCollection:
            creditCardTransaction.AmountInCents = transaction.amountInCents
            creditCardTransaction.CreditCardBrandEnum = transaction.creditCardBrandEnum
            creditCardTransaction.CreditCardNumber = transaction.creditCardNumber
            creditCardTransaction.CreditCardOperationEnum = transaction.creditCardOperationEnum
            creditCardTransaction.ExpMonth = transaction.expirationMonth
            creditCardTransaction.ExpYear = transaction.expirationYear
            creditCardTransaction.HolderName = transaction.holderName
            creditCardTransaction.InstallmentCount = transaction.installmentCount
            creditCardTransaction.PaymentMethodCode = transaction.paymentMethodCode
            creditCardTransaction.SecurityCode = transaction.securityCode
            creditCardTransaction.TransactionReference = transaction.transactionReference

            if transaction.recurrency is not None:
                creditCardTransaction.Recurrency.DateToStartBilling = transaction.recurrency.dateToStartBilling
                creditCardTransaction.Recurrency.FrequencyEnum = transaction.recurrency.frequencyEnum
                creditCardTransaction.Recurrency.Interval = transaction.recurrency.interval
                creditCardTransaction.Recurrency.OneDollarAuth = transaction.recurrency.oneDollarAuth
                creditCardTransaction.Recurrency.Recurrences = transaction.recurrency.recurrences

            transactionCollection.append(creditCardTransaction)

        return transactionCollection


    def ManageOrder(self, request):
        """Calls the ManageOrder method
        :param request: An CreateOrderRequest
        """
        url = self.getUrl()

        client = Client(url)

        ManageCreditCardTransactionRequest = []

        manageOrderRequest = client.factory.create('ns0:ManageOrderRequest')
        arrayOfManageCreditCardTransactionRequest = client.factory.create(
            'ns0:ArrayOfManageCreditCardTransactionRequest')

        if request.transactionCollection is None and request.transactionCollection.count > 0:

            for transaction in request.transactionCollection:
                ManageCreditCardTransactionRequest.append({
                'AmountInCents': transaction.amountInCents,
                'TransactionKey': transaction.transactionKey,
                'TransactionReference': transaction.transactionReference
                })

        manageOrderRequest.MerchantKey = request.merchantKey
        manageOrderRequest.OrderKey = request.orderKey
        manageOrderRequest.OrderReference = request.orderReference
        manageOrderRequest.RequestKey = request.requestKey

        arrayOfManageCreditCardTransactionRequest = ManageCreditCardTransactionRequest

        manageOrderRequest.ManageCreditCardTransactionCollection = arrayOfManageCreditCardTransactionRequest
        manageOrderRequest.ManageOrderOperationEnum = request.operationEnum.Capture

        result = client.service.ManageOrder(manageOrderRequest)

        return result

    def QueryOrder(self, request):
        """Calls the QueryOrder method
        :param request: A QueryOrderRequest
        """
        url = self.getUrl()
        client = Client(url)
        queryOrderRequest = client.factory.create('ns0:QueryOrderRequest')
        queryOrderRequest.MerchantKey = request.merchantKey
        queryOrderRequest.OrderKey = request.orderKey
        queryOrderRequest.OrderReference = request.orderReference
        queryOrderRequest.RequestKey = request.requestKey
        result = client.service.QueryOrder(queryOrderRequest)
        return result

    def CreateOrder(self, request):
        """Calls the CreateOrder method
        :param request: A CreateOrderRequest
        """
        url = self.getUrl()
        client = Client(url)
        createOrderRequest = client.factory.create('ns0:CreateOrderRequest')
        createOrderRequest.AmountInCents = request.amountInCents
        createOrderRequest.AmountInCentsToConsiderPaid = request.amountInCentsToConsiderPaid
        createOrderRequest.CurrencyIsoEnum = request.currencyIsoEnum
        createOrderRequest.MerchantKey = request.merchantKey
        createOrderRequest.OrderReference = request.orderReference
        createOrderRequest.RequestKey = request.requestKey
        createOrderRequest.EmailUpdateToBuyerEnum = request.emailUpdateToBuyerEnum

        if request.buyer is None:
            createOrderRequest.Buyer = request.buyer
        else:
            createOrderRequest.Buyer = self.CreateBuyer(request)

        if request.creditCardTransactionCollection is not None and len(request.creditCardTransactionCollection) > 0:
            creditCardTransactionCollection = self.CreateCreditCardTransactionCollection(request)
            createOrderRequest.CreditCardTransactionCollection = creditCardTransactionCollection
        else:
            createOrderRequest.CreditCardTransactionCollection = None

        if request.boletoTransactionCollection is not None and len(request.boletoTransactionCollection) > 0:
            boletoTransactionCollection = self.CreateBoletoTransaction(request)
            createOrderRequest.BoletoTransactionCollection = boletoTransactionCollection
        else:
            createOrderRequest.BoletoTransactionCollection = None

        print createOrderRequest
        result = client.service.CreateOrder(createOrderRequest)
        self.last_sent = client.last_sent()
        self.last_received = client.last_received()

        # As linhas abaixo servem apenas para simplificar o objeto de resposta para o caso de um único cartão de crédito
        # por transação (a imensa maioria dos casos portanto)
        try:
            result.FirstCreditCardResult = result.CreditCardTransactionResultCollection[0][0]
        except:
            result.FirstCreditCardResult = None
        return result

