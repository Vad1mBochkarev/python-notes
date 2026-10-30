from django.shortcuts import render

# Импортируем класс BirthdayForm, чтобы создать экземпляр формы.
from .forms import BirthdayForm


def birthday(request):

    if request.GET:
        form = BirthdayForm(request.GET)

        if form.is_valid():
            pass
        else:
            form = BirthdayForm()
    # Создаём экземпляр класса формы.
    form = BirthdayForm()
    # Добавляем его в словарь контекста под ключом form:
    context = {'form': form}
    # Указываем нужный шаблон и передаём в него словарь контекста.
    return render(request, 'birthday/birthday.html', context)
