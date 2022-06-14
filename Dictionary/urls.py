from django.urls import path
from .views import search, d_game, game_list, d_game2

app_name = "dictionary"

urlpatterns = [path('', search, name="search"),
               path('d_game', d_game, name="d_game"),
               path('games', game_list, name="games"),
               path('d_game2', d_game2, name="d_game2")
               ]
