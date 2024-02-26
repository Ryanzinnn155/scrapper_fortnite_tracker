from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
from time import sleep
import json


class Scraper:
    def __init__(self):
        self.driver = Chrome()

    def html_page(self, url_base):
        self.driver.get(url_base)
        html = self.driver.page_source
        html = BeautifulSoup(html, 'html.parser')
        return html

    def player_table(self, total_pages):
        player_data_list = []

        for page_num in range(0, total_pages + 1):
            page = f'https://fortnitetracker.com/events/epicgames_S28_DuosCashCup_BR?window=S28_DuosCashCup_Event5Round1_BR&page={page_num}'
            html = self.html_page(page)
            players = html.select('tr.trn-table__row')

            for i, player in enumerate(players):
                if i == 0:
                    continue
                player_data = [data.strip() for data in player.stripped_strings]
                player_dict = {
                    "Rank": player_data[0],
                    "Player": player_data[1],
                    "Points": player_data[2],
                    "Matches": player_data[3],
                    "Wins": player_data[4],
                    "Avg Elims": player_data[5],
                    "Avg Place": player_data[6]
                }
                player_data_list.append(player_dict)
            sleep(3)

        return player_data_list


tracker = Scraper()
data = tracker.player_table(2)
print(json.dumps(data, indent=4))
