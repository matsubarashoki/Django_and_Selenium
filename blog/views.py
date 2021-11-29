from re import template
from typing import List
from django.http import Http404
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.views import generic
from blog.models import BlogPost,Comment
from blog.form import CommentForm
# Create your views here.

class BlogView(generic.ListView):
    '''
        Blog Topページ
        登録済みの記事を一覧で見せる
        Attributes:
            template_name: レンダリングするテンプレート
            context_object_name:object_listキーの別名を設定
            queryset:データベースのクエリ
    '''

    template_name = 'blog.html'
    # object_listキーの別名を設定
    context_object_name = 'orderby_records'
    # モデルBlogPostのオブジェクトにorder_by()を適用して
    # BlogPostのレコードを投稿日時の降順で並べ替える
    queryset = BlogPost.objects.order_by('-posted_at')

#DetailViewを継承して詳細ページのレンダリング
class BlogArticle(generic.View):
    '''　
    　詳細ページ　投稿記事の詳細 & Comment入力ページ
    　Attributes:
    　　template_name:レンダリングするテンプレート
        Model:モデルクラス
    '''
    def get(self,request,pk):
        #リクエストパラメータからidを取る
        #取ったidでquery生成＆取得
        #コメントformのform生成
        pk = self.kwargs.get('pk')
        if not "pk" == "":
            blog = BlogPost.objects.get(pk=pk)
            #記事に紐づくコメントを取得
            comments = blog.comments.all().order_by('id')
            #コメント追加用Form生成
            form = CommentForm()
            param = {'form':form,'object':blog,'comments':comments}
            return render(request,"post.html",param)
        else:
           raise Http404("存在しません。")

    def post(self,request,pk):
        #POSTされた request　データからフォームを作成　空のModelを渡す
        comment = Comment()
        registdata = CommentForm(request.POST,comment)
        data = registdata.save(commit=False)
        pk= self.kwargs.get('pk')
        data.blogpost = BlogPost.objects.get(pk=pk)
        data.comment = request.POST.get('comment')
        data.user = self.request.user
        print(data)
        data.save()
        
        #return render(request,"post.html")
        url = '/blog-detail/'+ str(pk)
        return redirect(to=url)