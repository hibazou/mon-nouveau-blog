from django.shortcuts import render,get_object_or_404
from .models import Citations
from django.http import HttpResponse


def citations_view(request):
    citations = Citations.objects.all()
    context = {'citations': citations}
    return render(request, 'citations.html', context)


def quotes_view(request):
    citations= Citations.objects.all()
    return render(request, 'like.html', {'citations':citations})
    