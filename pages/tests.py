from django.test import SimpleTestCase
from django.urls import reverse, resolve
# Create your tests here.
from .views import HomePageView


class HomepageTests(SimpleTestCase):
    def setUp(self):
        url = reverse("home")
        self.response = self.client.get(url)


    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.status_code, 200)


    def test_homepage_template(self):
        self.assertTemplateUsed(self, "home.html")

    def test_homepage_contains_correct_html(self):
        self.assertContains(self, "home page")

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self, "Hi there! I should not be on teh page.")

    def test_homepage_url_resolves_homepageview(self):
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)