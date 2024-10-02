from django.db import models


class CommonModel(models.Model):
    """Common Model Definition"""

    created_at = models.DateTimeField(
        auto_now_add=True
    )  # Object 생성시 시간을 넣는다 auto_now_add
    updated_at = models.DateTimeField(
        auto_now=True
    )  # auto_now object가 저장될 때마다 시간 넣기

    class Meta:
        abstract = True
