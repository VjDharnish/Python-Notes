import cherrypy
from functools import wraps



class SampleController:

    def validate_userid_header(f):
        @wraps(f)
        def wrapper(self, *args, **kwargs):
            headers = cherrypy.request.headers
            userid = headers.get('userid')
            if not userid:
                raise cherrypy.HTTPError(400, "Missing userid in header")
            self.id = userid
            return f(self, *args, **kwargs)
        return wrapper

    def __init__(self):
        self.id = None
    

    @cherrypy.expose
    @validate_userid_header
    def user(self):
        return f"Hello, your user ID is: {self.id}"


if __name__ == '__main__':
    cherrypy.quickstart(SampleController())