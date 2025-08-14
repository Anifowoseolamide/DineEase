from django.test import TestCase
from django.urls import reverse
from .models import RestaurantInfo, About, Gallery

# Create your tests here.

class CoreViewsTest(TestCase):
    def setUp(self):
        # Create test data
        self.restaurant_info = RestaurantInfo.objects.create(
            name="Test Restaurant",
            tagline="Test Tagline",
            description="Test Description",
            address="123 Test St",
            phone="555-1234",
            email="test@test.com",
            hours="Mon-Fri: 9-5"
        )
        
        self.about_content = About.objects.create(
            title="About Us",
            content="Test content about the restaurant"
        )
        
        self.gallery_image = Gallery.objects.create(
            title="Test Image",
            image="test.jpg",
            caption="Test caption"
        )

    def test_home_view(self):
        response = self.client.get(reverse('core:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/index.html')
        self.assertContains(response, "Test Restaurant")

    def test_about_view(self):
        response = self.client.get(reverse('core:about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/about.html')
        self.assertContains(response, "About Us")

    def test_gallery_view(self):
        response = self.client.get(reverse('core:gallery'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/gallery.html')
        self.assertContains(response, "Test Image")

class CoreModelsTest(TestCase):
    def test_restaurant_info_str(self):
        restaurant = RestaurantInfo.objects.create(
            name="Test Restaurant",
            description="Test Description",
            address="123 Test St",
            phone="555-1234",
            email="test@test.com",
            hours="Mon-Fri: 9-5"
        )
        self.assertEqual(str(restaurant), "Test Restaurant")

    def test_about_str(self):
        about = About.objects.create(
            title="About Us",
            content="Test content"
        )
        self.assertEqual(str(about), "About Us")

    def test_gallery_str(self):
        gallery = Gallery.objects.create(
            title="Test Image",
            image="test.jpg"
        )
        self.assertEqual(str(gallery), "Test Image")
