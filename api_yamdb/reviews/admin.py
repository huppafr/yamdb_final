from django.contrib import admin
from reviews.models import Comment, Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'author', 'score', 'pub_date')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'author', 'pub_date')


admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
