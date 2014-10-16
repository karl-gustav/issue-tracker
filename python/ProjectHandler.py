from google.appengine.ext import webapp
from google.appengine.api import users
from google.appengine.ext import db
import logging
from json import dumps as json
from lib.models import Project, Issue
from lib.JSONGenerator import JSONList
from lib.requestUtil import htmlCodes, getArgument
	
class ProjectHandler(webapp.RequestHandler):
	@htmlCodes
	def get(self, key):
		self.response.out.write( Project().get(key).toJSON() )
		
	@htmlCodes
	def put(self, key): #update
		project = Project().get(key)
		project.name = getArgument(self.request, 'name', 'The "name" parameter can\'t be empty')
		project.put()
		url = project.url(self.request.url)
		self.response.headers.add_header("Location", url)
		self.response.out.write(json(url))

	@htmlCodes		
	def delete(self, key):
		keys = [key]
		project = Project().get(key)
		for issue in project.issues:
			for comment in issue.comments:
				keys.append(str(comment.key()))
			keys.append(str(issue.key()))
		logging.info('Deleting: ' + str(keys))
		db.delete(keys)
		self.response.out.write(json(keys))
