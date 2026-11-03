from django.shortcuts import render

from .forms import ContestForm
from .models import Contest


def proposal(request):
    form = ContestForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request, 'contest/form.html', context)


def proposal_list(request):
    proposals = Contest.objects.order_by('id')
    context = {'proposals': proposals}
    return render(request, 'contest/contest_list.html', context)