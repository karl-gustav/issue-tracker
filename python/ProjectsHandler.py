from google.appengine.ext import webapp
from google.appengine.api import users
from google.appengine.ext import db
import logging
from json import dumps as json
from lib.models import Project, Issue
from lib.JSONGenerator import JSONList
from lib.requestUtil import htmlCodes, getArgument
	
class ProjectsHandler(webapp.RequestHandler):
	@htmlCodes
	def get(self):
		self.response.out.write( JSONList( Project().all() ) )

	@htmlCodes
	def post(self): #post = create object
		project = Project()
		project.name = getArgument(self.request, 'name', 'The "name" parameter can\'t be empty')
		project.put()
		url = project.url(self.request.url)
		self.response.headers.add_header("Location", url)
		self.response.out.write(json(url))
		self.response.set_status(201)
