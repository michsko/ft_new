from django.contrib import admin
from .models import Event
from .models import Member
from .models import ProductionTheater
from .models import ProductionStandup
# Register your models here.


admin.site.register(Event)
admin.site.register(Member)

admin.site.register(ProductionTheater)
admin.site.register(ProductionStandup)
