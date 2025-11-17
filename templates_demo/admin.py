from django.contrib import admin
from .models import Constituency
from .models import Party

# Register your models here.
admin.site.register(Constituency)
admin.site.register(Party)
