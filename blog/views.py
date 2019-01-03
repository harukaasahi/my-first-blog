from django.shortcuts import render
from django.utils import timezone
from .models import Post
#.modelsはこのviews.pyと同じディレクトリないにある models.pyのことを指す.
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
#post_list関数の定義.Postモデルからブログの記事を取り出してそのリストをテンプレートに渡す.
#requestを引数にとり、クエリセットのデータをpostsで参照する.
#それらの情報をrender関数でpost_list.htmlに組み込む.
#引数の名前が'posts'、クエリセットで参照した引数の値がposts.

#ブラウザはHTMLしか理解できないが、HTMLだけでは静的なページしか書けない.
#でもpythonを用いれば動的なページも書ける.Djangoを使えばHTMLにPythonのコードを埋め込むことが可能.

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        #request.POSTに追加された"フォームのデータ"を使ってPostFormを構築する
        if form.is_valid():
        #全フォームの値が有効かチェック.有効だったら保存する
            post = form.save(commit=False)
            #まだ保存していないモデルを変数postに格納
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
            #post_detailに変数pkを渡す
    else:
        form = PostForm()
        #空白のフォームを用意する
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    #編集したい Postモデルを変数postに格納
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        #postをinstanceで渡す
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
        #投稿を編集するためにフォームを開く
    return render(request, 'blog/post_edit.html', {'form': form})
