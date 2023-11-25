from django.contrib import admin
from.models import Department,Doctore,Booking

class BookingAdmin(admin.ModelAdmin):
    list_display=('p_name','p_phone','doc_name','booked_to')
admin.site.register(Department)
admin.site.register(Doctore)
admin.site.register(Booking,BookingAdmin)
# Register your models here.
