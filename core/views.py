from django.shortcuts import render
import requests
API_KEY = 'SUA_KEY'


def home(request):
    """
    https://docs.thedogapi.com/api-reference/breeds/breeds-list
    :param request:
    :return:
    """
    payload = {}
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': API_KEY
    }

    q = request.GET.get('name')
    if q:
        url = f'https://api.thecatapi.com/v1/breeds/search?q={q}'
        response = requests.request('GET', url, headers=headers, data=payload)
        data = response.json()
    else:
        url = 'https://api.thecatapi.com/v1/breeds'
        response = requests.request('GET', url, headers=headers, data=payload)
        data = response.json()

    context = {'content': data}
    return render(request, 'home.html', context)

