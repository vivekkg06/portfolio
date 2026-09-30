

# Register your models here.
from django.contrib import admin
from .models import Profile, Service, Skill, Project, Contact


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "role")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "percentage")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at")
    readonly_fields = ("created_at",)