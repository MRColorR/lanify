import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import random
import time
import logging
import capcha_solver

def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run(delay_multiplier=1):
    setup_logging()
    logging.info('Starting the script...')

    # Read variables from the OS env
    email = os.getenv('USER')
    password = os.getenv('PASS')
    apikey = os.getenv('API')
    extension_id = 'fljkmocmlejbiaohjiecblmdjpaohapdom'
    # Check if credentials are provided
    if not email or not password:
        logging.error('No username or password provided. Please set the GRASS_USER and GRASS_PASS environment variables.')
        return  # Exit the script if credentials are not provided

    chrome_options = Options()
    chrome_options.add_extension(f'./{extension_id}.crx')

    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless=new')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0")

    # Initialize the WebDriver
    driver = webdriver.Chrome(options=chrome_options)
    # Navigate to a webpage
    logging.info('Navigating to the website...')
    driver.get("https://app.lanify.ai/")

    time.sleep(random.randint(3,7)*delay_multiplier)

    logging.info('Entering credentials...')
    username_input = driver.find_element(By.XPATH, '//input[@placeholder="Username or Email"]')
    username_input.send_keys(email)
    password_input = driver.find_element(By.XPATH, '//input[@type="password" and @placeholder="Password"]')

    password_input.send_keys(password)
    
    logging.info('Clicking the login button...')
    
    code = capcha_solver.capsolver(apikey)
    print(f"Successfully solved the Captcha.")

    # Set the solved Captcha
    recaptcha_response_element = driver.find_element(By.ID, 'g-recaptcha-response')
    driver.execute_script(f'arguments[0].value = "{code}";', recaptcha_response_element)

    # Submit the form
    button = driver.find_element(By.XPATH, '//button[contains(text(), "Access my account")]')
    button.click()
    logging.info('Waiting response...')

    time.sleep(random.randint(10,50)*delay_multiplier)
    logging.info('Accessing extension settings page...')
    driver.get(f'chrome-extension://fjkmocmlejbiaohijecbmdjpaohapdom/src/pages/popup/index.html')
    time.sleep(random.randint(10,17)*delay_multiplier)
    logging.info('Clicking the extension button...')
    password_input = driver.find_element(By.XPATH, '//input[@type="password" and @placeholder="Enter your password"]')
    password_input.send_keys(password)

    button = driver.find_element(By.XPATH, '//button[contains(text(), "Unlock")]')

    # Click the button
    button.click()

    logging.info('Logged in successfully.')
    logging.info('Earning...')


    while True:
        try:
            time.sleep(3600)
        except KeyboardInterrupt:
            logging.info('Stopping the script...')
            driver.quit()
            break

if __name__ == '__main__':
    for i in range(1,5):
        try:
            run(i)
        except KeyboardInterrupt:
            logging.info('Stopping the script...')
            break
        except Exception as e:
            logging.error(e)
            logging.info('Trying again......')

