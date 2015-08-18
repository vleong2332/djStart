from django.contrib import admin
from .models import ProjectCharter, Material


class MaterialInline(admin.TabularInline):
	model = Material
	extra = 1

class ProjectCharterAdmin(admin.ModelAdmin):
	list_display = ('proj_name', 'acc_num', 'src_lang_name', 'des_lang_name', 'start_date', 'completion_date')
	search_fields = ['proj_name', 'acc_num', 'src_lang_name', 'des_lang_name']
	inlines   = [MaterialInline]
	fieldsets = [
		(None, {'fields': ['proj_name', 'acc_num']}),
		(None, {'fields': ['src_lang_name', 'src_lang_ietf', 'des_lang_name', 'des_lang_ietf']}),
		('Details', {'fields': ['location_general', 'start_date', 'completion_date', 'op_responsible', 'funding_src']}),
		(None, {'fields': ['output_target', 'output_other', 'content_aided', 'content_other']}),
		(None, {'fields': ['check_lvl', 'check_workflow']}),
		(None, {'fields': ['content_flow', 'content_person']})
	]
	list_per_page = 50
	# date_hierarchy = 'start_date'


admin.site.register(ProjectCharter, ProjectCharterAdmin)