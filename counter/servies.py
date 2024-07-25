# services.py
import requests
from django.conf import settings

class EdamamAPI:
    BASE_URL = 'https://api.edamam.com/api/food-database/v2'

    @staticmethod
    def search_food(query):
        url = f"{EdamamAPI.BASE_URL}/parser"
        params = {
            'app_id': settings.EDAMAM_APP_ID,
            'app_key': settings.EDAMAM_APP_KEY,
            'ingr': query
        }
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
