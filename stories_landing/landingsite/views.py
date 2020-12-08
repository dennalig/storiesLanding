from django.shortcuts import render
from django.http import HttpResponse

posts = [  
    {
        'author':'Dennali',
        'communityName':'Breaking Bad',
        'content':'content',
        'date_posted':'June 6, 2020'
    },
    {
        'author':'SWUser',
        'communityName':'Star Wars',
        'content':'content',
        'date_posted':'June 4, 2020'
    },
    {

         'author':'InceptionUser',
        'communityName':'Inception',
        'content':'content',
        'date_posted':'June 7, 2020'

    }
]


def home(request):
    context={
        'posts':posts
    }
    return render(request,'landingsite/home.html', context)

def about(request):
    return render(request, 'landingsite/about.html')
# Create your views here.


