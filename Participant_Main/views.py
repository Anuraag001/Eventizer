from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def participant_main(request):
    return render(request,'par_index.html')