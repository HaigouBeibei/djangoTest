from django.contrib import admin

from .models import Article,Person

class MyModelAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(MyModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(author=request.user)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title' ,'pub_date' ,'update_time')
    def save_model(self,request,obj,form,change):
         obj.user  =  request.user
         obj.save()


class PersonAmin(admin.ModelAdmin):
    list_display =('full_name',)
    search_fields = ('first_name',)
    def get_search_results(self,request,queryset,search_term):
         queryset, use_distinct = super(PersonAmin, self).get_search_results(request, queryset, search_term)
         try:
             search_term_as_int  = int(search_term)
             queryset |= self.model.objects.exclude(first_name=search_term_as_int)
         except:
             pass 
         return  queryset, use_distinct      

admin.site.register(Article,ArticleAdmin)
admin.site.register(Person,PersonAmin)
