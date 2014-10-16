import webapp2
from python.LoginHandler import LoginHandler
from python.ProjectsHandler import ProjectsHandler
from python.ProjectHandler import ProjectHandler
from python.IssuesHandler import IssuesHandler
from python.IssueHandler import IssueHandler
from python.CommentHandler import CommentHandler
from python.CommentsHandler import CommentsHandler

app = webapp2.WSGIApplication([
		('/log(?:in|out)/?', LoginHandler),
		('/1/projects/?', ProjectsHandler),
		('/1/projects/([\w\-]+)', ProjectHandler),
		('/1/projects/([\w\-]+)/issues/?', IssuesHandler),
		('/1/projects/([\w\-]+)/issues/([\w\-]+)', IssueHandler),
		('/1/projects/([\w\-]+)/issues/([\w\-]+)/comments/?', CommentsHandler),
		('/1/projects/([\w\-]+)/issues/([\w\-]+)/comments/([\w\-]+)', CommentHandler),
	], debug=True)
