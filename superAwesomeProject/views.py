from django.http import HttpResponse
from django.shortcuts import render

data = {
    'superAwesomeProject': [
        {
            'id': 5,
            'title': 'RoboCop',
            'year': '1987'
        },
        {
            'id': 6,
            'title': 'VampireDog',
            'year': '1998'
        },
        {
            'id': 7,
            'title': 'CoboRop',
            'year': '2019'
        }
    ]
}

def superAwesomeProject(request):
    return render(request, 
                  'superAwesomeProject/superAwesomeProject.html',
                  data)

def home(request):
    return HttpResponse('Home page')