import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Ensure GUI is off
        chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
        chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
        self.service = ChromeService()
        self.driver = webdriver.Chrome(service=self.service, options=chrome_options)
        self.driver.get("http://webapp:5000")

    def test_working(self):
        # Find the input text box and submit button
        input_box = self.driver.find_element(By.ID, "search")
        submit_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")

        # Enter text into the input box
        input_box.send_keys("Amazing Grace")

        # Click the submit button
        submit_button.click()

        # Check the result
        result = self.driver.page_source
        self.assertIn("Showing results for: Amazing Grace", result)

    def test_not_working(self):
        # Find the input text box and submit button
        input_box = self.driver.find_element(By.ID, "search")
        submit_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")

        # Enter text into the input box
        input_box.send_keys("<script>alert(1)</script>")

        # Click the submit button
        submit_button.click()

        # Check the result
        result = self.driver.page_source
        self.assertIn("Nice try", result)


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
