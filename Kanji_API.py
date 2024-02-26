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
                random.shuffle(kanji_list)
                return kanji_list
            else:
                print("Cannot Get Kanji List")
                return None
        except Exception as e:
            print(f"Error getting kanji list: {e}")
            return None

    def get_random_kanji(self):
        if not self.kanji_list:
            print("Kanji list is empty")
            return None

        random_kanji = self.kanji_list.pop()
        print(self.kanji_list)
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


if __name__ == "__main__":
    kanjiApi = KanjiAPI(1)
    for i in range(4):
        kanji = kanjiApi.get_random_kanji()
        print(kanji)

    print("\n")
    print(kanjiApi.kanji_list)
