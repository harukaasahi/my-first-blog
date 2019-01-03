from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
#.modelsはこのviews.pyと同じディレクトリないにある models.pyのことを指す.

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
