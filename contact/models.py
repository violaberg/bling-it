from django.db import models


class Contact(models.Model):
    """
    Represents a contact form submission.

    Attributes:
        name (str): The name of the person who submitted the contact form.
        email (str): The email address of the person \
        who submitted the contact form.
        subject (str): The subject of the contact form message.
        message (str): The content of the contact form message.
        timestamp (datetime): The date and time when \
        the contact form was submitted.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
