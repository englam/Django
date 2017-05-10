
from django.contrib import admin
from restaurants.models import Restaurant, Food

# Register your models here.

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'address') #display information
    search_fields = ('name',) #for searching

class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant', 'price')
    list_filter = ('is_spicy',) # for filtering
    fields = ( 'price' , 'restaurant')  #limit edit fields
    ordering    = ('-price',) #for sorting


#admin.site.register(Restaurant)
admin.site.register(Restaurant,RestaurantAdmin)

#admin.site.register(Food)
admin.site.register(Food,FoodAdmin)
