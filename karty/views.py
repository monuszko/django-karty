from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import MenuCard


def menucard_list(request):
    sort_by = request.GET.get('sort_by')
    sort_by = sort_by if sort_by in ('name', 'num_dishes') else 'pk'

    card_list = MenuCard.objects.annotate(num_dishes=Count('dish'))
    card_list = card_list.exclude(num_dishes=0).order_by(sort_by)

    paginator = Paginator(card_list, 10)
    page = request.GET.get('page')
    try:
        menucards = paginator.page(page)
    except PageNotAnInteger:
        menucards = paginator.page(1)
    except EmptyPage:
        menucards = paginator.page(paginator.num_pages)

    return render(request, 'karty/menucard_list.html', {'menucards': menucards})


def menucard_detail(request, menucard_id):
    menucard = get_object_or_404(MenuCard, pk=menucard_id)
    return render(request, 'karty/menucard_detail', {'menucard': menucard})
