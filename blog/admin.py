from django.contrib import admin

# Register your models here.
from .models import Article,Comment,Live,Lyric,Chord


admin.site.register(Comment)
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):    
    actions = ['download_csv']

    list_display = ["title","author","created_date","slug","editing"]

    list_display_links = ["title","created_date"]

    search_fields = ["title"]

    list_filter = ["created_date"]
    class Meta:
        model = Article

    def download_csv(self, request, queryset):
        import csv
        from django.http import HttpResponse
    
        f = open('some.csv', 'wb')
        writer = csv.writer(f)
        writer.writerow(['author','title','english_title','slug','content','Optional_english_version_content','created_date','editing','article_image'])
    
        for s in queryset:
            writer.writerow([s.author, s.title, s.english_title, s.slug, s.content, s.Optional_english_version_content, s.created_date, s.editing, s.article_image])
    
        f.close()
    
        f = open('some.csv', 'r')
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=stat-info.csv'
        return response

@admin.register(Live)
class LiveAdmin(admin.ModelAdmin):    
    list_display = ["title","video_id","caption_or_description"]

    list_display_links = ["title","video_id","caption_or_description"]

    search_fields = ["video_id","title","caption_or_description"]

    list_filter = ["video_id","title","caption_or_description"]
    class Meta:
        model = Live

@admin.register(Lyric)
class LyricAdmin(admin.ModelAdmin):    
    actions = ['download_csv']

    list_display = ["english_name","author","created_date","slug","english_lyrics","editing"]

    list_display_links = ["english_name","created_date"]

    search_fields = ["english_name"]

    list_filter = ["created_date"]
    class Meta:
        model = Lyric

@admin.register(Chord)
class ChordAdmin(admin.ModelAdmin):    
    
    list_display = ["english_name","author","key","created_date","slug","english_lyrics","editing"]

    list_display_links = ["english_name","created_date","key"]

    search_fields = ["english_name","key"]

    list_filter = ["created_date"]
    class Meta:
        model = Chord