# -*- coding: UTF-8 -*-
__author__ = 'Arcarius Engenharia'

from mundipagg.CreateOrderRequest import CreateOrderRequest
from mundipagg.CreditCardTransaction import CreditCardTransaction
from mundipagg.Gateway import Gateway
import uuid


class NewOrder():
    """ 
    Essa classe é apenas um helper simplificado para a operações de cartão de crédito 
    :rtype : CreateOrderResponse   
    """
    ultimaresposta = None
    MerchantKey = "00000000-0000-0000-0000-000000000000"
    nog = None
    currencyIsoEnum = None

    def __init__(self, MerchantKey, currencyIsoEnum=CreateOrderRequest.DinheiroIsoEnum.BrazillianReal):
        """
        :param MerchantKey: A string que foi atribuido especialmente para a sua loja
        :param currencyIsoEnum: Uma das possívels moedas definidas em CreateOrderRequest.DinheiroIsoEnum
        """
        self.MerchantKey = MerchantKey
        self.currencyIsoEnum = currencyIsoEnum

    def usual_ccorder(self,
                      ZamountInCent, ZcreditCardNumber, ZsecurityCode, ZholderName,
                      ZexpirationYear, ZexpirationMonth,
                      simulado=1,
                      ZcreditCardBrand=CreditCardTransaction.BrandEnum.MasterCard,
                      ZorderReference="Exemplo 123"
    ):
        """
        :param ZamountInCent:
        :param ZcreditCardNumber:
        :param ZsecurityCode:
        :param ZholderName:
        :param ZexpirationYear:
        :param ZexpirationMonth:
        :param simulado:
        :param ZcreditCardBrand:
        :return: CreateOrderResponse:
        :rtype: CreateOrderResponse
        """

        nocct = CreditCardTransaction()
        nocct.paymentMethodCode = simulado
        nocct.amountInCents = ZamountInCent
        nocct.creditCardNumber = ZcreditCardNumber
        nocct.holderName = ZholderName
        nocct.securityCode = ZsecurityCode
        nocct.expirationMonth = ZexpirationMonth
        nocct.expirationYear = ZexpirationYear
        nocct.creditCardBrandEnum = ZcreditCardBrand  # nocct.BrandEnum.MasterCard
        nocct.creditCardOperationEnum = nocct.OperationEnum.AuthAndCapture
        nocct.installmentCount = 1
        nocct.transactionReference = "transactionReference"

        nor = CreateOrderRequest()
        nor.currencyIsoEnum = self.currencyIsoEnum
        nor.amountInCents = ZamountInCent
        nor.amountInCentsToConsiderPaid = 0
        nor.orderReference = ZorderReference
        nor.emailUpdateToBuyerEnum = "Yes"
        nor.merchantKey = self.MerchantKey
        nor.creditCardTransactionCollection.append(nocct)

        if self.nog is None:
            self.nog = Gateway()
        resposta = self.nog.CreateOrder(nor)
        # Descomente as linhas abaixo se for necessário troubleshooting no SOAP / XML
        # xf = open("suds_com_debug.txt","w")
        # xf.write("\nSUDS Client last XML sent:\n\n")
        # xf.write( str(self.nog.last_sent()))
        # xf.write("\n\nSUDS Client last XML received:\n\n")
        # xf.write( str(self.nog.last_received()) )
        return resposta

    def instantbuy_ccorder(self, ZamountInCent, ZinstantBuyKey, ZcreditCardBrand='Mastercard',
                           ZorderReference="Exemplo 123", simulado=1):
        """
        :param ZamountInCent:
        :param ZinstantBuyKey:
        :param simulado:
        :param ZcreditCardBrand:
        :return: arcCreateOrderResponse:
        :rtype: CreateOrderResponse
        """

        nocct = CreditCardTransaction()
        nocct.paymentMethodCode = simulado
        nocct.amountInCents = ZamountInCent
        nocct.creditCardBrandEnum = ZcreditCardBrand  # nocct.BrandEnum.MasterCard
        nocct.creditCardOperationEnum = nocct.OperationEnum.AuthAndCapture
        nocct.installmentCount = 1
        nocct.InstantBuyKey = ZinstantBuyKey
        nocct.transactionReference = "transactionReference"

        nor = CreateOrderRequest()
        nor.currencyIsoEnum = self.currencyIsoEnum
        nor.amountInCents = ZamountInCent
        nor.amountInCentsToConsiderPaid = 0
        nor.orderReference = "Order 123"
        nor.emailUpdateToBuyerEnum = "Yes"
        nor.merchantKey = self.MerchantKey
        nor.creditCardTransactionCollection.append(nocct)

        if self.nog is None:
            self.nog = Gateway()
        resposta = self.nog.CreateOrder(nor)
        # Descomente as linhas abaixo se for necessário troubleshooting no SOAP / XML
        # xf = open("suds_com_debug.txt","w")
        # xf.write("\nSUDS Client last XML sent:\n\n")
        # xf.write( str(self.nog.last_sent()))
        # xf.write("\n\nSUDS Client last XML received:\n\n")
        # xf.write( str(self.nog.last_received()) )
        return resposta

