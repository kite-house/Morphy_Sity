from django.shortcuts import render

# Create your views here.

def error404(request, exception):
    print("мы здесь")
    return render(request, 'error.html', {'error_code' : '404', 'error_description' : 'Заблудились???'})

def error500(request):
    render(request, 'error.html', {'error_code' : '500', 'error_description' : 'Server Error'})