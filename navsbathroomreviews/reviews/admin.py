from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Review

admin.site.register(Review)

class ReviewAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    # list_display = ('title','slug','status','created_on')
    # list_filet = ('status')
    # search_fields = ['title','content']
    prepopulated_fields = {'slug':('title',)}
    
admin.site.unregister(Review)
admin.site.register(Review,ReviewAdmin)