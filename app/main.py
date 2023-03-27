from typing import Union
from api_db import DatabaseClass
from fastapi import FastAPI, Query
from pydantic import BaseModel, EmailStr
import api
import random
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()
database = DatabaseClass()
# Configure CORS middleware
origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/games/{game_id}")
async def get_db_data(game_id: str = ...):
    game = database.get_game_data(game_id)
    return game

@app.get("/games/reviews/{game_id}")
async def get_random_review(game_id:str = ...):
    #TODO: move random game review to GetRequest
    handler = api.GetReview(game_id)# I get only the first 20 items in this list.
    random_review = random.choice(handler.sorted_reviews)
    return {game_id: handler.sorted_reviews}


@app.get("/games/random/reviews/")
async def get_random_reviews(difficulty: Union[int,None] = ...):
    """
    get N random games and generate a bad review for each one, retrieve store data of Name, image, and review for them and mix them up.
    N is related to difficulty.
    """
    game_list = database.get_random_n_games(difficulty)
    games = [api.GameStoreData(game).__dict__ for game in game_list]
    print(json.dumps(games))

    return json.dumps(games)
# redis backend cache 