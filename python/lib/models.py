from google.appengine.ext import db
from google.appengine.api import users
from requestUtil import NotFoundException
import json
from JSONGenerator import JSONGenerator

class Parrent(db.Model):
	date = db.DateTimeProperty(auto_now_add=True)
	author = db.UserProperty(auto_current_user_add=True)
	def toJSON(self):
		return JSONGenerator(self)

	def url(self, baseUrl):
		if not baseUrl.endswith('/'):
			baseUrl += '/'
		return baseUrl + str(self.key())

	def get(self, key):
		item = super(Parrent, self).get(key)
		if not item:
			raise NotFoundException('The key for the object you specified was not found! Key: %s' % key)
		return item

class Project(Parrent):
	name = db.StringProperty()

class Issue(Parrent):
	project = db.ReferenceProperty(Project, collection_name='issues')
	summary = db.StringProperty()
	text = db.StringProperty()
	closed = db.BooleanProperty(default=False)

class Comment(Parrent):
	issue = db.ReferenceProperty(Issue, collection_name='comments')
	text = db.StringProperty()
