# -*- coding: UTF-8 -*-
__author__ = 'Arcarius Engenharia'

# Isso é um exemplo de implementação bem simplificada de requisição por cartão de crédito.(testado em Fev/2015)
# E diferente da última revisão que estava no GITHUB da mundipagg, essa versão foi minimamente testada antes de se publicar...
# Se precisarem de uma consultoria no assunto, entrem em contato
# conosco.(Arcarius Engenharia)

from mundipagg.ccred_helper import NewOrder
from mundipagg.CreditCardTransaction import CreditCardTransaction

# Atenção: Preencha aqui a sua chave do MundiPagg !!!! Se não fizer isso
# vai obter erros mesmo no ambiente simulado.
neword = NewOrder(MerchantKey="1cb019a7-105a-40bf-a205-bdfd55d58c2f")
newordres = neword.usual_ccorder(
    amountInCent=200, creditCardNumber="1234123412341234",
    securityCode="123", holderName="e da Silva",
    expirationYear=2017, expirationMonth=5,
    creditCardBrand=CreditCardTransaction.BrandEnum.MasterCard,
    orderReference="Exemplo234",
    simulado=1)


print("Functionou? %s" % newordres.Success)
if newordres.ErrorReport is not None:
    print(" ...%s" % newordres.ErrorReport.ErrorItemCollection[0][0].Description)
print("OrderKey=%s" % newordres.OrderKey)
print("OrderReference=%s" % newordres.OrderReference)
print("OrderStatusEnum=%s" % newordres.OrderStatusEnum)
print("RequestKey=%s" % newordres.RequestKey)
if newordres.FirstCreditCardResult is not None:
    print("InstantBuyerKey=%s" % newordres.FirstCreditCardResult.InstantBuyKey)
    print("CreditCard Trahsactuion Status: %s" % newordres.FirstCreditCardResult.CreditCardTransactionStatusEnum)
print("MundiPaggSuggestion=%s" % newordres.MundiPaggSuggestion)
