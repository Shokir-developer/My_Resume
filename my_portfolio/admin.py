from django.contrib import admin

from my_portfolio.models import MySkills, MyPortfolio, SendModel, Blogs


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'blog_date')
    list_display_links = ('title', 'author',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(MySkills)
admin.site.register(MyPortfolio)
admin.site.register(SendModel)
admin.site.register(Blogs, BlogAdmin)
