from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, get_user
from .models import Users
import requests
import os
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join('.env')
load_dotenv(dotenv_path)
# Create your views here.

def oauth2(request):
    return redirect(os.environ.get('DISCORD_AUTH_URL'))

def oauth2DiscordCheck(request):
    code = request.GET.get('code')
    try:
        user = exchange_code(code)
    except KeyError:
        return render(request, 'error.html')
    auth = authenticate(request,user=user)
    print(auth)
    if auth != None:
        access = Users.objects.values_list('access', flat=True).filter(discord_id=user['id']) 
        for access in access:
            auth = list(auth).pop()
            login(request, auth)
            render(request, 'completed.html', {'access':access})
            return redirect('http://127.0.0.1:8000/morphydb')
        
    else: return render(request, 'error.html')

def exchange_code(code: str):
    data = {
        'client_id': os.environ.get('DISCORD_CLIENT_ID'),
        'client_secret' : os.environ.get('DISCORD_CLIENT_SECRET'),
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': 'http://127.0.0.1:8000/oauth2/check',
        'scope': 'identify guilds'
    }

    headers = {
        'Content-Type' : 'application/x-www-form-urlencoded'
    }

    response = requests.post('https://discord.com/api/oauth2/token', data=data, headers=headers)
    credentials = response.json()
    access_token = credentials['access_token']
    response = requests.get('https://discord.com/api/v6/users/@me', headers= {
        'Authorization' : 'Bearer %s' % access_token
    })
    user = response.json()
    return user