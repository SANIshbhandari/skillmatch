from django.contrib import admin

from .models import CompanyProfile, SeekerProfile


@admin.register(SeekerProfile)
class SeekerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'education_level', 'years_experience')
    search_fields = ('user__username', 'user__email')
    filter_horizontal = ('skills',)


@admin.register(CompanyProfile)
class CompanyProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'location')
    search_fields = ('name', 'user__username')
