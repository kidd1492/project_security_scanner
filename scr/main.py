from main_menu import start
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, filename='app.log', format='%(asctime)s - %(levelname)s - %(message)s')

    
if __name__ == "__main__":
    start()
