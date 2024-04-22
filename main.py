from src.scrapper import Scrapper
from src.opensearch import send_data_to_opensearch


if __name__ == '__main__':
    scrapper = Scrapper()
    contents = scrapper.player_table(3, 'https://fortnitetracker.com/events/epicgames_S29_PlaystationCupMarch_BR?window=S29_PlaystationCupMarch_Final_BR')
    scrapper.close_session()
    print(contents)
    for player in contents:
        pass
        test = send_data_to_opensearch(player)
        print(test)
