from google.appengine.ext import webapp
from google.appengine.ext import db
import logging
from lib.models import Issue, Comment
from json import dumps as json
from lib.JSONGenerator import JSONList
from lib.requestUtil import getArgument, htmlCodes

class CommentHandler(webapp.RequestHandler):
	
	@htmlCodes
	def get(self, projectKey, issueKey, key):
		self.response.out.write( Comment().get(key).toJSON() )
	
	@htmlCodes
	def put(self, projectKey, issueKey, key): #update
		comment = Comment().get(key)
		comment.Issue = Issue().get(issueKey)
		comment.text = getArgument(self.request, 'text', '"text" is a required field!')
		comment.put()
		url = comment.url(self.request.url)
		self.response.headers.add_header("Location", url)
		self.response.out.write(json(url))
	
	@htmlCodes
	def delete(self, projectKey, issueKey, key):
		comment = Comment().get(key)
		comment.delete()
		self.response.out.write(json(str(comment.key())))
