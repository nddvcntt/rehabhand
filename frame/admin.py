from django.contrib import admin

from .models import *


# Register your models here.

class Patadmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'sex', 'address', 'weakhand']
    list_filter = ['name', 'address']
    search_fields = ['name']


admin.site.register(Patient, Patadmin)

class Exadmin(admin.ModelAdmin):
    list_display = [ 'name_uk', 'frequency']
    list_filter = ['name_uk', 'frequency']
    search_fields = ['name_uk']

admin.site.register(Exercise, Exadmin)

class Ex_videoadmin(admin.ModelAdmin):
    list_display = ['exercise', 'raw_video', 'file_name','frame_start','frame_stop','path']
    list_filter = ['exercise', 'raw_video', 'file_name','frame_start','frame_stop','path']
    search_fields = ['exercise']

admin.site.register(Ex_video, Ex_videoadmin)


class Rvadmin(admin.ModelAdmin):
    list_display = ['patient', 'position', 'nFrames', 'file_path']
    list_filter = ['patient', 'position', 'nFrames', 'file_path']
    search_fields = ['patient', 'position']


admin.site.register(Raw_video, Rvadmin)

class Svadmin(admin.ModelAdmin):
    list_display = ['ex_video', 'start', 'end']
    list_filter = ['ex_video', 'start', 'end']
    search_fields = ['ex_video', 'start', 'end']
admin.site.register(Seg_video, Svadmin)


class Decadmin(admin.ModelAdmin):
    list_display = ['DataAug', 'apLeft','apRight','mapIou50','mapIou75','mapIou','paperlink']
    list_filter = ['DataAug', 'apLeft']
    search_fields = ['DataAug', 'apLeft','apRight','mapIou50','mapIou75','mapIou','paperlink']
admin.site.register(Detection, Decadmin)

class Segmenadmin(admin.ModelAdmin):
    list_display = ['DataAug', 'apLeft','apRight','mapIou50','mapIou75','mapIou','paperlink']
    list_filter = ['DataAug', 'apLeft']
    search_fields = ['DataAug', 'apLeft','apRight','mapIou50','mapIou75','mapIou','paperlink']


admin.site.register(Segmentation, Segmenadmin)

class GeneralAdmin(admin.ModelAdmin):
    list_display = ['data', 'dextroushand','weekhand','timestart', 'timestop', 'path_camera','path_accelerometor']
    list_filter = ['data', 'dextroushand','weekhand','timestart', 'timestop', 'path_camera','path_accelerometor']
    search_fields = ['data', 'dextroushand','weekhand','timestart', 'timestop', 'path_camera','path_accelerometor']
admin.site.register(General, GeneralAdmin)