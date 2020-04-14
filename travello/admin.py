from .models import Destination
from django.contrib import admin
from .models import Questionpool
from .models import Clock

# Register your models here.
admin.site.register(Destination)
admin.site.register(Questionpool)
admin.site.register(Clock)
