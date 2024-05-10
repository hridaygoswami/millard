from django.contrib import admin
from .models import menu_items, reservation, FeedBack
# Register your models here.


admin.site.register(menu_items )

admin.site.register(reservation)
admin.site.register(FeedBack)