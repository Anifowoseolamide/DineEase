#!/usr/bin/env python3
"""
Setup script for DineEase Restaurant Website
This script helps set up the initial database and create sample data
"""

import os
import sys
import django
from django.core.management import execute_from_command_line

def setup_database():
    """Set up the database and create initial data"""
    print("Setting up DineEase Restaurant Website...")
    
    # Set up Django environment
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant_site.settings')
    django.setup()
    
    # Import models after Django setup
    from django.contrib.auth.models import User
    from core.models import RestaurantInfo, About, Gallery
    from menu.models import Category, MenuItem
    from django.core.files.uploadedfile import SimpleUploadedFile
    
    print("Creating superuser...")
    try:
        # Create superuser if it doesn't exist
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@dineease.com', 'admin123')
            print("Superuser created: admin/admin123")
        else:
            print("Superuser already exists")
    except Exception as e:
        print(f"Error creating superuser: {e}")
    
    print("Creating sample restaurant information...")
    try:
        # Create restaurant info if it doesn't exist
        if not RestaurantInfo.objects.exists():
            RestaurantInfo.objects.create(
                name="DineEase Restaurant",
                tagline="Where Every Bite Tells a Story",
                description="Welcome to DineEase, where culinary excellence meets warm hospitality. Our passionate chefs create memorable dining experiences using the finest ingredients and innovative techniques. From intimate dinners to family celebrations, we provide the perfect setting for every occasion.",
                address="123 Gourmet Street\nCulinary District, Food City, FC 12345",
                phone="(555) 123-4567",
                email="info@dineease.com",
                hours="Monday - Thursday: 11:00 AM - 10:00 PM\nFriday - Saturday: 11:00 AM - 11:00 PM\nSunday: 12:00 PM - 9:00 PM"
            )
            print("Restaurant information created")
        else:
            print("Restaurant information already exists")
    except Exception as e:
        print(f"Error creating restaurant info: {e}")
    
    print("Creating sample about content...")
    try:
        if not About.objects.exists():
            About.objects.create(
                title="Our Story",
                content="Founded in 2024, DineEase began as a dream to create a restaurant that would not only serve exceptional food but also provide an unforgettable dining experience. Our founder, Chef Michael, envisioned a place where guests could escape the ordinary and indulge in extraordinary flavors.\n\nEvery dish at DineEase is crafted with passion, using locally sourced ingredients and traditional cooking methods combined with modern culinary innovation. We believe that great food has the power to bring people together, create memories, and transform ordinary moments into extraordinary experiences.\n\nOur commitment to excellence extends beyond the kitchen. From our warm and attentive service to our carefully curated wine list and elegant atmosphere, every detail is designed to ensure your visit is nothing short of perfect."
            )
            print("About content created")
        else:
            print("About content already exists")
    except Exception as e:
        print(f"Error creating about content: {e}")
    
    print("Creating sample menu categories...")
    try:
        # Create menu categories
        categories_data = [
            {"name": "Appetizers", "description": "Start your meal with our carefully crafted appetizers", "order": 1},
            {"name": "Main Courses", "description": "Our signature dishes featuring premium ingredients", "order": 2},
            {"name": "Desserts", "description": "Sweet endings to perfect meals", "order": 3},
            {"name": "Beverages", "description": "Compliment your meal with our selection of drinks", "order": 4},
        ]
        
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data["name"],
                defaults=cat_data
            )
            if created:
                print(f"Category '{category.name}' created")
        
        print("Menu categories created")
    except Exception as e:
        print(f"Error creating menu categories: {e}")
    
    print("Creating sample menu items...")
    try:
        # Get categories
        appetizers = Category.objects.get(name="Appetizers")
        main_courses = Category.objects.get(name="Main Courses")
        desserts = Category.objects.get(name="Desserts")
        beverages = Category.objects.get(name="Beverages")
        
        # Sample menu items
        menu_items_data = [
            {
                "name": "Bruschetta al Pomodoro",
                "description": "Toasted artisan bread topped with fresh tomatoes, basil, and extra virgin olive oil",
                "price": "12.99",
                "category": appetizers,
                "is_vegetarian": True,
                "is_popular": True
            },
            {
                "name": "Grilled Salmon",
                "description": "Fresh Atlantic salmon grilled to perfection with seasonal vegetables and lemon butter sauce",
                "price": "28.99",
                "category": main_courses,
                "is_gluten_free": True,
                "is_popular": True
            },
            {
                "name": "Beef Tenderloin",
                "description": "Premium cut beef tenderloin with roasted potatoes and red wine reduction",
                "price": "34.99",
                "category": main_courses,
                "is_popular": True
            },
            {
                "name": "Tiramisu",
                "description": "Classic Italian dessert with layers of coffee-soaked ladyfingers and mascarpone cream",
                "price": "14.99",
                "category": desserts,
                "is_vegetarian": True
            },
            {
                "name": "Fresh Fruit Smoothie",
                "description": "Blend of seasonal fruits with yogurt and honey",
                "price": "8.99",
                "category": beverages,
                "is_vegetarian": True,
                "is_gluten_free": True
            }
        ]
        
        for item_data in menu_items_data:
            menu_item, created = MenuItem.objects.get_or_create(
                name=item_data["name"],
                defaults=item_data
            )
            if created:
                print(f"Menu item '{menu_item.name}' created")
        
        print("Sample menu items created")
    except Exception as e:
        print(f"Error creating menu items: {e}")
    
    print("Setup completed successfully!")
    print("\nNext steps:")
    print("1. Run: python manage.py runserver")
    print("2. Visit: http://127.0.0.1:8000/")
    print("3. Admin panel: http://127.0.0.1:8000/admin/")
    print("4. Login with: admin/admin123")

if __name__ == "__main__":
    setup_database()
