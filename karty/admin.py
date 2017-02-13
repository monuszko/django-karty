from django.contrib import admin

from .models import MenuCard, Dish


class DishInline(admin.TabularInline):
    model = Dish
    extra = 3


class MenuCardAdmin(admin.ModelAdmin):
    inlines = [DishInline]


admin.site.register(MenuCard, MenuCardAdmin)
