from django.contrib import admin
from .models import Cpu, Gpu, Ram, Profile, UserRig, Postai, PostaiReview, Advertisements

# Register your models here.

class CpuAdmin(admin.ModelAdmin):
    list_display = ('manufacturer', 'model', 'base_speed')

class GpuAdmin(admin.ModelAdmin):
    list_display = ('manufacturer', 'model', 'vram', 'power_pins')

class RamAdmin(admin.ModelAdmin):
    list_display = ('manufacturer', 'model', 'size')


admin.site.register(Cpu, CpuAdmin)
admin.site.register(Gpu, GpuAdmin)
admin.site.register(Ram, RamAdmin)
admin.site.register(Profile)
admin.site.register(UserRig)
admin.site.register(Postai)
admin.site.register(PostaiReview)
admin.site.register(Advertisements)
