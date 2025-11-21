from django.contrib import admin
from .models import Category, Country, Material, Mint, Coin, Banknote

admin.site.empty_value_display = 'Не задано'


class CoinInline(admin.TabularInline):
    model = Coin


class BanknoteInline(admin.TabularInline):
    model = Coin


class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        CoinInline,
        BanknoteInline,
    )
    list_display = (
        'title',        
    )


class CoinAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'description',
        'is_published',
        'is_on_main',
        'country',
        'year'
    )
    list_editable = (
        'category',
        'is_published',
        'is_on_main'
    )
    search_fields = ('name',)
    list_filter = ('category', 'country', 'year')
    list_display_links = ('name',)


class BanknoteAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'description',
        'is_published',
        'is_on_main',
        'country',
        'year'
    )
    list_editable = (
        'category',
        'is_published',
        'is_on_main'
    )
    search_fields = ('name',)
    list_filter = ('category', 'country', 'year')
    list_display_links = ('name',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Country)
admin.site.register(Material)
admin.site.register(Mint)
admin.site.register(Coin, CoinAdmin)
admin.site.register(Banknote, BanknoteAdmin)