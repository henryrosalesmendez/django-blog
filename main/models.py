
from django.contrib.auth.models import User
from django.db import models
import uuid


class Tag(models.Model):

    ######################################
    # Constants
    ######################################
    TAG_MAX_LENGTH = 255

    ######################################
    name = models.CharField(
        max_length=TAG_MAX_LENGTH,
        verbose_name="Tag",
        help_text="tag",
    )
    
    def __str__(self) -> str:
        return self.name



class Article(models.Model):
    """
    Model for storing the

    """

    ######################################
    # Constants
    ######################################

    NAME_MAX_LENGTH = 255
    ADDRESS_MAX_LENGTH = 255

    ######################################

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name="ID",
        help_text="Unique identifier for an article.",
    )

    title = models.CharField(
        max_length=NAME_MAX_LENGTH,
        verbose_name="Title",
        help_text="Title of the article",
    )

    slug = models.SlugField(default="", null=False)
    template_filename = models.TextField(null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    reading_minutes = models.IntegerField(default=3)
    public = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True)

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name="Created at",
        help_text="Date and time when the record was created.",
    )

    created_by = models.ForeignKey(
        to=User,
        on_delete=models.PROTECT,
        related_name="+",
        verbose_name="Created by",
        help_text="User who created this record.",
        null=True,
        blank=True
    )

    def __str__(self) -> str:
        return self.title



