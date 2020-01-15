from django.contrib.auth.models import AbstractUser

from django.db import models


class User(AbstractUser):

    """ Custom User Model """

    # 성별 변수
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    # 언어 변수
    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"
    LANGUAGE_JAPANESE = "jp"

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_KOREAN, "한국어"),
        (LANGUAGE_JAPANESE, "日本語"),
    )

    # 통화 변수
    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"
    CURRENCY_JPY = "jpy"

    CURRENCY_CHOICES = (
        (CURRENCY_USD, "USD"),
        (CURRENCY_KRW, "KRW"),
        (CURRENCY_JPY, "JPY"),
    )

    # 모델 선언부
    avatar = models.ImageField(blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10)
    bio = models.TextField(blank=True)
    birthdate = models.DateField(null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, blank=True, max_length=2)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, blank=True)
    superhost = models.BooleanField(default=False)
