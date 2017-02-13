from django.shortcuts import render, get_object_or_404

from .models import MenuCard


def menucard_list(request):
    card_list = MenuCard.objects.all()
    return render(request, 'karty/menucard_list.html', {'menucard_list': card_list})


def menucard_detail(request, menucard_id):
    menucard = get_object_or_404(MenuCard, pk=menucard_id)
    return render(request, 'karty/menucard_detail', {'menucard': menucard})
