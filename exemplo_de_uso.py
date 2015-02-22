# -*- coding: UTF-8 -*-
__author__ = 'Arcarius Engenharia'

# Isso é um exemplo de implementação bem simplificada de requisição por cartão de crédito.(testado em Fev/2015)
# E diferente da última revisão que estava no GITHUB da mundipagg, essa versão foi minimamente testada antes de se publicar...
# Se precisarem de uma consultoria no assunto, entrem em contato conosco.(Arcarius Engenharia)
# O suporte da mundipagg não costuma ajudar muito quando o assunto envolve python...

from mundipagg.ccred_helper import NewOrder
from mundipagg.Gateway import CreateOrderResponse, CreditCardTransactionReponse
from mundipagg.CreateOrderRequest import CreateOrderRequest
from mundipagg.CreditCardTransaction import CreditCardTransaction

# Atenção: Preencha aqui a sua chave do MundiPagg !!!! Se não fizer isso vai obter erros mesmo no ambiente simulado.
neword = NewOrder(MerchantKey = "12345678-1234-1234-1234-123456789012")
newordres = neword.usual_ccorder(
    ZamountInCent=200, ZcreditCardNumber="1234123412341234",
    ZsecurityCode="123", ZholderName="Ze da Silva",
    ZexpirationYear=2017, ZexpirationMonth=5,
    ZcreditCardBrand=CreditCardTransaction.BrandEnum.MasterCard,
    ZorderReference="Exemplo234",
    simulado=1)

# Descomente as linhas abaixo se for necessário troubleshooting no SOAP / XML.
# Isso vai gravar o XML enviado e a resposta correspondente no arquivo suds_com_debug.txt
xf = open("suds_com_debug.txt", "w")
xf.write("\nSUDS Client last XML sent:\n\n")
xf.write(str(neword.nog.last_sent))
xf.write("\n\nSUDS Client last XML received:\n\n")
xf.write(str(neword.nog.last_received))


print "Functionou? %s" % newordres.Success
if newordres.ErrorReport is not None:
    print newordres.ErrorReport.ErrorItemCollection[0][0].Description
print "InstantBuyerKey=%s" % newordres.FirstCreditCardResult.InstantBuyKey
print "OrderKey=%s" % newordres.OrderKey
print "OrderReference=%s" % newordres.OrderReference
print "OrderStatusEnum=%s" % newordres.OrderStatusEnum
print "RequestKey=%s" % newordres.RequestKey
print "CreditCard Trahsactuion Status: %s" % newordres.FirstCreditCardResult.CreditCardTransactionStatusEnum

print "MundiPaggSuggestion=%s" % newordres.MundiPaggSuggestion
