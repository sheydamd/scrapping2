# Varzesh3 Search Automation with Selenium

This project is a simple Python automation script using Selenium and Microsoft Edge. It opens the [Varzesh3](https://www.varzesh3.com) website, clicks the search icon, and searches for a specific keyword ("بارسلونا").

## Installation

`bash`
- Make venv by using:
    - python -m venv .venv
- active it by using:
    - .venv\scripts\activate
- install selenium by using:
    - pip install selenium

and you should import:
```python
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
```
# Running the Script

Simply run the Python file by using:
`bash`
python main.py
 
 make sure your venv being active

# Script Overview

Launches Microsoft Edge using Selenium

Navigates to varzesh3.com

Clicks the search icon

Enters the keyword "بارسلونا" into the search input

Waits for results to appear

## 🛠 Technical Notes

The script uses time.sleep() for basic waiting; for better control, consider using WebDriverWait.

If elements are not found, the script exits safely to prevent crashes.
