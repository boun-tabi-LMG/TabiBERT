import logging
import os
from datetime import datetime

def setup_logging(name: str):
    """
    Set up logging configuration for a specific module.
    Outputs to both console and log file.
    
    Args:
        name (str): Name of the module for the log file
    """
    # Create logs directory if it doesn't exist
    os.makedirs('logs', exist_ok=True)
    
    # Get the current timestamp for the log file name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = f'logs/{name}_{timestamp}.log'
    
    # Remove any existing handlers to prevent duplicate logging
    root_logger = logging.getLogger()
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)
    
    # Create formatters
    detailed_formatter = logging.Formatter(
        '%(levelname)s - %(asctime)s - %(name)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    console_formatter = logging.Formatter(
        '%(levelname)s - %(message)s'
    )
    
    # Create and configure console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(console_formatter)
    
    # Create and configure file handler
    file_handler = logging.FileHandler(log_file, mode='w', encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)  # Log more details to file
    file_handler.setFormatter(detailed_formatter)
    
    # Configure root logger
    root_logger.setLevel(logging.DEBUG)
    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)
    
    # Create a logger with the module name
    logger = logging.getLogger(name)
    
    # Log the start of a new section
    logger.info(f"=== Starting {name} ===")
    logger.info(f"Log file: {log_file}")
    
    return logger