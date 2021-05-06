from django.shortcuts import render
import requests

API_KEY = '7ea0c9ccc61144eda83999efde87e85d'

def home(request):
    country = request.GET.get('country')
    category = request.GET.get('category')

    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    else:
        url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']

    context ={
        'articles': articles
    }

    return render(request, 'newsapp/home.html', context)

