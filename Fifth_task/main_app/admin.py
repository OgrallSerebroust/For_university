from django.contrib import admin
from .models import Theatre, Show, Visitor


class TheatreAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


class ShowAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    list_filter = ["theatre"]
    raw_id_fields = ["theatre"]


class VisitorAdmin(admin.ModelAdmin):
    list_display = ["name", "age"]
    search_fields = ["name"]
    list_filter = ["show"]
    raw_id_fields = ["show"]


admin.site.register(Theatre, TheatreAdmin)
admin.site.register(Show, ShowAdmin)
admin.site.register(Visitor, VisitorAdmin)
