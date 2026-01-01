import logging
import os
from datetime import datetime

def setup_logging(name: str):
    """
    Set up logging configuration for a specific module.
    
    Args:
        name (str): Name of the module for the log file
    """
    # Create logs directory if it doesn't exist
    os.makedirs('logs', exist_ok=True)
    
    # Get the current timestamp for the log file name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = f'logs/inference_{timestamp}.log'
    
    # Remove any existing handlers to prevent duplicate logging
    root_logger = logging.getLogger()
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)
    
    # Configure logging with a simpler format
    logging.basicConfig(
        level=logging.INFO,
        format='%(levelname)s - %(asctime)s - %(name)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[
            # Console handler
            logging.StreamHandler(),
            # File handler - create a single log file for the entire run
            logging.FileHandler(log_file, mode='w', encoding='utf-8')
        ]
    )
    
    # Create a logger with the module name
    logger = logging.getLogger(name)
    
    # Log the start of a new section
    logger.info(f"=== Starting {name} ===")
    
    return logger 