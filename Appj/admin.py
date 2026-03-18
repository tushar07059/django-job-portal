from django.contrib import admin

from Appj.models import JobPost,location,Author,skills

class JobAdmin(admin.ModelAdmin):
    list_display=('title','date','salary',)
    list_filter=('date','salary','expiry',)
    search_fields=('title','salary',)
    search_help_text="Write in your query and hit enter "
    # fields=(('title','description'),'expiry')
    fieldsets=(
        (
            'Basic Information',{
                'fields':('title','description',)
            }
        ),
        (
            'More information',{
                'classes':('collapse','wide'),
                'fields':('expiry','salary')
            }
        ),
    )

# Register your models here.




admin.site.register(JobPost)
admin.site.register(location)
admin.site.register(Author)
admin.site.register(skills)
