import mysql.connector
import warnings
warnings.simplefilter(action='ignore', category=UserWarning)
import pandas as pd

class DatabaseClass():

    def __init__(self) -> None:
        self.db = mysql.connector.connect(host='localhost', user='root', password='necromancer1', db='SteamAPI')
        self.curs = self.db.cursor()

    def insert_data(self, game_id:str , game_name:str ) -> None:
        query = f"""
        INSERT INTO
            steam_games
                (
                    steam_id,
                    name,
                    number_reviews
                )
        VALUES 
            (
                "{game_id}",
                "{game_name}",
                '100'
            )
        """
        self.curs.execute(query)
        self.db.commit()
    
    def get_games(self) -> pd.DataFrame:
        query = """
        SELECT
            *
        FROM
            steam_games
        """
        data = self.curs.execute(query)
        data = self.curs.fetchall()
        print(data)
        return data

    def get_game_data(self, game_id:str) -> pd.DataFrame:
        query = f"""
        SELECT
            *
        FROM
            steam_games
        WHERE 
            steam_id = "{game_id}"
        """
        data = self.curs.execute(query)
        data = self.curs.fetchone()
    

        return data
    
    def get_random_n_games(self, n:int):
        query = f"""
        SELECT
            steam_id
        FROM
            steam_games
        ORDER BY RAND()
        LIMIT {n};
        """
        data = self.curs.execute(query)
        data = self.curs.fetchall()
        data = [x[0] for x in data]
        return data
