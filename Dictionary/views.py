from django.shortcuts import render
import os
import requests
from .forms import SearchForm
# Create your views here.


def search(request):
    dictionary_url = "https://api.dictionaryapi.dev/api/v2/entries/en/"
    form = SearchForm()
    query = request.GET.get('query')
    if query:
        try:
            response = requests.get(f"{dictionary_url}{query}").json()
            print(response)
            print(response[0]["meanings"][0]["definitions"][0]["definition"])
            if "title" in response:
                return render(request, 'search.html', {"response": "NOT A VALID WORD", "form": form})
            data = {"word": response[0]["word"],
                    "phonetic": response[0]["phonetic"],
                    "meaning": response[0]["meanings"][0]["definitions"][0]["definition"],
                    "audio": response[0]['phonetics'][0]['audio']
                    }
            print(data["word"])
            return render(request, "search.html", {"response": response, "data": data, "form": form})
        except:
            return render(request, "search.html", {"response": "No Internet Connection", "form": form})
    else:
        return render(request, "search.html", {"form": form})


def d_game(request):
    return render(request, "d_game.html")


def d_game2(request):
    return render(request, "d_game2.html")


def game_list(request):
    return render(request, "games_list.html")
