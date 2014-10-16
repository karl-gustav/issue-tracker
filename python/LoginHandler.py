from google.appengine.ext import webapp
from google.appengine.api import users
import logging
	
class LoginHandler(webapp.RequestHandler):
	def get(self):
		user = users.get_current_user()
		if user:
			greeting = ("Welcome, %s! (<a href=\"%s\">sign out</a>)" %
						(user.nickname(), users.create_logout_url("/")))
		else:
			greeting = ("<a href=\"%s\">Sign in or register</a>." %
						users.create_login_url("/"))
		
		self.response.out.write("<html><body><a href='/'>Back</a><br /><br />%s</body></html>" % greeting)