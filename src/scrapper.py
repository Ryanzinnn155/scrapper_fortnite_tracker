from selenium.webdriver import Chrome
from bs4 import BeautifulSoup


class Scrapper:
    def __init__(self):
        self.session = Chrome()

    def close_session(self):
        self.session.close()

    def html_page(self, url_base):
        self.session.get(url_base)
        html = self.session.page_source
        html = BeautifulSoup(html, 'html.parser')
        return html

    def player_table(self, total_pages, url_site):
        '''
        Function responsible for collecting data from each player in the table and manipulating
        :param total_pages: Parameter that defines which page the Scrapper will go to
        :param url_site: Parameter that defines the Url of the Championship and session in which the data will be collected
        :return: Returns table data formatted in dict
        '''
        player_data_list = []

        for page_num in range(0, total_pages + 1):
            page = f'{url_site}&page={page_num}'
            html = self.html_page(page)
            players = html.select('tr.trn-table__row')

            for i, player in enumerate(players):
                if i == 0:
                    continue
                player_data = [data.strip() for data in player.stripped_strings]
                rank = player_data[0]
                player = player_data[1]
                team_player = player_data[2] if len(player_data[2]) > 4 else None
                points = player_data[2] if team_player is None else player_data[3]
                matches = player_data[4] if points is player_data[3] else player_data[3]
                wins = player_data[4] if matches not in player_data[4] else player_data[5]
                avg_elims = player_data[6] if wins is player_data[5] else player_data[5]
                avg_place = player_data[7] if avg_elims is player_data[6] else player_data[6]
                player_dict = {
                    "Rank": int(rank),
                    "Player": player,
                    "Team": team_player,
                    "Points": int(points),
                    "Matches": int(matches),
                    "Wins": int(wins),
                    "Avg Elims": float(avg_elims),
                    "Avg Place": float(avg_place)
                }
                player_data_list.append(player_dict)
            return player_data_list
