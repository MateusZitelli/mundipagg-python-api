class QueryOrderRequest:
	#: MundiPagg merchant identification [GUID]
	merchantKey = None

	#: Unique order identification. Generated by MundiPagg
	orderKey = None

	#: Custom order identification
	orderReference = None

	#: If not send, it will be generate automatically in the webservice and returned in response.
    #: Web service request identification, it is used for investigate problems with webservice requests.
    #: [Guid]
	requestKey = None
	
	def __init__(self):
		self.requestKey = '00000000-0000-0000-0000-000000000000'
		