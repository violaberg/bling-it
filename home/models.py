from django.db import models


class FAQ(models.Model):
    """
    Model representing Frequently Asked Questions (FAQs).
    
    Attributes:
        question (CharField): The question being asked.
        answer (TextField): The detailed answer to the question.
    """

    class Meta:
        """
        Customizes the display name of the category in the admin panel.
        """
        verbose_name_plural = 'Frequently Asked Questions'

    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question


class NewsletterSubscriber(models.Model):
    """
    Model representing Newsletter Subscribers.
    
    Attributes:
        email (EmailField): The email address of the subscriber.
        timestamp (DateTimeField): The timestamp when the subscriber was added.
    """
    email = models.EmailField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
