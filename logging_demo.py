import logging

logging.basicConfig(
    filename ="weaviate_insert.log",
)
logger = logging.getLogger("Weaviate::APP")
# Create log messages
# logging.debug("This is a debug message")

logger.info("Finished importing data for sample_63    Object Count  :43800   Time Taken:23.655757665634155")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")
