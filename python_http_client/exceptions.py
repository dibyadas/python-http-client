class HTTPError(Exception):
	''' Base of all other errors'''
	def __init__(self,error):
		self.code = error.code
		self.reason = error.reason
		#self.headers = error.headers

class BadRequestsError(HTTPError):
	pass

class UnauthorizedError(HTTPError):
	pass

class ForbiddenError(HTTPError):
	pass

class NotFoundError(HTTPError):
	pass

class MethodNotAllowedError(HTTPError):
	pass

class PayloadTooLargeError(HTTPError):
	pass

class UnsupportedMediaTypeError(HTTPError):
	pass

class TooManyRequestsError(HTTPError):
	pass

class InternalServerError(HTTPError):
	pass

class ServiceUnavailableError(HTTPError):
	pass

err_dict = { 	400 : BadRequestsError,
				401 : UnauthorizedError,
				403 : ForbiddenError,
				404 : NotFoundError,
				405 : MethodNotAllowedError,
				413 : PayloadTooLargeError,
				415 : UnsupportedMediaTypeError,
				429 : TooManyRequestsError,
				500 : InternalServerError,
				503 : ServiceUnavailableError
}

def handle_error(error):
	exc = err_dict[error.code](error)
	exc.__cause__ = None
	raise exc
