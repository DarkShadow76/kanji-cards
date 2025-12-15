import requests
import random
from typing import List, Dict, Tuple, Union, Any


class KanjiAPI:
    def __init__(self, level_k: Union[int, List[str]] = 0) -> None:
        self.base_url: str = "https://kanjiapi.dev/v1/kanji/"
        self.kanji_list: List[str] = []

        if level_k == 0:
            level_k = random.randint(1,6)

        if isinstance(level_k, int):
            self.level: int = level_k
            kanji_list, error = self.get_kanji_list(self.level)
            if error:
                print(error)  # Or handle it more gracefully
                self.kanji_list = []
            else:
                self.kanji_list = kanji_list if kanji_list else []
        else:
            self.kanji_list = level_k
            random.shuffle(self.kanji_list)

    def get_kanji_list(self, level: int) -> Tuple[List[str], None] | Tuple[None, str]:
        try:
            url: str = f"{self.base_url}grade-{level}"
            response = requests.get(url)

            if response.status_code == 200:
                kanji_list: List[str] = response.json()
                random.shuffle(kanji_list)
                return kanji_list, None
            else:
                return None, f"Cannot Get Kanji List. Status code: {response.status_code}"
        except Exception as e:
            return None, f"Error getting kanji list: {e}"

    def get_random_kanji(self) -> str | None:
        if not self.kanji_list:
            return None

        random_kanji: str = self.kanji_list.pop()
        return random_kanji

    def get_kanji_info(self, kanji_char: str) -> Tuple[Dict[str, Any], None] | Tuple[None, str]:
        try:
            url: str = f"{self.base_url}{kanji_char}"
            response = requests.get(url)
            if response.status_code == 200:
                info_kanji: Dict[str, Any] = response.json()
                return info_kanji, None
            else:
                return None, f"Cannot get kanji info. Status code: {response.status_code}"
        except Exception as e:
            return None, f"Error Getting kanji: {e}"


if __name__ == "__main__":
    kanjiApi = KanjiAPI(1)
    if kanjiApi.kanji_list:
        for i in range(4):
            kanji = kanjiApi.get_random_kanji()
            # print(kanji, end='  ')

    # print()
    # print(kanjiApi.kanji_list)
