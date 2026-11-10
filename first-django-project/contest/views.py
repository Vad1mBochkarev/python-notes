from django.shortcuts import get_object_or_404, redirect, render

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


def proposal_edit(request, pk):
    instance = get_object_or_404(Contest, pk=pk)
    form = ContestForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request, 'contest/form.html', context)


def proposal_delete(request, pk):
    instance = get_object_or_404(Contest, pk=pk)
    form = ContestForm(instance=instance)
    context = {'form': form}
    if request.method == 'POST':
        instance.delete()
        return redirect('contest:list')
    return render(request, 'contest/form.html', context)


ice_cream_edit = proposal_edit
ice_cream_delete = proposal_delete



ice_cream_edit = proposal_edit
ice_cream_delete = proposal_delete