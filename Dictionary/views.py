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
        response = requests.get(f"{dictionary_url}{query}").json()
        print(response)
        print(response[0]["meanings"][0]["definitions"][0]["definition"])
        if "title" in response:
            return render(request, 'search.html', {"response": "NOT A VALID WORD", "form": form})
        return render(request, "search.html", {"response":response, "form": form})
    else:
        return render(request, "search.html", {"form": form})



