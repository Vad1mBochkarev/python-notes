from django.shortcuts import render


def description(request):
    templates_about = 'about/description.html'
    return render(request, templates_about)