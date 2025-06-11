from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

# Register your models here.
#admin.site.register(Book)
#admin.site.register(Author)
#admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)

class BookInstanceInline(admin.TabularInline):
    model = BookInstance

class AuthorInline(admin.TabularInline):
    model = Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [AuthorInline]

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BookInstanceInline]

 
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    #list_display = ('book', 'due_back', 'status')
    list_filter = ('status', 'due_back')
    fieldsets = (
        ("Test", {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )
 

