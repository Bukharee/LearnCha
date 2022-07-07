from django.shortcuts import render
import requests
from .forms import SearchForm
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.


def get_audio(data):
    audio = None
    for sound in data:
        if sound["audio"] != '':
            audio = sound["audio"]
            return audio
    return audio


def structure_word(response):
    """
    Input: Json Response From Open Dictionary Api -Guaranteed an array of objects.
    Output: Python Dictionary Contains Word, Its Meaning, Pronounciation, Phonetics,
    Examples, Synonyms and Antonyms
    """
    result = {"pronounciation": [],
              }  # final  dictionary containing every thing
    # contains part of spech, definations and all will be extracted to our results array
    meanings = []
    phonetics = []
    for dictionary in response:
        # only assign word to result dict if it doesn't already exist
        result.setdefault("word", dictionary["word"])

        # only assign phonetic to result dict if it doesn't already exist
        result.setdefault("phonetic", dictionary["phonetic"])

        for meaning in dictionary["meanings"]:
            meanings.append(meaning)

        for phonetic in dictionary["phonetics"]:
            phonetics.append(phonetic)

    result["pronounciation"] = get_audio(phonetics)
    result["meanings"] = meanings
    return result


def search(request):
    """
    example = response[3][1][5][3]
    """
    dictionary_url = "https://api.dictionaryapi.dev/api/v2/entries/en/"
    form = SearchForm()
    query = request.GET.get('query')
    if query:
        try:
            response = requests.get(f"{dictionary_url}{query}").json()
            structure_word(response)
            if "title" in response:
                return render(request, 'search.html', {"response": "NOT A VALID WORD", "form": form})
            data = structure_word(response)
            return render(request, "search.html", {"response": response, "data": data, "form": form})
        except Exception as e:
            return render(request, "search.html", {"response": "No Internet Connection", "form": form})
    else:
        return render(request, "search.html", {"form": form})


def d_game(request):
    return render(request, "d_game.html")


def d_game2(request):
    return render(request, "d_game2.html")


def d_game3(request):
    return render(request, "one-word-four-pictures.html")


def game_list(request):
    return render(request, "games.html")


@api_view(["GET"])
def dictionary_search_api(request):
    dictionary_url = "https://api.dictionaryapi.dev/api/v2/entries/en/"
    query = request.GET.get('query')
    if query:
        try:
            response = requests.get(f"{dictionary_url}{query}").json()
            if "title" in response:
                return Response({"response": "NOT A VALID WORD"})
            data = structure_word(response)
            return Response({"data": data})
        except Exception as e:
            return Response({"response": "Something went wrong"})
    else:
        return Response({"message": "you did'nt pass any search word"}, status=400)
