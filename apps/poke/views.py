# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from models import *
from django.contrib import messages
import bcrypt
from django.contrib.sessions.models import Session


def index(request):
    return render(request, "poke/index.html")

def process(request):
    print request.POST
    errors = User.objects.validator(request.POST)
    if errors:
        for error in errors:
            print errors[error]
            messages.error(request, errors[error])
        return redirect('/')
    else:
        hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user = User.objects.create(name = request.POST['name'], alias = request.POST['alias'], email = request.POST['email'], password = hashed_pw, dob = request.POST['date'])
        request.session['id'] = user.id
        messages.success(request, "You have successfully registered")
    return redirect('/pokes')

def login(request):
    login_return = User.objects.login(request.POST)
    if 'user' in login_return:
        request.session['id'] = login_return['user'].id
        messages.success(request, "You have successfully logged in")
        return redirect('/pokes')
    else:
        messages.error(request, login_return['error'])
    return redirect('/')

def logout(request):
    Session.objects.all().delete()
    return redirect('/')

def pokes(request):
    context = {
        "user": User.objects.get(id=request.session['id']),
        "users_list": User.objects.all().exclude(id=request.session['id'])
    }

    return render(request, "poke/pokes.html", context)

def create_poke(request, user_id):
    sender_id = user_id
    receiver_id = User.objects.all().exclude(id=request.session['id'])

    send_user = User.objects.get(id=sender_id)
    receive_user = User.objects.get(id=receiver_id)
    # send_user.pokee.add(receive_user)
    return redirect('/pokes')