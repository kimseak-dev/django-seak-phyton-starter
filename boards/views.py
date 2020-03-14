# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import Board, Topic, Post
from .forms import NewTopicForm

def about(request):
    # do something...
    return render(request, 'about.html')

def about_company(request):
    # do something else...
    # return some data along with the view...
    return render(request, 'about_company.html', {'company_name': 'Simple Complex'})

def about_author(request):
    # do something else...
    # return some data along with the view...
    return render(request, 'about_author.html', {'author_name': 'PHON KIMSEAK'})  

def about_vitor(request):
    # do something else...
    # return some data along with the view...
    return render(request, 'about_vitor.html', {'author_name': 'PHON KIMSEAK'})    

def about_erica(request):
    # do something else...
    # return some data along with the view...
    return render(request, 'about_erica.html', {'author_name': 'PHON KIMSEAK'}) 

def privacy_policy(request):
    # do something else...
    # return some data along with the view...
    return render(request, 'privacy_policy.html')      

def board_topics(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404
    return render(request, 'topics.html', {'board': board})


def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})

def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    user = User.objects.first()  # TODO: get the currently logged in user
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=user
            )
            return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', {'board': board, 'form': form})