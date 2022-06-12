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
            return render(request, "search.html", {"response": response, "form": form})
        except:
            return render(request, "search.html", {"response": "No Internet Connection", "form": form})
    else:
        return render(request, "search.html", {"form": form})


# def search_offline():
#     dictionary_url = "https://api.dictionaryapi.dev/api/v2/entries/en/"
#     word = requests.args.get("word")
#     print(f"{dictionary_url}{word}")
#     response = requests.get(f"{dictionary_url}{word}").json()
#     if "title" in response:
#         return "Not a Valid Word"
#     return str(response[0]["meanings"][0]["definitions"][0]["definition"])


# def ussd():
#   # Read the variables sent via POST from our API
#   session_id   = request.values.get("sessionId", None)
#   serviceCode  = request.values.get("serviceCode", None)
#   phone_number = request.values.get("phoneNumber", None)
#   text         = request.values.get("text", "default")

#   """"
#   -first dial
#   -if registered
#         -play a game
#         - dictionary
#         -topics
#         -quiz
#   -else
#       redirect to register
#   """
#   database = {}
#   if phone_number in database:
#       if text      == '':
#           # This is the first request. Note how we start the response with CON
#           response  = "Welcome to Learncha!!  \n"
#           response += "1. Play a Game \n"
#           response += "2. Dictionary\n"
#           response += "3. Topics\n"
#           response += "4. Quiz"
#       elif text    == '1':
#           # Business logic for first level response
#           response  = "CON Choose account information you want to view \n"
#           response += "1. Account number"

#       elif text   == '2':
#           # This is a terminal request. Note how we start the response with END
#           dictionary_url = "https://api.dictionaryapi.dev/api/v2/entries/en/"
#           word = request.args.get("word")
#           print(f"{dictionary_url}{word}")
#           response = requests.get(f"{dictionary_url}{word}").json()
#           if "title" in response:
#               return "Not a Valid Word"
#           return str(response[0]["meanings"][0]["definitions"][0]["definition"])
#           response = "CON Enter A Word "


#       elif text == '1*1':
#           # This is a second level response where the user selected 1 in the first instance
#           accountNumber  = "ACC1001"
#           # This is a terminal request. Note how we start the response with END
#           response       = "END Your account number is " + accountNumber

#       else :
#           response = "END Invalid choice"

#   else:
#     pass
#     #register user here


#   # Send the response back to the API
#   return response
