from django.contrib import admin
from .models import Post

# Register your models here.
# 관리자(admin)가 게시글(Post)에 접근 가능

from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
  pass# 'delete_selected' action을 추가

admin.site.register(Post, PostAdmin)  # PostAdmin 클래스를 사용하여 Post 모델을 등록