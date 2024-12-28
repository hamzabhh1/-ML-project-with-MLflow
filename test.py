# Import the logger
from src.mlProject import logger

def main():
    # Log some test messages
    logger.info("Main function started.")
    logger.debug("This is a debug message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    logger.critical("This is a critical message.")
    
if __name__ == "__main__":
    main()
