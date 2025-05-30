import cherrypy
import random
class SessionExample:
    @cherrypy.expose
    def store(self, item=None):
        if not 'items' in cherrypy.session:
            cherrypy.session['items'] = {}
        if item:
            cherrypy.session['items'][item]= random.randint(1,19999999999)
            return f"Added {item} to session. Current items: {cherrypy.session['items']}"
        return f"Current items in session: {cherrypy.session['items']}"


    @cherrypy.expose
    def get_session(self,item):
        if 'items' in cherrypy.session:
            if item in cherrypy.session['items']:
                return f"Item {item} found in session with value: {cherrypy.session['items'][item]}"
            else:
                return f"Item {item} not found in session."
            return f"Session items: {cherrypy.session['items']}"
        else:
            return "No items in session."

    @cherrypy.expose
    def index(self):
        if not 'count' in cherrypy.session:
            cherrypy.session['count'] = 0
        cherrypy.session['count'] += 1
        return f"You've visited this page {cherrypy.session['count']} times!"

if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.storage_type': 'ram',
            'tools.sessions.timeout': 3600  # Session timeout in seconds (1 hour)
        }
    }
    cherrypy.quickstart(SessionExample(), '/', conf)