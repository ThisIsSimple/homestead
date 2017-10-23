from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Post, Board

# content


# views
def board_list(request):
    boards = Board.objects.all()

    content = {
        'boards' : boards
    }

    return render(request, 'board/board_list.html', content)

def post_list(request, board_name):
    board = get_object_or_404(Board, name=board_name)
    posts = Post.objects.filter(board_id=board.id).order_by('created_at').reverse()[:12]
    # posts = get_object_or_404(Post, board_id = board.id)

    content = {
        'posts': posts,
        'board': board
    }

    return render(request, 'board/post_list.html', content)


def post_detail(request, board_name, post_id):
    board = get_object_or_404(Board, name=board_name)
    post = Post.objects.filter(board_id=board.id, id=post_id)

    content = {
        'post': post[0],
        'board': board
    }

    return render(request, 'board/post_detail.html', content)

def post_create(request, board_name):
    board = get_object_or_404(Board, name=board_name)

    content = {
        'board' : board
    }

    return render(request, 'board/post_create.html', content)
