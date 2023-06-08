from django.shortcuts import render
from django.contrib.auth import get_user

# Create your views here.\

def morphydb(request):
    user = get_user(request)
    try:
        access = user.__getattribute__('access')
        if access != '':
            print(access)
            return render(request, 'morphydb.html')
    except AttributeError:
        return render(request, 'error.html', {'error-code': '404', 'error-description': 'Заблудились?'})