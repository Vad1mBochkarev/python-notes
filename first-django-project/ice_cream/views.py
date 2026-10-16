from django.shortcuts import get_object_or_404, render

from .models import IceCream


def ice_cream_detail(request, pk):
    template = 'ice_cream/detail.html'
    ice_cream = get_object_or_404(IceCream, pk=pk)
    context = {'ice_cream': ice_cream}
    return render(request, template, context)


def ice_cream_list(request):
    template = 'ice_cream/list.html'
    ice_creams = IceCream.objects.filter(is_published=True)
    context = {'ice_creams': ice_creams}
    return render(request, template, context)