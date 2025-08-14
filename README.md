# DineEase Restaurant Website

A modern, responsive restaurant website built with Django and PostgreSQL, featuring online reservations, menu management, and a beautiful user interface.

## Features

- **Responsive Design**: Mobile-first design using Bootstrap 5
- **Online Reservations**: Easy table booking system with validation
- **Menu Management**: Dynamic menu with categories and dietary information
- **Photo Gallery**: Beautiful image showcase with lightbox effects
- **Contact Forms**: Multiple contact options for customer inquiries
- **Admin Panel**: Comprehensive Django admin for content management
- **Modern UI/UX**: Clean, professional design with smooth animations

## Technology Stack

- **Backend**: Django 5.2.5
- **Database**: PostgreSQL
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript
- **Forms**: Django Crispy Forms with Bootstrap styling
- **Image Handling**: Pillow for image processing
- **Environment**: python-decouple for configuration management

## Project Structure

```
restaurant_site/
├── manage.py
├── requirements.txt
├── .env
├── .gitignore
├── restaurant_site/          # Main project settings
├── core/                     # Core functionality (home, about, gallery)
├── menu/                     # Menu management
├── reservations/             # Table booking system
├── contact/                  # Contact forms
├── static/                   # CSS, JS, and images
├── media/                    # User-uploaded content
└── templates/                # HTML templates
```

## Installation

### Prerequisites

- Python 3.8+
- PostgreSQL
- pip

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd restaurant_site
   ```

2. **Create and activate virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up PostgreSQL database**
   ```bash
   # Create database and user
   createdb dineease_db
   createuser dineease_user
   psql -d dineease_db -c "ALTER USER dineease_user WITH PASSWORD 'dineease_password';"
   psql -d dineease_db -c "GRANT ALL PRIVILEGES ON DATABASE dineease_db TO dineease_user;"
   ```

5. **Configure environment variables**
   ```bash
   # Copy and edit .env file
   cp .env.example .env
   # Edit .env with your actual database credentials and secret key
   ```

6. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

8. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

9. **Run the development server**
   ```bash
   python manage.py runserver
   ```

10. **Access the website**
    - Main site: http://127.0.0.1:8000/
    - Admin panel: http://127.0.0.1:8000/admin/

## Configuration

### Environment Variables

Create a `.env` file in the project root with the following variables:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database settings
DB_NAME=dineease_db
DB_USER=dineease_user
DB_PASSWORD=dineease_password
DB_HOST=localhost
DB_PORT=5432

# Email settings (optional)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

### Database Configuration

The project is configured to use PostgreSQL by default. To use a different database:

1. Update `DATABASES` in `restaurant_site/settings.py`
2. Install appropriate database adapter
3. Update requirements.txt

## Usage

### Admin Panel

1. Access `/admin/` with your superuser credentials
2. Add restaurant information in the "Core" section
3. Create menu categories and items
4. Manage reservations and contact messages
5. Upload gallery images

### Content Management

- **Restaurant Info**: Set basic restaurant details (name, address, hours, etc.)
- **Menu**: Create categories and add menu items with images and dietary information
- **Gallery**: Upload and organize restaurant photos
- **Reservations**: View and manage table bookings
- **Contact**: Monitor customer inquiries

### Customization

- **Styling**: Modify `static/css/base.css` and `static/css/style.css`
- **Templates**: Edit HTML templates in the `templates/` directory
- **Functionality**: Extend views and models as needed

## Development

### Running Tests

```bash
python manage.py test
```

### Code Style

- Follow PEP 8 Python style guide
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions small and focused

### Adding New Features

1. Create models in appropriate app
2. Add views and forms
3. Create templates
4. Update URLs
5. Add tests
6. Update documentation

## Deployment

### Production Checklist

- [ ] Set `DEBUG=False` in production
- [ ] Use strong `SECRET_KEY`
- [ ] Configure production database
- [ ] Set up static file serving
- [ ] Configure email settings
- [ ] Set up SSL/HTTPS
- [ ] Configure logging
- [ ] Set up monitoring

### Recommended Hosting

- **Platform**: Heroku, DigitalOcean, AWS
- **Database**: PostgreSQL (managed service)
- **Static Files**: AWS S3, CloudFront
- **Media Files**: AWS S3 or similar

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions:
- Create an issue in the repository
- Contact the development team
- Check the documentation

## Changelog

### Version 1.0.0
- Initial release
- Basic restaurant website functionality
- Online reservation system
- Menu management
- Photo gallery
- Contact forms
- Responsive design

---

**DineEase** - Making restaurant management easier, one website at a time.
