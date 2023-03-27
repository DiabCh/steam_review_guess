import requests
import json
import urllib.parse
from typing import List
import random

class GetReview():
    def __init__(self, app_id: str) -> None:
        self.app_id =  app_id
        self.reviews = list()
        self._get_review_data()
        self.sorted_reviews = self._sort_review_data()

    def _get_review_data(self, cursor = '*'):

        cursor = urllib.parse.quote(cursor)
        response = requests.get(f'https://store.steampowered.com/appreviews/{self.app_id}?json=1&filter=recent&num_per_page=100&review_type=negative&cursor={cursor}&day_range=365&purchase_type=all')
        data = json.loads(response.text)

        self.reviews.extend(data['reviews']) # data['reviews'] contains all review data
        print('id: ', self.app_id, ' cursor: ', cursor)
        # if data['query_summary']['num_reviews'] == 100: # 100 is max and anything under 100 means there is no next page
        #     self._get_review_data( data['cursor']) # recursive function, repeats action until complete.

    def _sort_review_data(self):

        sorted_reviews = sorted(self.reviews, key=lambda x: float(x['weighted_vote_score']))
        sorted_reviews = [x for x in sorted_reviews if x['weighted_vote_score'] != 0] # ~40% of reviews have no score, i want to filter for the worst scored ones

        return sorted_reviews
        

class GameStoreData():
    def __init__(self, game_id:str ) -> None:
        self.game_id = game_id
        self._get_game_data()
        self._get_worst_review()
        # get "data">"header_image"
        # get "data">"name"


    def _get_game_data(self):
        response = requests.get(f'https://store.steampowered.com/api/appdetails/?json=1&appids={self.game_id}')
        data = json.loads(response.text)[self.game_id]['data']
        self.name = data['name']
        self.desctiption = data['short_description']
        self.header_image = data['header_image']
    
    def _get_worst_review(self):
        handler = GetReview(self.game_id)# I get only the first 20 items in this list.
        random_review = random.choice(handler.sorted_reviews)
        self.review = random_review['review'].strip()
        





        