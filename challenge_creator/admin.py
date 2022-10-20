from django.contrib import admin
from .models import ChallengeStatement, Industry


# Register your models here.
class ChallengeStatementAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'challenge_title', 'challenge_location', 'status',)
    list_display_links = ('id', 'user',)
    list_filter = ('status', )


admin.site.register(ChallengeStatement, ChallengeStatementAdmin)
admin.site.register(Industry)
