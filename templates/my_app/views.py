from django.shortcuts import render

def home1(request):
     return render(request , 'home.html')
def new_search(request):
         return render(request , 'my_app/new_search.html')
