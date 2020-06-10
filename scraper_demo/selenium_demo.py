from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)

query = 'lifepo4'
driver.get(f'http://amazon.com/s?k={query}')
for element in driver.find_elements_by_css_selector('div.a-section.a-spacing-medium'):
    try:
        name = element.find_element_by_css_selector('h2 span').text
        price_whole = element.find_element_by_css_selector('span.a-price-whole').text
        price_fraction = element.find_element_by_css_selector('span.a-price-fraction').text
        print(f"\"{name}\",{price_whole}.{price_fraction}")
    except NoSuchElementException:
        pass

driver.close()
