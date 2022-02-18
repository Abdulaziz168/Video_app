from django.shortcuts import render
from .models import Banner,Product,Category

def index(request):
    banners = Banner.objects.all()
    xorijlar = Product.objects.all()
    context = {"banners":banners,"xorijlar":xorijlar}
    return render(request,'index.html',context)

def index_light(request):
    return render(request,'index_light.html')

def landing(request):
    return render(request,'landing.html')

def moviegrid_light(request):
    return render(request,'moviegrid_light.html')

def moviegrid(request):
    return render(request,'moviegrid.html')

def moviesingle(request):
    return render(request,'moviesingle.html')

def moviegridfw_light(request):
    return render(request,'moviegridfw_light.html')

def moviegridfw(request):
    return render(request,'moviegridfw.html')

def movielist_light(request):
    return render(request,'movielist_light.html')

def movielist(request):
    return render(request,'movielist.html')

def base(request):
    return render(request,'base.html')

def _404page(request):
    return render(request,'404.html')

def blogdetail(request):
    return render(request,'blogdetail.html')

def blogdetail_light(request):
    return render(request,'blogdetail_light.html')

def bloggrid(request):
    return render(request,'bloggrid.html')

def bloggrid_light(request):
    return render(request,'bloggrid_light.html')

def bloglist(request):
    return render(request,'bloglist.html')

def bloglist_light(request):
    return render(request,'bloglist_light.html')

def celebritygrid01(request):
    return render(request,'celebritygrid01.html')

def celebritygrid01_light(request):
    return render(request,'celebritygrid01_light.html')

def celebritygrid02(request):
    return render(request,'celebritygrid02.html')

def celebritygrid02_light(request):
    return render(request,'celebritygrid02_light.html')

def celebritylist(request):
    return render(request,'celebritylist.html')

def celebritylist_light(request):
    return render(request,'celebritylist_light.html')

def celebritysingle(request):
    return render(request,'celebritysingle.html')

def celebritysingle_light(request):
    return render(request,'celebritysingle_light.html')

def comingsoon(request):
    return render(request,'comingsoon.html')

def homev2(request):
    return render(request,'homev2.html')

def homev2_light(request):
    return render(request,'homev2_light.html')

def homev3(request):
    return render(request,'homev3.html')

def homev3_light(request):
    return render(request,'homev3_light.html')

def blogdetail_light(request):
    return render(request,'blogdetail_light.html')

def bloggrid(request):
    return render(request,'bloggrid.html')

def bloggrid_light(request):
    return render(request,'bloggrid_light.html')

def bloglist(request):
    return render(request,'bloglist.html')

def bloglist_light(request):
    return render(request,'bloglist_light.html')

def celebritygrid01(request):
    return render(request,'celebritygrid01.html')

def seriessingle(request,pk):
    banners = Banner.objects.get(pk=pk)
    context = {
        'banners': banners
    }
    return render(request,'seriessingle.html',context)

def seriessingle_light(request):
    return render(request,'seriessingle_light.html')

def userfavoritegrid(request):
    return render(request,'userfavoritegrid.html')

def userfavoritegrid_light(request):
    return render(request,'userfavoritegrid_light.html')

def userfavoritelist(request):
    return render(request,'userfavoritelist.html')

def userfavoritelist_light(request):
    return render(request,'userfavoritelist_light.html')

def userprofile(request):
    return render(request,'userprofile.html')

def userprofile_light(request):
    return render(request,'userprofile_light.html')

def userrate(request):
    return render(request,'userrate.html')

def userrate_light(request):
    return render(request,'userrate_light.html')


