# -*- coding: UTF-8 -*-
__author__ = 'Arcarius Engenharia'

class CreditCardTransaction:
	"""Class that hold Credit Card Transaction information"""

	#: Transaction amount in cents [Long]
	amountInCents = None

	#: Card brand. Use the BrandEnum class [String]
	creditCardBrandEnum = None

	#: Credit card number [String]
	creditCardNumber = None

	#: Type of operation. User OperationEnum class [String]
	creditCardOperationEnum = None

	#: Credit card expiration month [Integer]
	expirationMonth = None

	#: Credit card expiration year [Integer]
	expirationYear = None

	#: Name in the credit card [String]
	holderName = None

	#: Transaction installments count [Integer]
	installmentCount = None

	#: Card security code [Integer]
	securityCode = None

	#: Code to select the payment method. Can be Cielo, Redecard and others [Integer]
	paymentMethodCode = None

	#: Custom transaction identifier [String]
	transactionReference = None

	#: Fill this property when creating a recurrency transaction. 
	#: [Recurrency] Transaction recurrency information.
	recurrency = None

	#: Brand enum
	brandEnum = None

	#: Operation enum
	operationEnum = None

	#: Correção... estava faltando esse campo (Guid)
	InstantBuyKey = None

	class BrandEnum:
		"""Credit card brand enum"""
		Visa = 'Visa'
		MasterCard = 'Mastercard'
		AmericanExpress = 'Amex'
		Hipercard = 'Hipercard'
		Diners = 'Diners'
		Elo = 'Elo'
		Aura = 'Aura'
		Discover = 'Discover'

	class OperationEnum:
		"""Operation type enum"""
		AuthOnly = 'AuthOnly'
		AuthAndCapture = 'AuthAndCapture'
		AuthAndCaptureDelay = 'AuthAndCaptureDelay'	


	def __init__(self):
		self.brandEnum = self.BrandEnum	
		self.operationEnum = self.OperationEnum
		
