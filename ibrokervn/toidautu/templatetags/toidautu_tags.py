from django import template
register = template.Library()

from django.shortcuts import render, redirect, get_object_or_404

from Vimo.models import Vimo

@register.inclusion_tag('vimosimple.html')
def Vimosimple():

    ConAH = Vimo.objects.filter(DangAH=1).order_by('-Mucdo')
    return {'ConAH': ConAH }


from django.db.models import Sum

from GDNN.models import GDNN
# Create your views here.
@register.inclusion_tag('TKgdnn.html')
def TKgdnn():
    Name = [f for f in GDNN._meta.get_fields() if f.name != 'id' if f.name != 'status']
    Post = GDNN.objects.filter(status='published')
    Post5 = Post.order_by('id')[:5]
    Post20 = Post.order_by('id')[:20]
    Post40 = Post.order_by('id')[:40]
    Post60 = Post.order_by('id')[0:60]
    GTGDRong5days =    Post5.aggregate(total=Sum('Val_Rong'))
    GTGDRong20days =   Post20.aggregate(total=Sum('Val_Rong'))
    GTGDRong40days =   Post40.aggregate(total=Sum('Val_Rong'))
    GTGDRong60days =   Post60.aggregate(total=Sum('Val_Rong'))
    GTGDKLRong5days =  Post5.aggregate(total=Sum('Val_KL_Rong'))
    GTGDKLRong20days = Post20.aggregate(total=Sum('Val_KL_Rong'))
    GTGDKLRong40days = Post40.aggregate(total=Sum('Val_KL_Rong'))
    GTGDKLRong60days = Post60.aggregate(total=Sum('Val_KL_Rong'))
    GTGDTTRong5days =  Post5.aggregate(total=Sum('Val_TT_Rong'))
    GTGDTTRong20days = Post20.aggregate(total=Sum('Val_TT_Rong'))
    GTGDTTRong40days = Post40.aggregate(total=Sum('Val_TT_Rong'))
    GTGDTTRong60days = Post60.aggregate(total=Sum('Val_TT_Rong'))

    context = { 'Name': Name,
                'Post':Post,
                'Post5': Post5,
                'Post20': Post20,
                'Post40': Post40,
                'Post60': Post60,
                'GTGDRong5days': GTGDRong5days,
                'GTGDRong20days': GTGDRong20days,
                'GTGDRong40days': GTGDRong40days,
                'GTGDRong60days': GTGDRong60days,
                'GTGDKLRong5days': GTGDKLRong5days,
                'GTGDKLRong20days': GTGDKLRong20days,
                'GTGDKLRong40days': GTGDKLRong40days,
                'GTGDKLRong60days': GTGDKLRong60days,
                'GTGDTTRong5days': GTGDTTRong5days,
                'GTGDTTRong20days': GTGDTTRong20days,
                'GTGDTTRong40days': GTGDTTRong40days,
                'GTGDTTRong60days': GTGDTTRong60days,
               }

    return context


