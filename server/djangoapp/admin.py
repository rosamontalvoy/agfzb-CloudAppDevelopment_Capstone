from django.contrib import admin
from .models import CarMake, CarModel
# from .models import related models

# Register CarMake model
admin.site.register(CarMake)

# Define CarModelInline
class CarModelInline(admin.TabularInline):
    model = CarModel

# Register CarModel model with CarModelInline
@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]

