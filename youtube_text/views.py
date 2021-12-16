from django.forms import forms
from django.shortcuts import redirect, render
from django.views import generic
from django.urls import reverse_lazy
from django.conf import settings
from django.contrib import messages
from newsapi import NewsApiClient
from .forms import SearchLogForm
from .models import SearchLog
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from . import youtube_text

# Create your views here.


class IndexView(generic.View):
    def get(self,request):
        params = {"message":"クラスベースView：Get処理"}
        return render(request,"Index.html",params)

    #　titleからpostでconfirmにいく必要がなくなったのでコメントアウト
    # def post(self,request):
    #     '''イメージとしては、ここから動画ページを出して、この動画の文字起こしのテキストを取得しますか？って聞く
    #         やっぱりview関数じゃなくてクラス作りたいな。ふつうのtemplateviewでいいのと
    #         youtube画面を開くっていう処理がいるよね　んーtemplateにしないといけんかな。
    #     '''
    #     link = request.POST['input_link']
    #     params = {"url":request.POST['input_link']}
    #     print("Post通った" + link)
    #     return render(request,"confirm.html",params)

class LogListView(generic.ListView):
    template_name = 'log_list.html'
    # モデルBlogPostのオブジェクトにorder_by()を適用して
    # 投稿日時の降順で並べ替える
    queryset = SearchLog.objects.order_by('-search_date')
    #1ページに表示するレコードの件数
    #paginate_by = 9

@method_decorator(login_required, name='dispatch')
class Scraping(generic.CreateView):
    '''
        スクレイピング実行するクラス
        結果をresultで表示する
        titleから遷移してきたら、confirmを開く
        confirmでFormnを展開をして登録処理
    '''
    model = SearchLog
    form_class = SearchLogForm
    template_name = "confirm.html"
    success_url = reverse_lazy('youtube_text:result')    

    '''CreateViewクラスのform_valid()をオーバーライド
        フォームのバリデーションを通過したときに呼ばれる
        フォームデータの登録をここで行う
        parameters:
          form(django.forms.Form):
            form_classに格納されているSearchFormオブジェクト
        Return:
          HttpResponseRedirectオブジェクト:
            スーパークラスのform_valid()の戻り値を返すことで、
            success_urlで設定されているURLにリダイレクトさせる
    '''
    def form_valid(self, form):
        registdata = form.save(commit=False)
        #URLを取得 画面からでいいか いらないらしい。
        url = self.request.POST.get('url')
        
        #スクレイピング処理
        result = youtube_text.scraping(url)
        print("scraping成功" + result[0] + ":" + result[1])
        registdata.title = result[0]
        registdata.result = result[1]
        #ユーザをリクエストのIDを持ってきて登録する
        registdata.user = self.request.user
        registdata.save()
        #ここのメッセージ処理どっちかに統一したいな
        messages.success(self.request,'取得完了しました。')
        params = {"result":result}
        return render(self.request,"result.html",params)
        #return super().form_valid(form)

    def form_invalid(self, form):
        # print(form.errors)
        # params = {"messages":form.errors}
        # return render(self.request,"confirm.html",params)
        return super().form_invalid(form)

class NewsListView(generic.TemplateView):
  '''
   newsの一覧を作成するぜ
  '''
  template_name = "news_list.html"

  def get_context_data(self, **kwargs):
        news = super(NewsListView, self).get_context_data(**kwargs)
        newsapi = NewsApiClient(api_key=settings.NEWSAPI)
        news['top_headlines'] = newsapi.get_top_headlines(language=None,country='jp')
        #print(news['top_headlines'])
        return news

class ResultView(generic.TemplateView):
    #スクレイピング完了ページ
    template_name = "result.html"

class DetailView(generic.DetailView):
    #詳細ページ
    template_name = 'detail.html'
    model = SearchLog
