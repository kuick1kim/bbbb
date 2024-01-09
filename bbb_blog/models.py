from django.db import models
from django.urls import reverse
from django.conf import settings  # 추가
import os

# Create your models here. #글의 분류(일상, 유머, 정보)
class Category (models.Model):
    name = models.CharField(max_length=50, blank=False, help_text= "블로그 글의 분류를 입력하세요(ex:일상)")

    def __str__(self):
        return self.name

    

#블로그 글(제목, 작성일, 대표 이미지, 내용, 분류)
class Post (models.Model):
    title = models.CharField(max_length=200)
    title_image = models.ImageField(blank=True, upload_to='media')
    content = models.TextField()
    createDate = models.DateTimeField(auto_now_add=True) 
    updateDate = models.DateTimeField(auto_now_add=True) 
    #히나의 글을 여러가지의 분류에 해당될 수 있다. (ex: 정보, 유머), 히나의 분류에는 여러가지 글이 포함될 수 있죠. (정보 카테고리에 글 10개) 
    category = models.ManyToManyField(Category, help_text="20 글의 분류를 설정하세요")
    def __str__(self):
        return self.title
    
    #1번 글의 경우 -> post/1
    def get_absolute_url(self):
        return reverse("post", args=[str(self.id)])
    
    def get_absolute_url2(self):
        return reverse("post", args=[str(self.id)])    

    def get_absolute_url3(self):
        # print(os.path.join(settings.MEDIA_ROOT, self.title_image.name))
        # os.remove(os.path.join(settings.MEDIA_ROOT, self.title_image.name))
        
        return reverse("remove_post", args=[str(self.id)])    
    
    
    def change_title(self):            
        text = str(self.title)
        if len(text) <= 38:
            text = text.ljust(100)
            text = text.replace(' ', '-')
        return text[:38]
    
    def change_content(self):            
        text = str(self.content)
        if len(text) <= 130:
            text = text.ljust(130)
            text = text.replace(' ', '-')
        return text[:120]
    

