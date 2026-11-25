from django.db import models
from datetime import date
from django.core.validators import MaxValueValidator, MinValueValidator

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    pages = models.PositiveIntegerField(null=True, blank=True)
    published_year = models.PositiveSmallIntegerField(null=True, blank=True)

    class Meta:
        ordering = ["title"]
        constraints = [
            models.UniqueConstraint(
                fields=["title", "author"], name="unique_book_title_author"
            )
        ]

    def __str__(self):
        return f"{self.title} by {self.author}"


class ReadingLog(models.Model):
    member = models.ForeignKey(
        "Member", on_delete=models.CASCADE, related_name="readings"
    )
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="readings"
    )
    date_finished = models.DateField(default=date.today)

    class Meta:
        ordering = ["-date_finished"]
        constraints = [
            models.UniqueConstraint(
                fields=["member", "book"], name="unique_member_book"
            )
        ]

    def __str__(self):
        return f"{self.member} read {self.book}"

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  email = models.CharField(max_length=255, null=True)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)
  favorite_book = models.CharField(max_length=255, blank=True)

  def __str__(self):
    return f"{self.firstname} {self.lastname}"