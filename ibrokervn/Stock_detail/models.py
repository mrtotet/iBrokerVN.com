from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models



from django.db import models
from django.utils import timezone
from datetime import date
from django.contrib.auth.models import User
from django.urls import reverse
from autoslug import AutoSlugField
from django.core.validators import MaxValueValidator, MinValueValidator


from django.utils.text import slugify
from django.template.defaultfilters import slugify
# Create your models here.
STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
)
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Stock_Detail(models.Model):
    publish =           models.DateTimeField(default=timezone.now, blank=True, null=True)
    S_created =         models.DateTimeField(auto_now_add=True,null=True)
    S_updated =         models.DateTimeField(auto_now=True,null=True)
    S_status =          models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft',null=True)
    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # The Dahl-specific manager.

    Symbol =            models.CharField("Mã CK",max_length=10, blank=True, null=True, unique = True)
    Name =              models.CharField("Tên Công Ty",max_length=50, blank=True, null=True)
    slug =              AutoSlugField(populate_from='Symbol',null=True)
    San =               models.CharField("Sàn",max_length=10, blank=True, null=True)
    Website =           models.CharField("Website",max_length=100, blank=True, null=True)
    So_dien_thoai =     models.CharField("Số điện thoại",max_length=50, blank=True, null=True)
    Dia_chi =           models.CharField("Địa chỉ",max_length=200, blank=True, null=True)
    Quan =              models.CharField("Quận/Huyện",max_length=50, blank=True, null=True)
    Tinh =              models.CharField("Tỉnh/Thành",max_length=100, blank=True, null=True)
    Tong_Quan =         models.TextField("Tổng quan",max_length=2000, blank=True, null=True)
    Industry =          models.CharField("Ngành",max_length=100, blank=True, null=True)
    SL_CP_Niem_yet =    models.BigIntegerField("Số lượng CP Niêm Yết", blank=True, null=True)
    Ty_le_Freeloat =    models.DecimalField("Free-loat", max_digits=4, decimal_places=2, blank=True, null=True)
    Ty_le_SHNN =        models.DecimalField("Tỷ lệ SH NN tối đa",max_digits=4, decimal_places=2, blank=True, null=True)



    #Total_score = int(((Management * W_Ma) + (Capital * W_Ca) + (Qualify_asset * W_Qu_As) (Leverage * W_Lev) + (Share * W_Share) +(Perform * W_Perform))
    #Check = (W_Ma + W_Ca +  W_Qu_As + W_Lev + W_Share + W_Perform)
    class Meta:
        ordering = ('Symbol',)
    def __str__(self):
        return self.Symbol


    def get_absolute_url(self):
        return reverse('Stock_detail_1:Stock_detail_2', args=[self.slug])


class Recommend(models.Model):

    title =     models.CharField(max_length=250)
    R_publish = models.DateTimeField(default=timezone.now, primary_key=True)
    R_created = models.DateTimeField(auto_now_add=True)
    R_updated = models.DateTimeField(auto_now=True)
    R_status =  models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # The Dahl-specific manager.
    Stock_chosen =  models.ManyToManyField(Stock_Detail, through= 'Estimate')

    viewed =        models.IntegerField(default=0)

    class Meta:
        ordering = ('-R_publish',)
    def __str__(self):
        return self.title


class Estimate (models.Model):

    POSITION_CHOICES = (  ('open', 'Mở vị thế GD'),
                        ('Close', 'Đóng vị thế GD')       )

    GD_CHOICES =             (   ('Buy', 'Mua'),
                                ('Buy_More', 'Mua Thêm'),
                                ('Hold', 'Nắm  giữ'),
                                ('Take_profit', 'Chốt lời'),
                                ('Cut_loss', 'Cắt lỗ'),
                                ('Sell_partion', 'Bán dần'),
                                ('Sell_all', 'Bán hết')     )

    STYLE_CHOICES =             (   ('Longterm', 'Dài hạn'),
                                ('Shorterm', 'Ngắn hạn'),
                             )

    Stock =       models.ForeignKey(Stock_Detail,related_name='estimate_Com', on_delete=models.CASCADE)
    DateRecommend =     models.ForeignKey(Recommend, on_delete=models.CASCADE, blank= True, null= True)
    author =            models.ForeignKey(User, blank=True, null=True,
                                       related_name='WatchList', on_delete=models.CASCADE)
    publish =           models.DateTimeField(default=timezone.now, blank=True, null=True)

    S_created =         models.DateTimeField(auto_now_add=True,null=True)
    S_updated =         models.DateTimeField(auto_now=True,null=True)
    S_status =          models.CharField(max_length=10,
                                        choices=STATUS_CHOICES,
                                        default='draft',null=True)
    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # The Dahl-specific manager.

    Postion=                models.CharField(max_length=10,
                                        choices=POSITION_CHOICES,
                                             blank=True,null=True)
    Trade=                  models.CharField(max_length=10,
                                        choices=GD_CHOICES,
                                             blank=True,null=True)
    Style=                  models.CharField(max_length=10,
                                        choices=STYLE_CHOICES,
                                             blank=True,null=True)
    Price_open=             models.IntegerField("Giá mở vị thế",default=1,null=True, blank=True)
    Price_update=           models.IntegerField("Giá cập nhật",default=1,null=True, blank=True)
    @staticmethod
    def Cal_Gain_loss(a, b):
        Cal = int((a-b)*100/a)
        return Cal

    def Gain_Loss(self):
        return self.Cal_Gain_loss(self.Price_open, self.Price_update)

    @staticmethod
    def Cal_PE_PB(a,b):
        Cal = int(a/b)
        return  Cal

    EPS =                   models.IntegerField("EPS",default=1,null=True, blank=True)
    def PE(self):
        return self.Cal_PE_PB(self.Price_update, self.EPS)
    Bookvalue =             models.IntegerField("Book Value",default=1,null=True, blank=True)
    def PB(self):
        return self.Cal_PE_PB(self.Price_update, self.Bookvalue)
    Liquidity_30days =      models.BigIntegerField("KL GDTB 30 ngày", blank=True, null=True)
    Price_change_5days=     models.IntegerField("Giá thay đổi 5 ngày",null=True, blank=True)
    Price_change_20days=    models.IntegerField("Giá thay đổi 20 ngày",null=True, blank=True)
    Price_change_60days=    models.IntegerField("Giá thay đổi 60 ngày",null=True, blank=True)

    EnvironmentIndustry =   models.IntegerField("Mô trường kinh doanh",default=7,null=True, blank=True, validators = [MaxValueValidator(10),MinValueValidator(0)])
    W_Envi =                models.PositiveIntegerField(default=20, null=True, blank=True)
    Management =            models.IntegerField("Quản trị Doanh Nghiệp",default=7, null=True, blank=True, validators = [MaxValueValidator(10),MinValueValidator(0)])
    W_Ma =                  models.IntegerField(default=10, null=True, blank=True)
    Qualify_asset =         models.IntegerField("Chất lượng tài sản",default=7, null=True, blank=True, validators = [MaxValueValidator(10),MinValueValidator(0)])
    W_Qu_As =               models.PositiveIntegerField(default=10, null=True, blank=True)
    Leverage =              models.IntegerField("Tỷ lệ vay nợ",default=7, null=True, blank=True, validators = [MaxValueValidator(10),MinValueValidator(0)])
    W_Lev =                 models.PositiveIntegerField(default=10, null=True, blank=True)
    Top_industry =          models.IntegerField("Thứ hạng trong ngành",default=7, null=True, blank=True, validators = [MaxValueValidator(10),MinValueValidator(0)])
    W_Top_industry =        models.PositiveIntegerField(default=10, null=True, blank=True)
    Perform =               models.IntegerField("Hiệu suất kinh doanh",default=7, null=True, blank=True, validators = [MaxValueValidator(10),MinValueValidator(0)])
    W_Perform =             models.PositiveIntegerField(default=15, null=True, blank=True)
    Capital =               models.IntegerField("Vốn hóa",default=7, null=True, blank=True, validators = [MaxValueValidator(10),MinValueValidator(0)])
    W_Ca =                  models.IntegerField(default=10, null=True, blank=True)
    Liquidity =             models.IntegerField("Thanh khoản",default=7, null=True, blank=True, validators = [MaxValueValidator(10),MinValueValidator(0)])
    W_Li =                  models.IntegerField(default=15, null=True, blank=True)
    Commnent =              models.TextField("Đánh giá DN", max_length=2000, blank=True, null=True)
    Indicator =             models.IntegerField(default=50, null=True, blank=True, validators = [MaxValueValidator(100),MinValueValidator(0)])
    action =                models.TextField("Đề xuất GD", max_length=2000, blank=True, null=True)


    # Total_score = models.PositiveIntegerField()

    @staticmethod
    def Calculatiion_score(a, b, c, d, e, f, g, h, i, j, k, l, m, n,o,p):
        full_Weight = int(b + d + f + h + j + l + n +p)
        Cal_score = int(((a * b) + (c * d) + (e * f) + (g * h) + (i * j) + (k * l) + (m * n) + (o * p)) /
                   full_Weight)
        return  Cal_score

    def Total_score(self):
        return self.Calculatiion_score(self.EnvironmentIndustry, self.W_Envi,
                                       self.Management, self.W_Ma,
                                       self.Qualify_asset, self.W_Qu_As,
                                       self.Leverage, self.W_Lev,
                                       self.Top_industry, self.W_Top_industry,
                                       self.Perform, self.W_Perform,
                                       self.Capital, self.W_Ca,
                                       self.Liquidity, self.W_Li,
                                       )



    class Meta:
        ordering = ('-publish',)



"""

class Action(models.Model):
    DateRecommend = models.ForeignKey(Recommend, on_delete=models.CASCADE)
    Stock = models.ForeignKey(Stock_Detail,on_delete=models.CASCADE)
    Apublish = models.DateField(default=date.today)
    Indicator = models.IntegerField(default=0)
    action = models.CharField(max_length=15)
    class Meta:
        ordering = ('-Apublish',)
        
        
        
    @staticmethod
    def Cal_Gain_loss(a, b):
        gain_loss = int(b+a)
        Cal_G_L = gain_loss
                  #*100/int(a)
        return  Cal_G_L   

    def Gain_Loss(self):
        return self.Cal_Gain_loss(self.Price_open, self.Price_update)

    @staticmethod
    def Cal_PE_PB(a,b):
        Cal = int(a+b)
        return  Cal

    def PE(self):
        return self.Cal_PE_PB(self.Price_update, self.EPS)
        
    def PB(self):
        return self.Cal_PE_PB(self.Price_update, self.Bookvalue)   
        
        
        
    @staticmethod
    def Calculatiion_score(a, b, c, d, e, f, g, h, i, j, k, l, m, n,o,p):
        full_Weight = int(b + d + f + h + j + l + n +p)
        Cal_score = int(((a * b) + (c * d) + (e * f) + (g * h) + (i * j) + (k * l) + (m * n) + (o * p)) /
                   full_Weight)
        return  Cal_score

    def Total_score(self):
        return self.Calculatiion_score(self.EnvironmentIndustry, self.W_Envi,
                                       self.Management, self.W_Ma,
                                       self.Qualify_asset, self.W_Qu_As,
                                       self.Leverage, self.W_Lev,
                                       self.Top_industry, self.W_Top_industry,
                                       self.Perform, self.W_Perform,
                                       self.Capital, self.W_Ca,
                                       self.Liquidity, self.W_Li,
                                       )
             


"""