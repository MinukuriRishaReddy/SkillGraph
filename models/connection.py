import os
import logging
from dotenv import load_dotenv
from neo4j import GraphDatabase
from neomodel import db, config

load_dotenv()

logger = logging.getLogger(__name__)

# Lazy connection holders
_driver = None
_neomodel_configured = False

class Neo4jWrapper:
    """Compatibility layer to mimic py2neo's Graph().run().data() interface using the official driver."""
    def __init__(self, driver):
        self.driver = driver

    def run(self, query, **parameters):
        with self.driver.session() as session:
            result = session.run(query, parameters)
            return Neo4jResult(result.data())

class Neo4jResult:
    """Helper to provide .data() method on results with ID normalization."""
    def __init__(self, data):
        self._data = []
        for record in data:
            # AuraDB returns elementId, which might be a string like '4:0'.
            # We try to find 'id' in the record and ensure it's usable.
            normalized_record = record.copy()
            if 'id' in normalized_record:
                val = normalized_record['id']
                # If it's a string from elementId, we try to keep it as is 
                # or hash it if the frontend strictly needs an integer.
                # For this project, we'll try to convert it to a simple int if possible.
                if isinstance(val, str) and ":" in val:
                    try:
                        normalized_record['id'] = int(val.split(":")[-1])
                    except:
                        pass
            self._data.append(normalized_record)

    def data(self):
        return self._data

def _get_neo4j_config():
    """Get Neo4j connection config from environment variables."""
    # Priority 1: Full URI (Best for AuraDB)
    full_uri = os.getenv('NEO4J_URI')
    if full_uri:
        # Extract components for neomodel which needs bolt://user:pass@host
        # and for the driver which needs neo4j+s://host
        return full_uri, os.getenv('NEO4J_USER', 'neo4j'), os.getenv('PASSWORD', 'neo4jpass')
    
    # Priority 2: Individual components
    scheme = os.getenv('SCHEME', 'bolt://')
    url = os.getenv('URL', 'localhost:7687')
    username = os.getenv('NEO4J_USER', os.getenv('USERNAMEE', 'neo4j'))
    password = os.getenv('PASSWORD', 'neo4jpass')
    return f"{scheme}{url}", username, password

def get_graph():
    """Get a lazy Neo4j connection wrapper."""
    global _driver
    if _driver is None:
        uri, username, password = _get_neo4j_config()
        try:
            _driver = GraphDatabase.driver(uri, auth=(username, password))
            # Test connection
            _driver.verify_connectivity()
            logger.info(f"Connected to Neo4j via official driver at {uri}")
        except Exception as e:
            logger.error(f"Failed to connect to Neo4j at {uri}: {e}")
            raise
    return Neo4jWrapper(_driver)

def configure_neomodel():
    """Configure neomodel database connection."""
    global _neomodel_configured
    if not _neomodel_configured:
        uri, username, password = _get_neo4j_config()
        # Neomodel 6.x supports bolt+s:// and neo4j+s://
        # We need to build the URL as: neo4j+s://user:password@host
        host = uri.replace("neo4j+s://", "").replace("neo4j://", "").replace("bolt+s://", "").replace("bolt://", "")
        # Remove any trailing slashes
        host = host.split('/')[0]
        
        # Determine correct protocol based on URI
        protocol = "neo4j+s" if "neo4j+s" in uri else "bolt"
        connection_url = f'{protocol}://{username}:{password}@{host}'
        
        db.set_connection(connection_url)
        config.DATABASE_URL = connection_url
        _neomodel_configured = True
        logger.info(f"Neomodel configured with {protocol} for host: {host}")

def check_connection():
    """Test the Neo4j connection and return status."""
    try:
        graph = get_graph()
        result = graph.run("RETURN 1 AS test").data()
        if result and result[0]['test'] == 1:
            return {"status": "connected", "message": "Neo4j connection successful"}
        return {"status": "error", "message": "Unexpected response from Neo4j"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
