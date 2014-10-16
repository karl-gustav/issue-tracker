import logging
from google.appengine.ext.db import BadKeyError


class NotFoundException(Exception): pass
class MissingArgumentException(Exception): pass

def getArgument(request, argumentName, errorMessage='', allowEmpty=False):
	argument = request.get(argumentName)
	if allowEmpty:
		return argument
	if not argument:
		if errorMessage:
			raise MissingArgumentException(errorMessage)
		else:
			raise MissingArgumentException()
	return argument

def htmlCodes(func):
	def _decorator(self, *args, **kwargs):
		logging.info("%s request:\n\t%s" % (func.__name__, "\n\t".join( str(self.request).splitlines() )))
		try:
			func(self, *args, **kwargs)
		except NotFoundException, e:
			setResponseError(self.response, e, 404, e.message)
		except MissingArgumentException, e:
			setResponseError(self.response, e, 400, e.message)
		except BadKeyError, e:
			setResponseError(self.response, e, 400, "You used an invalid key to retrieve you object!")

	return _decorator

def setResponseError(response, exception, code, message):
	logging.info("Converting %s to HTML status code %s" % (exception.__class__.__name__, code))
	response.clear()
	response.set_status(code)
	response.out.write(message)

