from google.appengine.ext import webapp
from google.appengine.ext import db
import logging
from lib.models import Project, Issue
from json import dumps as json
from lib.JSONGenerator import JSONList
from lib.requestUtil import getArgument, htmlCodes

class IssuesHandler(webapp.RequestHandler):
	
	@htmlCodes
	def get(self, projectKey):
		self.response.out.write( JSONList( Project().get(projectKey).issues ) )
		
	@htmlCodes
	def post(self, projectKey): #post = create object
		issue = Issue()
		issue.project = Project().get(projectKey)
		issue.summary = getArgument(self.request, 'summary', '"summary" is a required field!')
		issue.text = self.request.get('text') or ""
		closed = self.request.get('closed')
		if closed: issue.closed = closed.lower() == "true"
		issue.put()
		url = issue.url(self.request.url)
		self.response.headers.add_header("Location", url)
		self.response.out.write(json(url))
		self.response.set_status(201)
