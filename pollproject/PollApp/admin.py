from django.contrib import admin
from . models import PollRecord, Vote

# Register your models here.
admin.site.register(PollRecord)
admin.site.register(Vote)

