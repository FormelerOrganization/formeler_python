import requests
import json

DEFAULT_BASE_URL = "https://formeler.com/api"
API_VERSION = "2025-11-12"


class LangID:
    def __init__(self, api_key, base_url=DEFAULT_BASE_URL):
        self.api_key = api_key
        self.base_url = base_url

    def detect(self, text):
        post_data = json.dumps({"text": text})
        response = requests.post("{}/{}/{}".format(self.base_url, API_VERSION, "langid/detect"), data=post_data,
                                 headers={"Content-Type": "application/json", "Authorization": self.api_key})
        return response.json()

    def batch_detect(self, texts):
        post_data = json.dumps({"texts": texts})
        response = requests.post("{}/{}/{}".format(self.base_url, API_VERSION, "langid/batch-detect"), data=post_data,
                                 headers={"Content-Type": "application/json", "Authorization": self.api_key})
        return response.json()


class Formeler:
    def __init__(self, api_key, base_url=DEFAULT_BASE_URL):
        self.api_key = api_key
        self.base_url = base_url
        self.lang_id = LangID(api_key, base_url)
