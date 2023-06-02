from django.db import models
#accountsアプリのmodelsモジュールからCustomUserをインポート
from accounts.models import CustomUser

class Category(models.Model):
#投稿する写真のカテゴリを管理するモデル
#カテゴリ名のフィールド
   title = models.CharField(
      verbose_name='カテゴリ',#フィールドのタイトル
      max_length=20)
 
def __str__(self):
    #オブジェクトを文字列に変換して返す
    #Returns(str):カテゴリ名
    return self.title

class PhotoPost(models.Model):
    '''投稿されたデータを管理するモデル
    '''
    #CustomUserモデル(のuser_id)とphotoPostモデルを
    #1対多の関係で結び付ける
    #CustomUserが親でPhotoPostが子の関係となる
    user = models.ForeignKey(
        CustomUser,
        #フィールドのタイトル
        verbose_name='ユーザー',
        #カテゴリに関連付けられた投稿データが存在する場合は
        #そのカテゴリを削除できないようにする
        on_delete=models.CASCADE
    )
    #Categoryモデル(のtitle)とPhotoPostモデルを
    #1対多の関係で結び付ける
    #Categoryが親でPhotoPostが子の関係となる
    category = models.ForeignKey(
       Category,
       #フィールドのタイトル
       verbose_name='カテゴリ',
       #カテゴリに関連付けられた投稿データが存在する場合は
       #そのカテゴリを削除できないようにする
       on_delete=models.PROTECT
    )
    #タイトル用のフィールド
    title = models.CharField(
       verbose_name='タイトル',#フィールドのタイトル
       max_length=200 #最大文字数は200
        )

    comment = models.TextField(
       verbose_name='コメント',
        )
    image1 = models.ImageField(
       verbose_name='イメージ１',
       upload_to = 'photos', 
        )
    image2 = models.ImageField(
       verbose_name='イメージ２',
       upload_to = 'photos',
       blank=True,
       null=True
       )
    posted_at = models.DateTimeField(
       verbose_name='投稿日時',
       auto_now_add=True
       )
    def __str__(self):
       

       return self.title

# Create your models here.
