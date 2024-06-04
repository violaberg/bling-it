from django.test import TestCase, Client
from django.urls import reverse
from .models import Contact


class ContactPageTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.contact_url = reverse('contact')

    def test_contact_page_loads_properly(self):
        response = self.client.get(self.contact_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')

    def test_contact_form_submission(self):
        data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'subject': 'Test Subject',
            'message': 'Test Message'
        }
        response = self.client.post(self.contact_url, data)
        self.assertEqual(response.status_code, 302)
        # Check if contact object was created
        self.assertTrue(Contact.objects.filter(email=data['email']).exists())

    def test_invalid_contact_form_submission(self):
        # Submitting an empty form
        response = self.client.post(self.contact_url, {})
        self.assertEqual(response.status_code, 200)

        # Check if no contact object was created
        self.assertFalse(Contact.objects.exists())

    def test_contact_success_page_loads_properly(self):
        response = self.client.get(reverse('contact_success'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact_success.html')
