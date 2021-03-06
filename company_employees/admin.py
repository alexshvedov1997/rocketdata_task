from django.contrib import admin
from .models import Position, Level, OtherInformation, Chief, Employer

# Register your models here.

def delete_admin():
    pass

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ["position_title"]

@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ["level_title"]


@admin.register(OtherInformation)
class OtherInformationAdmin(admin.ModelAdmin):
    list_display = ["age", "telephone_number"]

@admin.register(Chief)
class ChiefAdmin(admin.ModelAdmin):
    list_display = ["full_name", "position", "level", "salary"]


@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = ["full_name", "position", "level", "chief", "salary", "paid_salary"]
    list_display_links = ["chief"]
    list_filter = ["level", "position"]




