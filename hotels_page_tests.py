from phpTravelsTests import *

class HotelsPage(TestCase):

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
        self.chrome.find_element(By.LINK_TEXT, 'Hotels').click()
        sleep(2)

    def tearDown(self):
        self.chrome.quit()

    def test_title(self):
        actual = self.chrome.find_element(By.XPATH, '//h2[normalize-space()="SEARCH FOR BEST HOTELS"]').text
        expected = 'SEARCH FOR BEST HOTELS'
        actual2 = self.chrome.find_element(By.XPATH, '//h2[normalize-space()="SEARCH FOR BEST HOTELS"]').is_displayed()
        expected2 = True
        self.assertEqual(expected, actual, f'Text is incorrect, text should be: {actual}')
        self.assertEqual(expected2, actual2, f'Text is not displayed')

    def test_sub_title(self):
        actual = self.chrome.find_element(By.XPATH, '//h2[normalize-space()="Featured Hotels"]').text
        expected = 'Featured Hotels'
        self.assertEqual(expected, actual)

    def test_search_hotel(self):
        self.chrome.find_element(By.XPATH, '//span[@role="combobox"]').click()
        sleep(2)
        self.chrome.find_element(By.XPATH, '//input[@role="searchbox"]').send_keys('Paris')
        sleep(7) # => longer sleep for site to have enough time to find our destination
        self.chrome.find_element(By.XPATH, '//span[@role="combobox"]').send_keys(Keys.ENTER)
        self.chrome.find_element(By.XPATH, '//a[@class="dropdown-toggle dropdown-btn travellers waves-effect"]').click()
        self.chrome.find_element(By.XPATH, '//div[@class="roomInc"]//i[@class="la la-plus"]').click()
        self.chrome.find_element(By.XPATH, '//button[@id="submit"]').click()
        sleep(5)
        actual = self.chrome.current_url
        expected = 'https://phptravels.net/hotels/en/usd/paris/12-02-2023/13-02-2023/2/2/0/RO'
        self.assertEqual(expected, actual)