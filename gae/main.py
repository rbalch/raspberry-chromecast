import webapp2
from google.appengine.api import app_identity, urlfetch


class GiphyCron(webapp2.RequestHandler):
    def get(self):
        app_id = app_identity.get_application_id()
        url = 'https://{app_id}.firebaseapp.com/giphy/search'.format(app_id=app_id)
        result = urlfetch.fetch(url)
        self.response.status = result.status_code
        self.response.write(result.content)


app = webapp2.WSGIApplication([
    ('/giphy-cron/', GiphyCron),
], debug=True)
