import cherrypy
import logging 
from typing import Dict, Any

LOGGER = logging.getLogger("Weaviate::APP")
class HelloWorld:
    @cherrypy.expose
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

    @cherrypy.expose('delete_collection')
    @cherrypy.tools.json_out()
    @cherrypy.tools.allow(methods=['DELETE'])
    def schema_delete_collection(self, collection_name: str) -> Dict[str, Any]:
        """Deletes a collection from Weaviate."""
        try:
            if not collection_name:
                cherrypy.response.status = 400
                return {"status": "FAILED", "message": "Collection name is required"}
                
            # self.weaviate_app.delete_collection(self.service,collection_name)
            return {"status": "SUCCESS", "message": "Collection deleted successfully "+collection_name}
        except Exception as e:
            LOGGER.error(f"WeaviateAdminController: {self.service}: schema_delete_collection: {str(e)}",exc_info=True)
            cherrypy.response.status = 500
            return {"status": "FAILED", "message": f"Failed to delete collection {str(e)}."}

if __name__ == '__main__':
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    
    # Create a logger
    logger = logging.getLogger("Weaviate::APP")
    
    # Create log messages
    logger.info("Starting the application")
    
    # Start the CherryPy server
    cherrypy.quickstart(HelloWorld())