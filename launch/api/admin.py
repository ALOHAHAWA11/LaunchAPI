from django.contrib import admin
from .models import *

admin.site.register(Comment)
admin.site.register(Launch)
admin.site.register(Pad)
admin.site.register(Rocket)