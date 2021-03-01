from django.contrib import admin
from .models import Listing
# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title' , 'is_published' , 'price' , 'list_date')
    list_display_links = ('id', 'title') # make list items clickable to take you to edit listing page
    #list_filter = ('realtor', ) #fitler box, haave to add comma at the end to avoid errors
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address', 'city')
    list_per_page = 25
    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        form.base_fields['price'].label = 'Price (leave empty for negotiable)'
        form.base_fields['mileage'].label = 'Mileage (try not to leave empty)'
        form.base_fields['engine'].label = 'Engine Capacity (try not to leave empty)'
        return form

admin.site.register(Listing, ListingAdmin)