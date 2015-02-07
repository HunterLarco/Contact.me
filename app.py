from google.appengine.ext.webapp import template
import webapp2
import os


class LandingHandler(webapp2.RequestHandler):
  def get(self):
    template_values = {}
    path = os.path.join(os.path.dirname(__file__), 'landing.html')
    self.response.out.write(template.render(path, template_values))


class LoginHandler(webapp2.RequestHandler):
  def get(self):
    template_values = {}
    path = os.path.join(os.path.dirname(__file__), 'login.html')
    self.response.out.write(template.render(path, template_values))


class SignupHandler(webapp2.RequestHandler):
  def get(self):
    template_values = {}
    path = os.path.join(os.path.dirname(__file__), 'signup.html')
    self.response.out.write(template.render(path, template_values))


app = webapp2.WSGIApplication([
                ('/signup/?', SignupHandler),
                ('/login/?', LoginHandler),
                ('/.*', LandingHandler)
              ], debug=True)