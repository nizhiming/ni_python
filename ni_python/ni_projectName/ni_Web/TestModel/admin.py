from django.contrib import admin
from TestModel.models import Test,Contact,Tag

# Register your models here.
class TagInline(admin.TabularInline):
    model = Tag
    
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','age','email')   #list 列表显示
    search_fields = ('name',)
    inlines = [TagInline]   # Inline 内联显示
    #fields = ('name', 'email') # 自定义表单
    fieldsets = (
        ['Main',{
            'fields':('name','email'),
        }],
        ['Advance',{
            'classes':('collapse',),    # CSS
            'fields': ('age',),
        }]
    )
    
admin.site.register(Contact, ContactAdmin)
#admin.site.register([Test, Tag])
admin.site.register([Test])