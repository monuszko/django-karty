from django.db.models import Count
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from rest_framework.filters import OrderingFilter
from rest_framework import generics

from .models import MenuCard
from .serializers import MenuCardSerializer


class MenuCardList(ListView):
    queryset = MenuCard.public.all()
    template_name = 'karty/menucard_list.html'

    def get_context_data(self, **kwargs):
        context = super(MenuCardList, self).get_context_data(**kwargs)

        paginator = Paginator(self.get_queryset(), 10)
        pagenr = self.request.GET.get('page')
        try:
            page = paginator.page(pagenr)
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)

        context['page'] = page
        # '?' technically not a part of querystring, saves one 'if' in template

        prev_qstring = ''
        if page.has_previous():
            prev_qstring = self.request.GET.copy()
            prev_qstring['page'] = page.previous_page_number()
            prev_qstring = '?' + prev_qstring.urlencode()

        next_qstring = ''
        if page.has_next():
            next_qstring = self.request.GET.copy()
            next_qstring['page'] = page.next_page_number()
            next_qstring = '?' + next_qstring.urlencode()

        context['prev_qstring'] = prev_qstring
        context['next_qstring'] = next_qstring
        return context


    def get_queryset(self, **kwargs):
        qs = self.queryset
        ordering = self.request.GET.get('ordering')
        if ordering in ('name' ,'num_dishes'):
            qs = qs.order_by(ordering)
        return qs



class MenuCardDetail(DetailView):
    queryset = MenuCard.public.all()
    template_name = 'karty/menucard_detail.html'
    template_object_name='menucard'


class APIMenuCardList(generics.ListAPIView):
    queryset = MenuCard.public.all()
    serializer_class = MenuCardSerializer
    filter_backends = (OrderingFilter,)
    ordering_fields = ('pk', 'name', 'num_dishes')
    ordering = ('pk',)


class APIMenuCardDetail(generics.RetrieveAPIView):
    queryset = MenuCard.public.all()
    serializer_class = MenuCardSerializer

