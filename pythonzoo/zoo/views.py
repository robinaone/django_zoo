from django.shortcuts import render

# Create your views here.

def index(request):
    temporaryData = "Bill"
    return render(
    request,
    "index.html",
    context = { 'temporaryData' : temporaryData },
    )
