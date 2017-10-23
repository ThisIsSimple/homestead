from django.utils.crypto import get_random_string
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
import json

from .models import Member
from plant.models import Plant
from board.models import Board

def login(request):
    if(request.method=="POST"):
        email = request.POST['email']
        password = request.POST['password']

        try:
            member = Member.objects.get(email=email, password=password)
            content = json.dumps({"status":"success", "msg":"Login Success", "email":member.email, "code":member.code})
            request.session['logged_in'] = True
            request.session['member_id'] = member.id
            request.session['member_name'] = member.name
            request.session['member_email'] = member.email
            request.session['member_code'] = member.code
        except Member.DoesNotExist:
            content = json.dumps({"status":"fail", "msg":"Member Does Not Exist"})
            request.session['logged_in'] = False

        return HttpResponse(content)
    else:
        if request.session.get('logged_in', True):
            return redirect('/')
        else:
            return render(request, 'login/login.html')

def logout(request):
    try:
        request.session['logged_in'] = False
    except KeyError:
        pass
    return redirect('/')

def register(request):
    if (request.method == "POST"):
        email = request.POST['email']
        password = request.POST['password']
        name = request.POST['name']

        try:
            member1 = Member.objects.get(email=email)
            content = json.dumps({"status":"fail", "msg":"Email Already Taken"})
        except Member.DoesNotExist:
            content = json.dumps({"status":"success", "msg":"Register Success"})
            while True:
                code = get_random_string(length=32)
                try:
                    member2 = Member.objects.get(code=code)
                    continue
                except Member.DoesNotExist:
                    register = Member(name=name, password=password, email=email, code=code)
                    register.save()
                    break

        return HttpResponse(content)
    else:
        return render(request, 'login/register.html')

def dashboard(request, member_code):
    content = get_content(member_code)

    return render(request, 'member/dashboard.html', content)

def profile(request, member_code):
    content = get_content(member_code)

    return render(request, 'member/profile.html', content)

def plants(request, member_code):
    content = get_content(member_code)
    content['plants'] = Plant.objects.all()

    return render(request, 'plants/plants.html', content)

# Content
def get_content(member_code):
    content = {
        'member' : get_object_or_404(Member, code=member_code),
        'boards' : Board.objects.all()
    }
    return content