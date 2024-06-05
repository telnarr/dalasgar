from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from datetime import datetime, timedelta
from user.forms import UserForm
from user.models import user

from gozle.forms import GozleForm
from gozle.models import gozle

from girenler.forms import GirenlerForm
from girenler.models import girenler

from giren.forms import GirenForm
from giren.models import giren

from talyp.forms import TalypForm
from talyp.models import talyp

from dosya.forms import dosyaform
from dosya.models import dosya


from tertip.forms import TertipForm
from tertip.models import tertip

from language.models import language

from meme.models import meme
import random

from django.utils import timezone
import datetime

from django import forms

gozlenen = []
ugurlar = []
filt = []
hug = ''
cc = -1
sann = 0
name_list = talyp.objects.all()
ksks = talyp.objects.all()
diller = language.objects.get(soz='tm')




def n1(request):
    global gozlenen, diller
    ok = UserForm()
    gz = GozleForm()
    x = 0

    xs = user.objects.all()
    paginator = Paginator(xs, 7)
    sahypa = request.GET.get('sayfa') or 1
    xx = paginator.get_page(sahypa)

    for i in user.objects.all():
        x += 1

    if len(gozlenen) > 0:
        ko = []
        xx = gozlenen
        gozlenen = []
    else:
        ko = user.objects.all()


    return render(request,'mugallym_gos.html',{'all':ok , 'teac':ko , 'jem':x , 'goz':gz , 'grk':gozlenen, 'den':xx , 'dil':diller})

def n2(request):
    if request.method == 'POST':
        lform = UserForm(request.POST)
        lform.save()
    return redirect ('/ulanyjy_gos')

def n3(request):
    al = UserForm()
    return render(request,'login.html',{'all':al})

def n4(request):
    global sssd, gozlenen
    if request.method == "GET":
        nam = request.GET.get("ad")
        pas = request.GET.get("pl")

    if nam == 'http://127.0.0.1:8000/static/student.png' and pas == 'http://127.0.0.1:8000/static/student.png':
        return redirect('/deneme')
    elif user.objects.filter(ulanyjy_ad=nam, parol=pas).exists():
        xx = user.objects.get(ulanyjy_ad=nam, parol=pas)
        dene = giren(san=xx.id)
        dene.save()
        now = datetime.datetime.now()
        san = ''
        mm = 0
        nn = 0
        for i in str(now):
            mm += 1
            if mm > 11:
                nn += 1
                if nn < 9:
                    san += i
        ilk, ikinci = san.split(':', 1)
        ilk = int(ilk)
        ilk += 5
        ilk = ilk % 24
        ilk = str(ilk)
        san = ilk + ':' + ikinci
        gosmak = girenler(ady=xx.ady, familya=xx.familya, idd=xx.id, ulanyjy_ad=xx.ulanyjy_ad, praol=xx.parol, wagt=san)
        gosmak.save()

        return redirect(f"/home/{nam}/{pas}")
    else:
        return redirect('/')


def n5(request):

    global name_list, diller

    gz = GozleForm()

    #search
    query = request.POST.get("posk")

    if query:
        xx = talyp.objects.filter(ady=query)
        x = len(xx)
    else:
        paginator = Paginator(name_list, 7)
        sahypa = request.GET.get('sayfa') or 1
        xx = paginator.get_page(sahypa)
        x = len(name_list)

    return render(request,'talyplar.html',{'jem':x,'goz':gz,'den':xx, 'dil':diller})

def n6(request):
    global diller
    all = TalypForm(initial={"netije": "Belli däl" , "atestat": 0 , "ekzamen1": 0 , "ekzamen2": 0 , "baha": 0})

    return render(request,'talyp_gos.html',{'all':all , 'dil':diller})

def n7(request):
    global gozlenen, diller
    goz = GozleForm()
    txt = open('girenler.txt' , 'r')
    list = []
    x = 0
    lis = girenler.objects.all()


    ters = girenler.objects.all()
    paginator = Paginator(ters[::-1], 7)
    sahypa = request.GET.get('sayfa') or 1
    xx = paginator.get_page(sahypa)




    for i in girenler.objects.all():
        x += 1

    if len(gozlenen) > 0:
        ko = []
        xx = gozlenen

        gozlenen = []
    else:
        ko = girenler.objects.all()

    kkk = xx.number - 1
    hhh = xx.number + 1



    return render(request,'girenler.html',{'den':xx , 'goz':goz , 'jem':x , 'kkk':kkk , 'hhh':hhh , 'dil':diller})


def n8(request, i):
    us = user.objects.get(id=i)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/', pk=user.i)
    else:
        form = UserForm(instance=us)
        return render(request, 'deneme2.html', {'form': form , 'ok':us})


def n9(request, i):
    xx = user.objects.get(id=i)
    if request.method == "POST":
        form = UserForm(request.POST, instance=xx)
        if form.is_valid():
            form.save()
            return redirect("/ulanyjy_gos")
    else:
        form = UserForm(instance=xx)
        return redirect(f"/uytget/{i}")

def poz(request, i):
    x = user.objects.get(id=int(i))
    x.delete()

    return redirect('/ulanyjy_gos')

def poz2(request, i):
    x = talyp.objects.get(id=int(i))
    x.delete()
    return redirect('/admin2')


def n10(request):
    global gozlenen
    query = request.get("posk")
    gozlenen = user.objects.filter(ady=query)
    return true

def n11(request):
    if request.method == "POST":
        form = TalypForm(request.POST, request.FILES)
        if form.is_valid():

            form.instance.netije = 'Belli däl'
            form.instance.atestat = 0
            form.instance.ekzamen1 = 0
            form.instance.ekzamen2 = 0
            form.instance.baha = 0


            form.save()
            return redirect('/admin2')
        else:
            form = TalypForm()
            return redirect('/talyp_gos')


def deneme(request):
    '''x = meme.objects.all()
    list = []
    for i in x:
        list.append(i)
    xx = random.choice(list)
    list2 = ['red','black','green','blue','pink','orange','purple','white','yellow','grey','#0458de','#a2c26e','#b80623','#a17f84','#3be3c7' ,'#54ba06']
    p = random.choice(list2)
    f = random.choice(list2)
    q = random.choice(list2)
    d = random.randint(0,150)
    z = random.choice(list2)

    x = dosya.objects.all()
    #return render(request, 'wideo2.html', {'all': xx , 'p':p , 'd':d , 'f':f , 'q':q , 'z':z})
    return render(request,'wideo2.html',{'x':x})'''
    # Müzik dosyasının yolunu belirle
    # Örneğin, uygulamanızın static klasöründe music.mp3 adlı bir dosya olsun
    music_file = "static/music.mp3"
    # Müzik dosyasını aç
    with open(music_file, "rb") as f:
    # Müzik dosyasını oku
        data = f.read()
    # Müzik dosyasının tipini belirle
    # Örneğin, mp3 formatında olsun
    content_type = "audio/mpeg"
    # Müzik dosyasını HTTP yanıtı olarak döndür
    return render(request,'wideo2.html')

def n12(request,i,p):
    global gozlenen , sssd, sann, filter_list, diller, ksks


    gz = GozleForm()
    sd = user.objects.get(ulanyjy_ad=i, parol=p)
    x = 0

    gozl = []
    gozl = gozlenen
    b3 = ''



    b2 = []
    bb = tertip.objects.all()
    for i in bb:
        b2.append(i)
    ug = b2[-1]


    filter_list = []
    for i in tertip.objects.all():
        filter_list.append(i)
    fil3 = filter_list[-1]
    fil4 = []


    goz2 = ''
    goz3 = ''
    goz4 = ''
    goz5 = ''


    if fil3.yyl != 'Ýyly':
        goz2 = fil3.yyl

    if fil3.ugur != 'Fakultet':
        goz3 = fil3.ugur

    if fil3.yasayan != 'Ýaşaýan ýeri':
        goz4 = fil3.yasayan

    if fil3.netije != 'Netije':
        goz5 = fil3.netije



    if goz2 != '' or goz3 != '' or goz4 != '' or goz5 != '':
        if talyp.objects.filter(fakultet = fil3.ugur):
            mmo = talyp.objects.filter(fakultet = fil3.ugur)
            for i in mmo:
                fil4.append(i)
    else:
        for i in talyp.objects.all():
            fil4.append(i)



    xx = []
    for i in gozlenen:
        xx.append(i)

    for i in ksks:
        x += 1

    if fil3.a_z == 'A_Z Ady':
        fil4 = talyp.objects.filter(netije="Geçdi").order_by('ady')




    xs = ksks
    ksks = talyp.objects.all()
    paginator = Paginator(xs, 7 )
    sahypa = request.GET.get('sayfa') or 1
    xxx = paginator.get_page(sahypa)


    if len(gozl) > 0 :
        xxx = gozl
        gozlenen = []

    fakultet = []
    for i in talyp.objects.all():
        if i.fakultet not in fakultet:
            fakultet.append(i.fakultet)

    filtr = TertipForm()
    b2 = []


    if sd.ulanyjy_ad and sd.parol == 'admin':
        return render(request,'homepage.html',{'all':sd , 'goz':gz , 'posk':xx , 'den':xxx , 'jem':x , 'dene':gozl ,'fakultet':fakultet , 'filter':filtr , 'fil3':fil3 , 'dil':diller})

    return render(request,'homepage2.html',{'all':sd , 'goz':gz , 'posk':xx , 'den':xxx , 'jem':x , 'dene':gozl ,'fakultet':fakultet , 'filter':filtr , 'fil3':fil3 , 'dil':diller})


def n13(request,q,p):
    global gozlenen

    if request.method == 'POST':
        lform = GozleForm(request.POST)
        lform.save()

    list = []
    jogap = []
    x = gozle.objects.all()
    for i in x:
        list.append(i)


    son = talyp.objects.filter(ady=list[-1])
    gozlenen = []

    for i in son:
        dene = talyp.objects.get(id= i.id)
        gozlenen.append(dene)

    return redirect(f"/home/{q}/{p}")


def n14(request, i, s):
    global diller
    bahalar = []
    belik = []
    x = talyp.objects.get(id=i)

    if x.ekzamen1 > 5:
        x.ekzamen1 = 5
    elif x.ekzamen1 < 2:
        x.ekzamen1 = 2


    if x.ekzamen2 > 5:
        x.ekzamen2 = 5
    elif x.ekzamen2 < 2:
        x.ekzamen2 = 2


    x.save()
    q = 0
    f = int(x.edebiyat) + int(x.inlis) + int(x.rus) + int(x.algebra) + int(x.geometriya) + int(x.informatika) + int(x.ikit) + int(x.fizika) + int(x.astronomiya) + int(x.himiya) + int(x.biologiya) + int(x.ekologiya) + int(x.geografiya) + int(x.tm_taryh) + int(x.ah_taryh) + int(x.jemgyyet)
    f += int(x.hukuk) + int(x.mod) + int(x.ykd) + int(x.oabm) + int(x.miras) + int(x.medeniyet) + int(x.cyzyw) + int(x.dte) + int(x.beden) + int(x.yasayys) + int(x.zapaz1) + int(x.zapaz2) + int(x.zapaz3) + int(x.zapaz4) + int(x.zapaz5) + int(x.zapaz6)

    belik.append(x.zapaz11)
    belik.append(x.zapaz22)
    belik.append(x.zapaz33)
    belik.append(x.zapaz44)
    belik.append(x.zapaz55)
    belik.append(x.zapaz66)

    for i in belik:
        if i != '-':
            q += 1
    q += 26
    f = f/q
    f = round(f, 1)

    x.atestat = f

    bir = x.ekzamen1
    iki = x.ekzamen2
    net = float(bir) + float(iki) + float(f)
    net = net / 3
    net = round(net, 1)

    x.baha = net



    x.save()

    bar = user.objects.get(id=s)

    return render(request, 'deneme.html',{'ok':x , 'd':f , 'den':net, 'dil':diller , 'bar':bar})


def n15(request):
    if request.method == 'POST':
        lform = TalypForm(request.POST)
        lform.save()
    return redirect ('/')

def n16(request, i):
    global diller
    belik = []
    q = 0
    x = talyp.objects.get(id=i)


    form = TalypForm(instance=x)


    return render(request,'ekzamen.html',{'ok':form , 'ko':x, 'dil':diller , 'ip':i})

def n17(request):
    global gozlenen

    if request.method == 'POST':
        lform = GozleForm(request.POST)
        lform.save()

    list = []
    jogap = []
    x = gozle.objects.all()
    for i in x:
        list.append(i)


    son = talyp.objects.filter(ady=list[-1])
    gozlenen = []
    for i in son:
        dene = talyp.objects.get(id= i.id)
        gozlenen.append(dene)
    return redirect('/admin2')

def n18(request):
    global gozlenen

    if request.method == 'POST':
        lform = GozleForm(request.POST)
        lform.save()

    list = []
    jogap = []
    x = gozle.objects.all()
    for i in x:
        list.append(i)


    son = girenler.objects.filter(ady=list[-1])
    gozlenen = []
    for i in son:
        dene = girenler.objects.get(id= i.id)
        gozlenen.append(dene)
    return redirect('/girenler')


def n19(request, i):
    x = talyp.objects.get(id=i)

    if request.method == "POST":
        form = TalypForm(request.POST, instance=x)
        if form.is_valid():
            form.save()
            return redirect(f"/sony/{i}")
    else:
        form = TalypForm(instance=x)
        return redirect(f"/ekzamen/{i}")

def n32(request,i):
    x = talyp.objects.get(id=i)

    if x.ekzamen1 == 0 and x.ekzamen2 == 0:
        x.ekzamen1 = 0
        x.ekzamen2 = 0
    elif x.ekzamen1 > 5:
        x.ekzamen1 = 5
    elif x.ekzamen1 < 2:
        x.ekzamen1 = 2
    elif x.ekzamen2 > 5:
        x.ekzamen2 = 5
    elif x.ekzamen2 < 2:
        x.ekzamen2 = 2



    x.save()
    belik = []
    q = 0
    f = int(x.edebiyat) + int(x.inlis) + int(x.rus) + int(x.algebra) + int(x.geometriya) + int(x.informatika) + int(x.ikit) + int(x.fizika) + int(x.astronomiya) + int(x.himiya) + int(x.biologiya) + int(x.ekologiya) + int(x.geografiya) + int(x.tm_taryh) + int(x.ah_taryh) + int(x.jemgyyet)
    f += int(x.hukuk) + int(x.mod) + int(x.ykd) + int(x.oabm) + int(x.miras) + int(x.medeniyet) + int(x.cyzyw) + int(x.dte) + int(x.beden) + int(x.yasayys) + int(x.zapaz1) + int(x.zapaz2) + int(x.zapaz3) + int(x.zapaz4) + int(x.zapaz5) + int(x.zapaz6)

    belik.append(x.zapaz11)
    belik.append(x.zapaz22)
    belik.append(x.zapaz33)
    belik.append(x.zapaz44)
    belik.append(x.zapaz55)
    belik.append(x.zapaz66)

    for b in belik:
        if b != '-':
            q += 1
    q += 26
    f = f/q
    f = round(f, 1)
    bir = x.ekzamen1
    iki = x.ekzamen2
    net = float(bir) + float(iki) + float(f)
    net = net / 3
    net = round(net, 1)

    x.baha = net
    #x.netije = 'oyoy'

    if bir == 0 and iki == 0:
        x.netije = 'Belli dal'
    elif net > 3.5 :
        x.netije = 'Geçdi'
    elif net < 3.5:
        x.netije = 'Ýykyldy'

    x.atestat = f
    x.save()
    return redirect('/admin2')

def n20(request):
    x = talyp.objects.all()
    return render(request,'tablisa.html',{'den':x})

def n21(request):
    global name_list
    name_list = talyp.objects.order_by('ady')
    return redirect('/admin2')

def n22(request, q, w):
    if request.method == 'POST':
        lform = TertipForm(request.POST)
        lform.save()

    return redirect(f'/home/{q}/{w}')

def n23(request):
    global name_list
    name_list = talyp.objects.order_by('familya')
    return redirect('/admin2')

def n24(request):
    global name_list
    name_list = talyp.objects.order_by('ata_ady')
    return redirect('/admin2')

def n25(request):
    global name_list
    name_list = talyp.objects.order_by('netije')
    return redirect('/admin2')

def n26(request):
    global name_list
    name_list = talyp.objects.order_by('fakultet')
    return redirect('/admin2')

def n27(request):
    global name_list
    name_list = talyp.objects.all()
    return redirect('/admin2')

def n28(request, i):
    global diller
    diller = language.objects.get(soz='tm')
    x = user.objects.get(id=i)

    return redirect(f'/home/{x.ulanyjy_ad}/{x.parol}')

def n29(request, i):
    global diller
    diller = language.objects.get(soz='ru')
    x = user.objects.get(id=i)
    return redirect(f'/home/{x.ulanyjy_ad}/{x.parol}')

def n30(request, i):
    global diller
    diller = language.objects.get(soz='en')
    x = user.objects.get(id=i)
    return redirect(f'/home/{x.ulanyjy_ad}/{x.parol}')


def n31(request):
    global ksks
    return render(request,'palyaco.html',{'x':ksks})

def n90(request):
    return render(request,'palyaco.html')

def filter(request , i):
    global ksks
    fak = request.GET.get("fak")
    net = request.GET.get("netije")
    yyl = request.GET.get("yyl")
    yas = request.GET.get("yasayan")
    azz = request.GET.get('a_z')
    x = user.objects.get(id=i)
    tayp = talyp.objects.all()


    if fak != '' and net != '':
        ksks = tayp.filter(fakultet=fak , netije=net)
    elif fak != '' and net != '' and yyl != '' and yas != '':
        ksks = tayp.filter(fakultet=fak , netije=net , doglan__year=yyl , adres__icontains=yas)
    elif net != '' and yyl != '' and yas != '':
        ksks = tayp.filter(netije=net , doglan__year=yyl ,  adres__icontains=yas)
    elif yyl != '' and yas != '':
        ksks = tayp.filter(doglan__year=yyl ,  adres__icontains=yas)
    elif yyl != '' and net != '':
        ksks = tayp.filter(doglan__year=yyl ,  netije=net)
    elif net != '' and yas != '':
        ksks = tayp.filter(netije=net ,  adres__icontains=yas)
    elif fak != '' and net != '' and yyl != '':
        ksks = tayp.filter(fakultet=fak ,  netije=net, doglan__year=yyl)
    elif fak != '' and yyl != '' and yas != '':
        ksks = tayp.filter(fakultet=fak , doglan__year=yyl, adres__icontains=yas)
    elif fak != '' and net != '' and yas != '':
        ksks = tayp.filter(fakultet=fak , netije=net, adres__icontains=yas)
    elif fak != '' and net != '':
        ksks = tayp.filter(fakultet=fak ,  netije=net)
    elif fak != '' and yyl != '':
        ksks = tayp.filter(fakultet=fak, doglan__year=yyl)
    elif fak != '' and yas != '':
        ksks = tayp.filter(fakultet=fak, adres__icontains=yas)
    else:
        if fak:
            ksks = tayp.filter(fakultet=fak)
        if net:
            ksks = tayp.filter(netije=net)
        if yyl:
            ksks = tayp.filter(doglan__year=yyl)
        if yas:
            ksks = tayp.filter(adres__icontains=yas)


    if azz == 'ady':
        ksks = tayp.order_by('ady')
    elif azz == 'familya':
        ksks = tayp.order_by('familya')
    elif azz == 'ata_ady':
        ksks = tayp.order_by('ata_ady')


    #return render(request, 'palyaco.html',{'cc':azz})
    return redirect(f'/home/{x.ulanyjy_ad}/{x.parol}')


def pim(request):
    x = dosya.objects.get(id=1)

    return render(request,'pim.html',{'i':x})
