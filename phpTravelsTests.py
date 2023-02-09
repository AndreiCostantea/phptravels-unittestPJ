from unittest import TestCase
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class Tests(TestCase):
    HOTELS_BTN = (By.XPATH, '//button[@id="hotels-tab"]')
    FLIGHTS_BTN = (By.XPATH, '//button[@id="flights-tab"]')
    TOURS_BTN = (By.XPATH, '//button[@id="tours-tab"]')
    TRANSFERS_BTN = (By.XPATH, '//button[@id="cars-tab"]')
    VISA_BTN = (By.XPATH, '//button[@id="visa-tab"]')

    def setUp(self):
        self.chrome = webdriver.Chrome
        self.chrome = webdriver.Chrome(ChromeDriverManager().install())
        self.chrome.get('https://phptravels.net/')
        self.chrome.maximize_window()
        sleep(0.5)
        # => the default language for the site is turkish so we are going to change it to english
        self.chrome.find_element(By.XPATH, '//button[@id="languages"]').click()
        self.chrome.find_element(By.XPATH, '//a[normalize-space()="English"]').click()
        sleep(2)

    def tearDown(self):
        self.chrome.quit()

    def test_url(self):
        actual = self.chrome.current_url
        expected = 'https://phptravels.net/'
        self.assertEqual(expected, actual, 'URL incorrect')

    def test_title(self):
        actual = self.chrome.find_element(By.XPATH, '//strong[contains(text(),"Let’s book your next trip!")]').text
        expected = 'Let’s book your next trip!'
        self.assertEqual(expected, actual, 'Incorrect title')

    def test_sub_title(self):
        actual = self.chrome.find_element(By.XPATH, '//p[normalize-space()="Choose best deals over 1.5 million travel services"]').text
        expected = 'Choose best deals over 1.5 million travel services'
        self.assertEqual(expected, actual, 'Incorrect sub title')

    def test_Hotels_Btn(self):
        actual = self.chrome.find_element(*self.HOTELS_BTN).text
        expected = 'Hotels'
        self.assertEqual(expected, actual)

    def test_Flights_Btn(self):
        actual = self.chrome.find_element(*self.FLIGHTS_BTN).text
        expected = 'Flights'
        self.assertEqual(expected, actual)

    def test_Tours_Btn(self):
        actual = self.chrome.find_element(*self.TOURS_BTN).text
        expected = 'Tours'
        self.assertEqual(expected, actual)

    def test_Transfers_Btn(self):
        actual = self.chrome.find_element(*self.TRANSFERS_BTN).text
        expected = 'Transfers'
        self.assertEqual(expected, actual)

    def test_Visa_Btn(self):
        actual = self.chrome.find_element(*self.VISA_BTN).text
        expected = 'Visa'
        self.assertEqual(expected, actual)

    def test_TopFlightDestinations(self):
        self.chrome.execute_script("window.scrollTo(0, 750)")
        sleep(5)
        actual = self.chrome.find_element(By.XPATH, '//h2[normalize-space()="Top Flight Destinations"]').text
        expected = 'Top Flight Destinations'
        actual2 = self.chrome.find_element(By.XPATH, '//h2[normalize-space()="Top Flight Destinations"]').is_displayed()
        expected2 = True
        self.assertEqual(expected, actual)
        self.assertEqual(expected2, actual2)

    def test_search_flight(self):
        self.chrome.find_element(*self.FLIGHTS_BTN).click()
        self.chrome.find_element(By.XPATH, '//input[@id="autocomplete"]').send_keys('Cluj')
        sleep(0.5)
        self.chrome.find_element(By.XPATH, '//input[@id="autocomplete"]').send_keys(Keys.ARROW_DOWN)
        self.chrome.find_element(By.XPATH, '//input[@id="autocomplete"]').send_keys(Keys.ENTER)
        sleep(0.5)
        self.chrome.find_element(By.ID, 'autocomplete2').send_keys('Barcelona')
        sleep(0.5)
        self.chrome.find_element(By.ID, 'autocomplete2').send_keys(Keys.ARROW_DOWN)
        self.chrome.find_element(By.ID, 'autocomplete2').send_keys(Keys.ENTER)
        sleep(0.5)
        self.chrome.find_element(By.XPATH, '//a[@class="dropdown-toggle dropdown-btn waves-effect"]').click()
        sleep(0.5)
        self.chrome.find_element(By.XPATH, '//div[@class="dropdown-item adult_qty"]//div[@class="qtyInc"]').click()
        sleep(3)
        self.chrome.find_element(By.XPATH, '//button[@id="flights-search"]').click()
        sleep(2)
        actual = self.chrome.current_url
        expected = 'https://phptravels.net/flights/en/usd/clj/bcn/oneway/economy/12-02-2023/2/0/0'
        self.assertEqual(expected, actual)

    def test_flight_page(self):
        self.chrome.find_element(By.LINK_TEXT, 'Flights').click()
        actual = self.chrome.current_url
        expected = 'https://phptravels.net/flights'
        self.assertEqual(expected, actual, 'Wrong URL')

    def test_tours_page(self):
        self.chrome.find_element(By.LINK_TEXT, 'Tours').click()
        actual = self.chrome.current_url
        expected = 'https://phptravels.net/tours'
        self.assertEqual(expected, actual, 'Wrong URL')

    def test_transfers_page(self):
        self.chrome.find_element(By.LINK_TEXT, 'Transfers').click()
        actual = self.chrome.current_url
        expected = 'https://phptravels.net/cars'
        self.assertEqual(expected, actual, 'Wrong URL')

    def test_visa_page(self):
        self.chrome.find_element(By.LINK_TEXT, 'Visa').click()
        actual = self.chrome.current_url
        expected = 'https://phptravels.net/visa'
        self.assertEqual(expected, actual, 'Wrong URL')

    def test_offers_page(self):
        self.chrome.find_element(By.LINK_TEXT, 'Offers').click()
        actual = self.chrome.current_url
        expected = 'https://phptravels.net/offers'
        self.assertEqual(expected, actual, 'Wrong URL')

    def test_company_page(self):
        self.chrome.find_element(By.LINK_TEXT, 'Company').click()
        actual = self.chrome.current_url
        expected = 'https://phptravels.net/company'
        self.assertEqual(expected, actual, 'Wrong URL')

