from django.contrib import admin
from django.forms import Textarea, TextInput
from django.db import models

from .models import MenuCard, Dish


class DishInline(admin.TabularInline):
    model = Dish
    extra = 3
    formfield_overrides = {
            models.TextField: {'widget': Textarea(attrs={'cols': 15, 'rows': 3})},
            models.CharField: {'widget': TextInput(attrs={'size': 10})},
            }


class MenuCardAdmin(admin.ModelAdmin):
    list_display = ('name', 'pub_date', 'mod_date')
    readonly_fields = ('pub_date', 'mod_date')
    inlines = [DishInline]


admin.site.register(MenuCard, MenuCardAdmin)
