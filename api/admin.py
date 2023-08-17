from django.contrib import admin
from .models import Drinks
# Register your models here.
class DrinksAdmin(admin.ModelAdmin):
    list_display = ('id','name','description')

admin.site.register(Drinks, DrinksAdmin)
