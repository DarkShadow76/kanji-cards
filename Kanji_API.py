import requests
import random


class KanjiAPI:
    def __init__(self, level_k=random.randint(1, 6)):
        self.base_url = "https://kanjiapi.dev/v1/kanji/"
        self.level = level_k
        self.kanji_list = self.get_kanji_list(self.level)

    def get_kanji_list(self, level):
        try:
            url = f"{self.base_url}grade-{level}"
            response = requests.get(url)

            if response.status_code == 200:
                kanji_list = response.json()
                return kanji_list
            else:
                print("Cannot Get Kanji List")
        except Exception as e:
            print(f"Error getting kanji list: {e}")

    def get_random_kanji(self):
        random_kanji = random.choice(self.kanji_list)
        return random_kanji

    def get_kanji_info(self, kanji_char):
        try:
            url = f"{self.base_url}{kanji_char}"
            response = requests.get(url)
            if response.status_code == 200:
                info_kanji = response.json()

                return info_kanji
            else:
                print("Cannot get kanji info")
        except Exception as e:
            print(f"Error Getting kanji: {e}")
