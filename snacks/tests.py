from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.
class SnacksTestCase(SimpleTestCase):

    # test home url status code
    def test_home_page_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    # test about url status code
    def test_about_page_status_code(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    # test home url template including ancestor template
    def test_home_page_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, '_base.html')

    # test about url template including ancestor template
    def test_about_page_template(self):
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, 'about.html')
        self.assertTemplateUsed(response, '_base.html')

        