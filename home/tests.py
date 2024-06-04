from django.core import mail
from django.test import TestCase, Client
from unittest.mock import patch
from django.urls import reverse
from .models import FAQ, NewsletterSubscriber
from .views import send_subscription_email


class HomeViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.index_url = reverse('home')
        self.faq_url = reverse('faq')

    def test_send_subscription_email(self):
        user_email = 'test@example.com'
        send_subscription_email(user_email)

        # Check if the email was sent successfully
        self.assertEqual(len(mail.outbox), 1)
        sent_email = mail.outbox[0]
        
        # Assert email contents
        self.assertEqual(sent_email.subject, 'Subscription Confirmation')
        self.assertIn('Thank you for subscribing to our newsletter!', sent_email.body)
        self.assertEqual(sent_email.from_email, 'viola.bergere@gmail.com')
        self.assertEqual(sent_email.recipients(), ['test@example.com'])
