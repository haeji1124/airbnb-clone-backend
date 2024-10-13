from django.db import models
from common.models import CommonModel


class Photo(CommonModel):
    # file = models.ImageField()
    file = models.URLField()
    description = models.CharField(
        max_length=140,
    )
    room = models.ForeignKey(
        "rooms.Room",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="photos",
    )
    experience = models.ForeignKey(
        "experiences.Experience",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="photos",
    )

    def __str__(self):
        return "Photo File"


class Video(CommonModel):
    # file = models.FileField()
    file = models.URLField()
    experience = models.OneToOneField(
        # foreignKey와 비슷한데, 이 동영상이 하나의 활동과 연결되면
        # 그 활동은 다른 동영상을 가질수 없게 된다.
        "experiences.Experience",
        on_delete=models.CASCADE,
        related_name="videos",
    )

    def __str__(self):
        return "Video File"
