from .models import FormSubmission, Department, Course, Purpose, Material
from django.contrib import admin

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'wikipedia_link')

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'department')

class PurposeAdmin(admin.ModelAdmin):
    list_display = ('name',)

class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name',)

class FormSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'dob', 'age', 'gender', 'phone_number', 'mail_id', 'address', 'department', 'course', 'purpose')
    filter_horizontal = ('materials_provided',)

# Register the models with their respective admin classes
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Purpose, PurposeAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(FormSubmission, FormSubmissionAdmin)
