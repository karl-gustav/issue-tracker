from google.appengine.ext import webapp
from google.appengine.ext import db
import logging
from lib.models import Issue, Comment
from json import dumps as json
from lib.JSONGenerator import JSONList
from lib.requestUtil import getArgument, htmlCodes

class CommentsHandler(webapp.RequestHandler):
	
	@htmlCodes
	def get(self, projectKey, issueKey):
		self.response.out.write( JSONList( Issue().get(issueKey).comments ) )
		
	@htmlCodes
	def post(self, projectKey, issueKey): #post = create object
		comment = Comment()
		comment.issue = Issue().get(issueKey)
		comment.text = getArgument(self.request, 'text', '"text" is a required field!')
		comment.put()
		url = comment.url(self.request.url)
		self.response.headers.add_header("Location", url)
		self.response.out.write(json(url))
		self.response.set_status(201)
