from django.db import models


class CommonModel(models.Model):
    # 데이터 생성시간기준 변경 불가
    created_at = models.DateTimeField(auto_now_add=True)
    # 데이터 생성시간기준 데이터 수정시 수정시간 기준으로 변동 
    updated_at = models.DateTimeField(auto_now=True)

# DB 테이블에 추가 안되도록 정의
class Meta:
    abstract = True