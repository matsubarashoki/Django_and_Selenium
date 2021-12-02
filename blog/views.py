import logging
from re import template
from typing import List
from django.contrib.messages.api import success
from django.db.models import query
from django.http import Http404
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic
from django.contrib import messages
from django.urls import reverse_lazy
from blog import models
from blog.models import BlogPost,Comment
from blog.form import CommentForm, InquiryForm

logger = logging.getLogger(__name__)

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

#
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
            param = {'form':form,'blog':blog,'comments':comments}
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

class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('blog:inquiry')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました。')
        logger.info('Inquiry send by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)

class CommentDeleteView(generic.View):
    model = Comment

    def get(self,request):
        pass
    
    def post(self,request,comment_blogpost_pk,comment_pk):
        comment = Comment.objects.filter(pk=comment_pk)
        comment.delete()

        url = '/blog-detail/'+ str(comment_blogpost_pk)
        return redirect(to=url)