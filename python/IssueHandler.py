from google.appengine.ext import webapp
from google.appengine.ext import db
import logging
from lib.models import Project, Issue
from json import dumps as json
from lib.JSONGenerator import JSONList
from lib.requestUtil import getArgument, htmlCodes

class IssueHandler(webapp.RequestHandler):
	
	@htmlCodes
	def get(self, projectKey, key):
		self.response.out.write( Issue().get(key).toJSON() )
	
	@htmlCodes
	def put(self, projectKey, key): #update
		issue = Issue().get(key)
		issue.project = Project().get(projectKey)
		issue.summary = self.request.get('summary') or issue.summary
		issue.text = self.request.get('text') or issue.text
		closed = self.request.get('closed')
		if closed: issue.closed = closed.lower() == "true"
		issue.put()
		url = issue.url(self.request.url)
		self.response.headers.add_header("Location", url)
		self.response.out.write(json(url))
	
	@htmlCodes
	def delete(self, projectKey, key):
		issue = Issue().get(key)
		keys = [key]
		for comment in issue.comments:
			keys.append(str(comment.key()))
		logging.info('Deleting: ' + str(keys))
		db.delete(keys)
		self.response.out.write(json(keys))
