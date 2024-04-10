from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException , ElementClickInterceptedException, TimeoutException
import time

# Configuration
CHROME_DRIVER_PATH = './chromedriver'
CHROME_FOR_TEST_PATH = '/Applications/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing'
TELEGRAM_WEB_URL = 'https://web.telegram.org/k/'
TELEGRAM_GROUP_NAME = 'Your group here'

# XPaths
GROUP_NAME_XPATH = '//*[@id="column-left"]/div/div[3]/div[2]/div/div[2]/div/div/div[2]/div[1]/div[1]'
GROUP_CREATION_BUTTON_XPATH = '//*[@id="column-left"]/div/div[2]/div[2]/button'
FIRST_DISCUSSION_XPATH = '//*[@id="folders-container"]/div/div[2]/ul/a[1]'
MESSAGE_FIELD_XPATH = '/html/body/div[1]/div/div[2]/div/div/div[4]/div/div[1]/div/div[8]/div[1]/div[1]'
GROUP_SETTINGS_XPATH = '/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div[1]/div/div[1]'
ADD_MEMBER_XPATH = '/html/body/div[1]/div/div[3]/div/div/div[2]/button'
SEARCH_FIELD_XPATH = '/html/body/div[7]/div/div[1]/div/input'
SELECT_FIRST_DISCUSSION_XPATH = '/html/body/div[7]/div/div[2]/div/div/div/div/div[3]/div/div/ul/a[1]'
ADD_BUTTON_XPATH = '/html/body/div[7]/div/div[2]/button[1]/div'

# Button XPaths
BUTTON_XPATHS = [
    '/html/body/div[1]/div/div[1]/div/div/div[3]/button/div',
    '//*[@id="new-menu"]/div[3]/div[2]',
    '/html/body/div[1]/div/div[2]/div/div/div/div/canvas[2]',
    '/html/body/div[1]/div/div[1]/div/div[2]/div[2]/button'
]

# Local storage items: this is used as cookies to authenticate the user
LOCAL_STORAGE_ITEMS = {
    "k_build": "499",
    "dc5_server_salt": "4959e5d5abad7446",
    "user_auth": '{"dcID":4,"date":1712543609,"id":5145586844}',
    "xt_instance": '{"id":1466872,"idle":true,"time":1712704105865}',
    "dc": "4",
    "dc4_auth_key": ("7ea75c8660c1c309109c1f16646a8d8891012b3cfa863dd522e144d25afe2d6452004aa06a0fbe259d594e1d7687a440"
                     "3c65148d520ab7abf4f0f61f8139fb8047dc06fe54f6c6527d44b1e344b596e030516e3ebb6883e25fdaef69540c3a22"
                     "e253d37902201e5b4a41b7de1279599ebdd207f54b75648423f6433a6ff7ebc75578d21a0ebb57f05d77ef5d8481cd18"
                     "4edf53c06d00505dfa948903886da0205d767da749afd82336229b6849d76b9f4596fa57863022464598fa57d37bb38b"
                     "0e853d4c2be506051ede26c05e2030dfce90ac568f2a717ad06749dcd10f2e5675c44d88d7541f73feabf6c9a91046c1"
                     "ffbffd30f3c15382ce133a1e9b643931"),
    "dc2_auth_key": ("aeccc3da8a801570469a5b4545d344849231e365301fdee9914dbcbcb74160c576c5a628f13477770a735714e6660b4f"
                     "b657b5bfd9171367cf9dab1c897e4b25f40ec33d71601f704e2126737a7a989998916d410d8b2e96735eef2a2c4b00c9"
                     "1ef8dceb349c179bf1d98165edde0a006acac05f904827db2745bf8677aad969cf21f6049016c789a35c5be63b1796af"
                     "8d43628a7d2fb740fe01c117218fc6386cc26051304d61825ea3e72d30a29de22cdb9bc40426b1cd4e938394fcd22653"
                     "e4f7add1d756b113469e71e59abd7503deb6ace29aa3ccb7cfdaf9924e370e8ee7e6fd2e02e59727152fbc053f38c5d8"
                     "65de3769f0515a4cd00f8ad8295004bd"),
    "dc4_server_salt": "2bac4e5423b5715b",
    "dc1_server_salt": "c99edd636909a231",
    "tgme_sync": '{"canRedirect":true,"ts":1712688590}',
    "dc2_server_salt": "63a276859ba3d7d0",
    "kz_version": "K",
    "auth_key_fingerprint": "aeccc3da",
    "dc1_auth_key": ("2f698754eea2fa2c6afc316561c703f7c8d1b57154badfc5ade4c8afa21a06c6ab541b4a9c94f92c8b0a29e6fb644b5a"
                     "ab6706a412bd181631c452e887f634845ac2b697bec9fc983d6d84fded3fab554da03df6ccdba6d0333086edc516ca9b"
                     "261e85251efd5ebd9f0f639d3912ac402fb59e65f7e4d426394891f6a02cdb616332114a42152c8608ec524453793fff"
                     "6261f93c4b56342b6238c8dd149bcffa4a8afa187b252b956ea151087c617ad5836dae1738f32635e90f3afa7d2d56dc"
                     "5fbbe38fad0bfe63f9de813bd29c8b7b9ac3a8f854a2867ee2bd7d97ce3fe828a28fb8252d6a9763856187c4b9e81314"
                     "ac6417e0df6658764c0e3eccd5347be8"),
    "state_id": 3865208015,
    "dc5_auth_key": ("4732a9470cca1ebd052e4e518d283d05a403cfb70f1b451bc80377b5a9cbc1cc0277e307dca4bd21c310b6fabbaa5733"
                     "43767c9110540cb2c242227a31b97a5661d9f6100377c498c1937f08b721ee26365d3f604a0e3a5a9134416281f2dcc5"
                     "2839a82a1719b1e5b4776677df25974438e4ed54f44d9a8f7c1805a880c001649224ea73918ea27e87c42f57edbc1cbc"
                     "2e421e2a40c38f54c7a2e13f0efbe11464687d336b8d940ac7b9cf96cb11e2b820db0031c5653662553861d07129bf26"
                     "269d664acf1cf6ee7037eec5d513454ef0e75a7856cb5a29490d88d66095bec6e967d255f6c27a0375328188d4ffe883"
                     "19301bbbc711797e66b9bf7beeee7be0")
}


# Functions
def setup_driver(chrome_driver_path, chrome_for_test_path):
    service = Service(executable_path=chrome_driver_path)
    options = Options()
    options.binary_location = chrome_for_test_path
    driver = webdriver.Chrome(options=options, service=service)
    return driver


def inject_local_storage(driver, local_storage_items):
    for key, value in local_storage_items.items():
        driver.execute_script("window.localStorage.setItem(arguments[0], arguments[1]);", key, value)


def navigate_and_act(driver, xpath_action_pairs):
    for xpath, action in xpath_action_pairs.items():
        try:
            element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            # Check if the action is to click the element
            if action is None:
                element.click()  # Use Selenium's native click
            # Otherwise, check if the action includes sending keys
            elif isinstance(action, dict) and "send_keys" in action:
                time.sleep(1)
                element.send_keys(action["send_keys"])
                time.sleep(1)
        except:# (StaleElementReferenceException, ElementClickInterceptedException, TimeoutException) as e:
            # Fallback to JavaScript click if Selenium's click fails
            print("Falling back to JavaScript click")
            driver.execute_script("arguments[0].click();", element)

def create_new_group(driver, group_name):
    for xpath in BUTTON_XPATHS:
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
            )
        driver.execute_script("arguments[0].click();", button)
    navigate_and_act(driver, {GROUP_NAME_XPATH: {"send_keys": group_name}})
    
    # Click create group button
    navigate_and_act(driver, {GROUP_CREATION_BUTTON_XPATH: None})

    driver.refresh()



def init_driver():
    # Initialize driver
    driver = setup_driver(CHROME_DRIVER_PATH, CHROME_FOR_TEST_PATH)
    driver.get(TELEGRAM_WEB_URL)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
    
    # Inject local storage items
    inject_local_storage(driver, LOCAL_STORAGE_ITEMS)
    time.sleep(1)
    driver.refresh()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
    return driver


# Main
def main():
    try:
        driver = init_driver()

        # Click buttons to create new group
        create_new_group(driver, TELEGRAM_GROUP_NAME)

        # Click on the first discussion which is supposed to be the newly created group
        navigate_and_act(driver, {FIRST_DISCUSSION_XPATH: None})

        # Open group settings
        navigate_and_act(driver, {GROUP_SETTINGS_XPATH: None})

        # Add members button
        navigate_and_act(driver, {ADD_MEMBER_XPATH: None})

        # Search for a contact
        navigate_and_act(driver, {SEARCH_FIELD_XPATH: {"send_keys": "@delugebuybot"}})

        # Click on (+) button
        navigate_and_act(driver, {SELECT_FIRST_DISCUSSION_XPATH: None})

        # Click on Add button
        navigate_and_act(driver, {ADD_BUTTON_XPATH: None})

        # Close group settings
        navigate_and_act(driver, {GROUP_SETTINGS_XPATH: None})

        # Send a message to setup the group
        navigate_and_act(driver, {MESSAGE_FIELD_XPATH: {"send_keys":"/settings"}})
        navigate_and_act(driver, {MESSAGE_FIELD_XPATH: {"send_keys": u'\ue007'}})
        
        print("Operation done successfully!")
    
    finally:
        driver.quit()

main()  # Uncomment to run
