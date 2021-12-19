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
from blog.form import CommentForm, InquiryForm , BlogPostForm

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
     詳細ページ 投稿記事の詳細 & Comment入力ページ
     Attributes:
     template_name:レンダリングするテンプレート
     Model:モデルクラス
    '''
    def get(self,request,pk):
        #リクエストパラメータからidを取る
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
        #コメント新規登録
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

class CommentUpdateView(generic.View):
    def get(self,request,comment_blogpost_pk,comment_pk):
        blog = BlogPost.objects.get(pk=comment_blogpost_pk)
        updatemodel = Comment.objects.get(pk=comment_pk)
        update_comment_form = CommentForm(instance=updatemodel)
        param = {'blog':blog ,'comment':updatemodel,'update_comment_form':update_comment_form}
        return render(request,"update_comment.html",param)
    
    def post(self,request,comment_blogpost_pk,comment_pk):
        updatecomment = get_object_or_404(Comment,pk=comment_pk)
        updatedata = CommentForm(request.POST,instance=updatecomment)
        updatedata.blogpost = BlogPost.objects.get(id=comment_blogpost_pk)
        updatedata.comment = self.request.POST.get('comment')
        updatedata.user = self.request.user
        if updatedata.is_valid():
            updatedata.save()

        url = '/blog-detail/'+ str(comment_blogpost_pk)
        return redirect(to=url)

class ArticleView(generic.View):
    template_name = "article.html"

    def get(self,request):
        #新規の処理
        blog_pk = self.request.GET.get('edit_flg')

        if blog_pk == "":        
            form = BlogPostForm()
            type = "new"
        elif blog_pk != "":
            blog = BlogPost.objects.get(pk=blog_pk)
            form = BlogPostForm(instance=blog)
            type = "edit"
        param = {'form':form,"type":type,"form_id":blog_pk}
        return render(request,"article.html",param)

    def post(self,request):
        btn_type = self.request.POST.get('btn_type')

        if(btn_type=="new"):
            blogpost = BlogPost()
            registdata = BlogPostForm(request.POST,blogpost)
            data = registdata.save(commit=False)
            data.user = self.request.user
            data.save()
        
        elif(btn_type=="update"):
            form_id = self.request.POST.get('form_id')
            updateblogpost = get_object_or_404(BlogPost,id=form_id)
            # updateblogpost = BlogPost.objects.get(id=form_id)
            updatedata = BlogPostForm(request.POST,instance=updateblogpost)
            updatedata.title = self.request.POST.get('title')
            updatedata.content = self.request.POST.get('content')
            #本当はuserは入力値じゃないから値の再代入は無駄だけど、null value in column "user_id" violates not-null constraint　エラーを外せない
            #編集画面への遷移には作成者のフィルターをかけてるから一応大丈夫な体
            updatedata.user = self.request.user
            if updatedata.is_valid():
                updatedata.save()

        elif(btn_type=="delete"):
            form_id = self.request.POST.get('form_id')
            blogpost = BlogPost.objects.filter(pk=form_id)
            blogpost.delete()


        url = '/blog'
        return redirect(to=url)

class TableView(generic.TemplateView):
    template_name = "table.html"