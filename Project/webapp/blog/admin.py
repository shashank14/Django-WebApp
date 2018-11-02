from django.contrib import admin
from .models import Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):

    list_display = ['title','author','status']
    prepopulated_fields={'slug':('title',)}
    list_filter=('status','author','created','publish')
    search_fields=('title','content')
    raw_id_fields=('author',)
    # date_hierarchy='publish'
    # ordering=['status','publish']


    class Meta:
        model = Post


admin.site.register(Post,PostAdmin)
