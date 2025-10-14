from django.contrib import admin
from contact.models import Contact, Category

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','firts_name','last_name','phone','email')
    ordering = ('id',)
    #list_filter = ('create_date',)
    list_display_links = ('firts_name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('id',)
    