from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from useractions.models import Announcement
from authentication.models import Account,Spartan
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from .forms import ProfileEditForm, PostForm
import md5
import datetime



def logout_view(request):
    logout(request)
    return redirect(reverse('home'))


def create_post(request):
    if request.user.is_authenticated():
        curruser = request.user
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                post_text = form.cleaned_data['text']
                adress = form.cleaned_data['adress']
                country = form.cleaned_data['country'] 
                city = form.cleaned_data['city']
                category = form.cleaned_data['category']
                time = form.cleaned_data['timePost']
                time = ":".join(map(lambda item: item.strip(), time.split(":")))
                data_post = form.cleaned_data['data']
                data_post=datetime.datetime.strptime(data_post, '%m/%d/%Y').strftime('%Y-%m-%d')
                money_user = form.cleaned_data['price']
                announcement = Announcement.objects.create(title=title, text=post_text, address=adress, country=country,
                                                           category=category,money =money_user, city=city,data=data_post, timePost=time, author=request.user)
                announcement.save()
                subject='Anunt Project Spartan'
                messagetip=" Buna % s , \n Ati postat un anunt cu succes! \n" \
                    " Titlul : %s ,\n Text: %s \n Adress: %s \n Country : %s \n City: %s \n category: %s \n" \
                    " Time : %s \n Data indepliniri task-ului: %s \n " \
                    "Suma maxima pentru licitatie: %s lei \n O zi buna!"  %(request.user.username,title,post_text,adress,country,city,category,time,data_post,money_user)
                from_email=settings.EMAIL_HOST_USER
                send_mail(subject, messagetip, from_email,
                          [request.user.email], fail_silently=True)
                return redirect('/')
            else:
                return render(request, 'useractions/create_post.html', {
                    'cod': curruser.account.cod,
                    'form': form,
                    'errors': ['Invalid form'] })
        else:
            form = PostForm()
            if request.user.is_active and not  request.user.is_superuser:
                return render(request, 'useractions/create_post.html', {
                    'cod': curruser.account.cod,
                    'form': form})
            else:
                return render(request, 'useractions/create_post.html', {
                    'cod': '61e1380365703a4c73c2480673d8993b',
                    'form': form})
    else:
        return redirect('/login/')


def profile(request):
    if request.user.is_authenticated():
        curruser = request.user
        now = datetime.datetime.now()
        form = ProfileEditForm
        if request.method == 'POST':

            if request.user.is_active and not  request.user.is_superuser:
                    return render(request, 'useractions/profile.html', {
                    'cod': curruser.account.cod,
                    'form': form
                    })
               
            else:
                return render(request, 'useractions/profile.html', { 
                    'cod': 1,
                    'form':form})

        else:
            if request.user.is_active and not  request.user.is_superuser:
                    return render(request, 'useractions/profile.html', {
                        'cod': curruser.account.cod,
                        'form': form, })
            else:
                  return render(request, 'useractions/profile.html',{
                         'cod': '61e1380365703a4c73c2480673d8993b',
                      'form': form })
    else:
        return redirect('/login/')


def category(request, kind):
    if request.user.is_authenticated:
        an = Announcement.objects.filter(category=kind)
        curruser = request.user
        print curruser.account.cod
        if request.user.is_active and not  request.user.is_superuser:
            return render(request, 'useractions/category.html', {
            'categories': ['Garden', 'Moving', 'Cleaning', 'Babysitting', 'Cooking', 'Others'],
            'kind': kind,
            'cod': curruser.account.cod,
            'ann': an
             })
        else: return render(request, 'useractions/category.html', {
            'categories': ['Garden', 'Moving', 'Cleaning', 'Babysitting', 'Cooking', 'Others'],
            'kind': kind,
           'cod': '61e1380365703a4c73c2480673d8993b',
            'ann': an
             })
    else:
        return redirect('/')

def profileGeneral(request):
    return render(request, 'useractions/profilegeneral.html')






def spartan(request):
    if request.user.is_authenticated():
        curruser = request.user
        if request.method == 'POST':
            nume=request.POST.get('nume')
            prenume=request.POST.get('prenume')
            data_nasterii=request.POST.get('Data_nasteri')
            data_nasterii=datetime.datetime.strptime(data_nasterii, '%m/%d/%Y').strftime('%Y-%m-%d')
            adress=request.POST.get('adress')
            cnp=request.POST.get('CNP')
            serie=request.POST.get('serie')
            cui=request.POST.get('cui')
            contBancar=request.POST.get('contBancar')
            abilitate1=request.POST.get('abilitate1')
            abilitate2=request.POST.get('abilitate2')
            abilitate3=request.POST.get('abilitate3')
            spartan = Spartan.objects.create(nume=nume, prenume=prenume, data_nasterii=data_nasterii,
                                            address=adress, cnp=cnp,serie=serie,cui=cui,
                                            contBancar=contBancar,
                                             abilitate1=abilitate1,abilitate2=abilitate2,
                                             abilitate3=abilitate3,
                                            author=request.user)
            spartan.save()
            subject='Activare putere de Spartan'
            messagetip=" Buna % s , \n Ati completat formularul pentru activare puterii de Spartan \n" \
                       " Nume : %s ,\n Prenume: %s \n Data nasterii: %s \n Adresa : %s \n CNP: %s \n Serie: %s \n" \
                       " CUI : %s \n Cont Bancar: %s \n " \
                       "Abilitate 1: %s  \n Abilitate 2: %s \n Abilitate 3:%s \n Datele dvs. vor fi analizate de Admin in vederea Activarii Puterii de Spartan \nO zi buna!"  %(request.user.username,nume,prenume,data_nasterii,adress,cnp,serie,cui,contBancar,abilitate1,abilitate2,abilitate3)
            from_email=settings.EMAIL_HOST_USER
            send_mail(subject, messagetip, from_email,
            [request.user.email], fail_silently=True)
            return render(request, 'useractions/spartan.html' ,{'errors': ['Ati completat cu succes formularul,asteptati confirmarea administratorului!'],
        'cod': request.user.account.cod})
        else:
              if request.user.is_active and not  request.user.is_superuser:
                    return render(request, 'useractions/spartan.html', {'cod': request.user.account.cod})
              else :
                    return render(request, 'useractions/spartan.html', {'cod': 1})
    else:
        return redirect('/login/')


