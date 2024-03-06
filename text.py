import unittest
import requests

class TestWebsiteLoad(unittest.TestCase):
    def test_website_load(self):
        url = "https://atg.world"
        print("Connecting to", url)

        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for non-200 status codes
            print("Website loaded successfully!")
        except requests.RequestException as e:
            print("Failed to connect to the website:", e)
            self.fail("Failed to connect to the website")

if __name__ == "__main__":
    unittest.main()
