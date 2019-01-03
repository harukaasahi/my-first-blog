from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    #formsをインポート.そしてこのクラスがModelFormの一種であることを宣言
    class Meta:
        model = Post
        #フォームを作るときはPostのモデルを使用する
        fields = ('title', 'text',)
        #フォームに書くものを宣言
    