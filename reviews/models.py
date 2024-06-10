from django.db import models


RATING = (
    (1,  "★☆☆☆☆"),
    (2,  "★★☆☆☆"),
    (3,  "★★★☆☆"),
    (4,  "★★★★☆"),
    (5,  "★★★★★"),
)


class Review(models.Model):
    """
    Model representing a review left by a user.

    Each review consists of a \
    name, email, subject, body, rating, and creation date.

    def__str__(self): Returns a string representation of the Review object \
    and the name of the reviewer.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    review_subject = models.CharField(max_length=100)
    review_body = models.TextField()
    rating = models.IntegerField(choices=RATING, default=None)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'

    @property
    def get_rating_range(self):
        """
        Return range of the review rating.

        Returns:
            range: A range representing the rating.
        """
        return range(self.rating or 1)
