from django.shortcuts import render

ICE_CREAM = chr(127846)


def ice_cream_detail(request, pk):
    templates_detail = 'ice_cream/detail.html'
    return render(request, templates_detail)


def ice_cream_list(request):
    templates_list = 'ice_cream/list.html'
    return render(request, templates_list)