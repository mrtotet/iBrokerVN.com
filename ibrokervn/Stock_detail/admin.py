from django.contrib import admin

# Register your models here.

from django.contrib import admin



# Register your models here.
from .models import Stock_Detail, Recommend, Estimate


def published_selected_Objects(self, request, queryset):
    rows_updated = queryset.update(S_status='published')
    if rows_updated == 1:
        message_bit = "1 Row was"
    else:
        message_bit = "%s Rows were" % rows_updated
    self.message_user(request, "%s successfully marked as published." % message_bit)



class StockInline(admin.StackedInline):
    model = Recommend.Stock_chosen.through
    extra = 2





class StockAdmin(admin.ModelAdmin):
    list_display = ('Symbol','S_status','slug','San','Industry','SL_CP_Niem_yet','Ty_le_Freeloat','Ty_le_SHNN',)
    list_editable = ['S_status',]
    list_per_page = 15
    list_filter = ('Industry','S_status', 'publish','San',)
    search_fields = ('Symbol','San',)
    inlines = [
        StockInline,
    ]
    fieldsets = [
        ['Stock general information',{'fields': [('Symbol','San'),'Name','Industry',('S_status','publish')]}],
        ['Stock Basic Info', {
            'classes': ['collapse'],
            'fields': ['Website','So_dien_thoai','Dia_chi',
                       ('Quan', 'Tinh'),'Tong_Quan','SL_CP_Niem_yet', ('Ty_le_Freeloat','Ty_le_SHNN'),],
        }]
        ,]
    #prepopulated_fields = {'slug': ('Symbol',)} #điền trước cho slugfield
    #raw_id_fields = ('author',) #thêm ô search thông tin author





    actions = [published_selected_Objects]

    """

    fields = [('Symbol','Industry'),('author','S_status','publish'),('strength','Indicator'),
              ('Management','W_Ma'),('Capital','W_Ca'), ('Qualify_asset','W_Qu_As'),
              ('Leverage','W_Lev'), ('Share','W_Share'), ('Perform','W_Perform'),'Total_score']
              
            ['Stock Fundemental Analyst', {
                                        'classes': ['collapse'],
                                        'fields': [ ('EnvironmentIndustry','W_Envi'),
                                            ('Management','W_Ma'),('Capital','W_Ca'), ('Qualify_asset','W_Qu_As'),
                                        ('Leverage', 'W_Lev'), ('Share', 'W_Share'), ('Perform', 'W_Perform')],
        }],          
              
              """

    #actions_on_bottom = True
    #actions_on_top = False





class RecommendAdmin(admin.ModelAdmin):
    list_display = ('title','R_publish','R_status','list_of_stock')
    def list_of_stock(self, obj):
        return ("%s" % ','.join([name.Symbol for name in obj.Stock_chosen.all()]))
    list_of_stock.short_description = 'list_stock_daily'
    list_filter = ['title']
    list_editable = ('R_status',)
    search_fields = ['title']
    filter_horizontal = ['Stock_chosen']
    actions = [published_selected_Objects]

#'Gain_Loss','PE','PB',
class EsitmateAdmin(admin.ModelAdmin):
    list_display = ('DateRecommend','publish','Stock','S_status','Postion','Trade','Style','Indicator','Total_score','Gain_Loss','PE','PB',)
    list_editable = ('S_status','Postion','Trade','Style','Indicator',)
    search_fields = ['Stock','DateRecommend',]
    list_filter = ('S_status', 'Postion','Trade', 'Style',)
    fieldsets = [
        ['Stock general information',{'fields': ['Stock','DateRecommend','publish',('author','S_status'),('Postion','Trade','Style'),'Indicator','action']}],
        ['Stock Update Info', {
            'classes': ['collapse'],
            'fields': [('Price_open','Price_update'),('Price_change_5days','Price_change_20days','Price_change_60days'),('EPS','Bookvalue'),'Liquidity_30days'
                       ],
        }],
        ['Stock Fundemental Analyst', {
            'classes': ['collapse'],
            'fields': [('EnvironmentIndustry', 'W_Envi'), ('Management', 'W_Ma'),
                       ('Qualify_asset', 'W_Qu_As'), ('Leverage', 'W_Lev'),
                       ('Top_industry', 'W_Top_industry'), ('Perform', 'W_Perform'),
                       ('Capital', 'W_Ca'), ('Liquidity', 'W_Li'),'Commnent' ],
        }]
        ,]
    actions = [published_selected_Objects]





admin.site.register(Recommend,RecommendAdmin)
admin.site.register(Stock_Detail,StockAdmin)
admin.site.register(Estimate,EsitmateAdmin)
