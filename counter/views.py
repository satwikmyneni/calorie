from django.shortcuts import render
import json
import requests

def home(request):
    if request.method == 'POST':
        query = request.POST['query']
        app_id = '5ba9dd6c'  
        app_key = 'f37e6f686a209f70dec9146fb3cc8f98'  
        api_url = 'https://api.edamam.com/api/nutrition-details'

        # Prepare the payload for POST request
        payload = {
            "ingr": [query]  # Wrap the query in a list
        }

        # Make the API request
        try:
            api_request = requests.post(api_url, params={'app_id': app_id, 'app_key': app_key}, json=payload)
            api_request.raise_for_status()  # Raise an error for bad responses
            api = api_request.json()  # Parse the JSON response
            print(api)  # Log the response for debugging
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            api = {"error": "Failed to retrieve data."}
        except Exception as e:
            print(f"An error occurred: {e}")
            api = {"error": "Oops! There was an error."}
        
        return render(request, 'home.html', {'api': api})
    else:
        return render(request, 'home.html', {'query': 'Enter a valid query'})
