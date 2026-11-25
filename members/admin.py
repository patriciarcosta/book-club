from django.contrib import admin
from .models import Member, Book, ReadingLog


class ReadingLogInline(admin.TabularInline):
    model = ReadingLog
    extra = 1
    autocomplete_fields = ["book"]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "pages", "published_year")
    search_fields = ("title", "author")


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "email", "joined_date", "books_read")
    search_fields = ("firstname", "lastname", "email", "phone")
    list_filter = ("joined_date",)
    date_hierarchy = "joined_date"
    inlines = [ReadingLogInline]

    @admin.display(description="Books read")
    def books_read(self, obj):
        return obj.readings.count()


@admin.register(ReadingLog)
class ReadingLogAdmin(admin.ModelAdmin):
    list_display = ("member", "book", "date_finished")
    list_filter = ("date_finished",)
    search_fields = ("member__firstname", "member__lastname", "book__title")
    autocomplete_fields = ("member", "book")
    date_hierarchy = "date_finished"