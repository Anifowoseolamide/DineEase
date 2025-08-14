from django.contrib import admin
from .models import Category, MenuItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'order', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'description']
    list_editable = ['order', 'is_active']
    readonly_fields = ['created_at']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'is_popular', 'is_active', 'created_at']
    list_filter = ['category', 'is_vegetarian', 'is_gluten_free', 'is_spicy', 'is_popular', 'is_active', 'created_at']
    search_fields = ['name', 'description']
    list_editable = ['is_popular', 'is_active']
    readonly_fields = ['created_at', 'updated_at']
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = []
