from django.contrib import admin


class ContributorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']
    ordering = ['name']
