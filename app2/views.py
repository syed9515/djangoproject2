from django.http import HttpResponse

from django.shortcuts import render

def Company_p(request):
    return render(request,"practicecompany.html")