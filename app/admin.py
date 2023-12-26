from django.contrib import admin

from .models import Alergen,Pancake,CreateYourOwn,Drink,FeaturedGame

admin.site.register(Alergen)
admin.site.register(Pancake)
admin.site.register(CreateYourOwn)
admin.site.register(Drink)
admin.site.register(FeaturedGame)

from django.contrib.admin import AdminSite

class CustomAdminSite(AdminSite):
    site_header = 'Palačinkara kod Bagija'
    site_title = 'Administracija'
    index_title = 'Palačinkara kod Bagija'

custom_admin_site = CustomAdminSite(name='admin')


class MyModelAdmin(admin.ModelAdmin):
    # ...
    fieldsets = [
        ("Section title", {
            "classes": ("collapse", "expanded"),
            "fields": (...),
        }),
    ]