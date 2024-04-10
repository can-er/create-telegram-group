# Telegram Group Automation Script

This Python script automates the process of creating a new group on Telegram Web, adding members to it, and setting up initial configurations using Selenium WebDriver for automation.

## Features

- Automated group creation on Telegram Web.
- Adds specified members to the newly created group.
- Configures the group by sending initial setup commands.

## Requirements

- Python 3.x
- Selenium WebDriver
- ChromeDriver (compatible with your Chrome version)
- Google Chrome or any Chromium-based browser
- Google Chrome for Tests (if you're a version of Chrome  above 115)

## Setup Instructions

1. **Install Python Dependencies**

   Ensure you have Python installed on your system. Then, install the required Python packages using pip:

   ```sh
   pip install selenium
   ```

2. **ChromeDriver**

   Download ChromeDriver from [the official site](https://sites.google.com/a/chromium.org/chromedriver/) that matches your Chrome browser's version. Extract and place `chromedriver` in your project directory or any preferred directory.

3. **Configure Script**

   - Update the `CHROME_DRIVER_PATH` variable in the script to the path where you've placed ChromeDriver.
   - Update `CHROME_FOR_TEST_PATH` to the path of your Chrome or Chromium-based browser executable.
   - Set `TELEGRAM_WEB_URL` to the URL of Telegram Web (default is set).
   - Customize `TELEGRAM_GROUP_NAME` to the name of the group you wish to create.
   - Ensure `LOCAL_STORAGE_ITEMS` contains the necessary authentication and configuration items for your Telegram account.

4. **Local Storage Items**

   You need to manually obtain the local storage items for authentication from your browser:
   - Login to Telegram Web in your browser.
   - Open the Developer Tools (F12 or Ctrl+Shift+I).
   - Go to the Application tab, and under the Local Storage section, copy the necessary items as shown in the script.

## Usage

To run the script, navigate to your project directory in the terminal and execute the Python script:

```sh
python3 main.py
```

## Additional Notes

- The script assumes that you have already authenticated with Telegram Web, and your local storage items are valid.
- Due to the dynamic nature of web pages, XPaths and other selectors might need updates based on changes to the Telegram Web UI.
- Always use a test account to avoid any unintended consequences on your primary Telegram account.
