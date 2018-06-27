from django.contrib import admin
from models import Events, Booked_slot
from django.contrib.auth.models import User

admin.site.register(Events)
admin.site.register(Booked_slot)


