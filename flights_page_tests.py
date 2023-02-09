from phpTravelsTests import *

class FlightsPage(TestCase):

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
        # => flights page
        self.chrome.find_element(By.LINK_TEXT, 'Flights').click()
        sleep(2)

    def tearDown(self):
        self.chrome.quit()

    def test_title(self):
        actual = self.chrome.find_element(By.XPATH, '//h2[normalize-space()="SEARCH FOR BEST FLIGHTS"]').text
        expected = 'SEARCH FOR BEST FLIGHTS'
        actual2 = self.chrome.find_element(By.XPATH, '//h2[normalize-space()="SEARCH FOR BEST FLIGHTS"]').is_displayed()
        expected2 = True
        self.assertEqual(expected, actual, f'Text is incorrect, text should be: {actual}')
        self.assertEqual(expected2, actual2, f'Text is not displayed')

    def test_sub_title(self):
        actual = self.chrome.find_element(By.XPATH, '//h2[normalize-space()="Top Flight Destinations"]').text
        expected = 'Top Flight Destinations'
        self.assertEqual(expected, actual)