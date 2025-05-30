import cherrypy
import random
import string


class HelloWorld():
    @cherrypy.expose
    def generate(self,length =5):
        str1 =  ''.join(random.sample(string.hexdigits,int(length)))
        cherrypy.session['string1']=str1
        return str1
    

    def display(self):
        return cherrypy.session['string1']

    def index(self):
        return """<html>
          <head></head>
          <body>
            <form method="get" action="generate">
              <input type="text" value="8" name="length" />
              <button type="submit">Give it now!</button>
            </form>
          </body>
        </html>"""

    def hello(self):
        return "welcome dharun"
    
    
if __name__  == '__main__':
    conf ={
        '/':{
            'tools.sessions.on':True
        }

    }
    cherrypy.quickstart(HelloWorld(),'/',conf)
