from django.contrib import admin

from .models import MenuCard, Dish


class DishInline(admin.TabularInline):
    model = Dish
    extra = 3


class MenuCardAdmin(admin.ModelAdmin):
    list_display = ('name', 'pub_date', 'mod_date')
    readonly_fields = ('pub_date', 'mod_date')
    inlines = [DishInline]


admin.site.register(MenuCard, MenuCardAdmin)
