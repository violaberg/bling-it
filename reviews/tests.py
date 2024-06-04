from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Review

class ReviewsPageTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.reviews_url = reverse('reviews')

    def test_reviews_page_loads_properly(self):
        response = self.client.get(self.reviews_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/reviews.html')

    def test_reviews_post_method(self):
        data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'review_subject': 'Test Review',
            'review_body': 'This is a test review.',
            'rating': 5
        }
        response = self.client.post(self.reviews_url, data)
        self.assertEqual(response.status_code, 302)  # Redirects after successful POST
        self.assertTrue(Review.objects.filter(review_subject='Test Review').exists())

    def test_delete_review(self):
        review = Review.objects.create(
            name='Test User',
            email='test@example.com',
            review_subject='Test Review',
            review_body='This is a test review.',
            rating=5
        )
        delete_url = reverse('delete_review', args=[review.id])
        response = self.client.get(delete_url)
        self.assertEqual(response.status_code, 302)  # Redirects after successful DELETE
        self.assertFalse(Review.objects.filter(id=review.id).exists())
