# DineEase Restaurant Website

A modern, responsive restaurant website built with Django, featuring online reservations, menu management, and a beautiful user interface.

## Features

- **Responsive Design**: Mobile-first UI using Bootstrap 5
- **Online Reservations**: Easy table booking with validation
- **Menu Management**: Dynamic menu with categories and dietary info
- **Photo Gallery**: Image showcase with lightbox effects
- **Contact Forms**: Customer inquiries via secure forms
- **Admin Panel**: Full Django admin for content management

## Technology Stack

- **Backend**: Django 5.2.5
- **Database (default)**: SQLite
- **Optional Database**: PostgreSQL (via `psycopg2-binary`)
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript
- **Forms**: Django Crispy Forms (Bootstrap 5)
- **Images**: Pillow for image processing
- **Env Config**: python-decouple (`.env`)

## Project Structure

```
.
├── manage.py                     # Django management entrypoint
├── requirements.txt              # Python dependencies
├── start.sh                      # Helper script (venv + collectstatic + runserver)
├── setup.py                      # Seeds admin user and sample data
├── restaurant_site/              # Project settings and WSGI/ASGI
├── core/                         # Home, about, gallery
├── menu/                         # Menu categories and items
├── reservations/                 # Table booking system
├── contact/                      # Contact forms
├── static/                       # CSS, JS, images
├── templates/                    # HTML templates
└── media/                        # User uploads (created at runtime)
```

## Installation

### Prerequisites

- Python 3.10+
- pip

### Setup Instructions

1. **Clone and enter the project**
   ```bash
   git clone <repository-url>
   cd <project-root>
   ```

2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create environment file**
   Create a `.env` file in the project root:
   ```env
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   ```

5. **Initialize the database (SQLite)**
   ```bash
   python manage.py migrate
   ```

6. **Seed sample data and admin (optional but recommended)**
   ```bash
   python setup.py
   # Admin credentials created: admin / admin123
   ```

7. **Collect static files**
   ```bash
   python manage.py collectstatic --noinput
   ```

8. **Run the development server**
   ```bash
   python manage.py runserver
   # Or use the helper script (expects venv at ./venv):
   ./start.sh
   ```

9. **Access the website**
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## Configuration

### Environment Variables

Supported variables in `.env` (via python-decouple):

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Optional: PostgreSQL settings if you switch databases (see below)
DB_NAME=dineease_db
DB_USER=dineease_user
DB_PASSWORD=dineease_password
DB_HOST=localhost
DB_PORT=5432
```

### Database Configuration

The project runs on SQLite by default (see `restaurant_site/settings.py`).

To use PostgreSQL instead:
1. Ensure `psycopg2-binary` is installed (already listed in `requirements.txt`).
2. Update `DATABASES` in `restaurant_site/settings.py` to a PostgreSQL configuration, e.g.:
   ```python
   DATABASES = {
       "default": {
           "ENGINE": "django.db.backends.postgresql",
           "NAME": config("DB_NAME"),
           "USER": config("DB_USER"),
           "PASSWORD": config("DB_PASSWORD"),
           "HOST": config("DB_HOST", default="localhost"),
           "PORT": config("DB_PORT", default=5432, cast=int),
       }
   }
   ```
3. Run `python manage.py migrate` against the new database.

## Usage

### Admin Panel

1. Visit `/admin/` and log in (default: `admin` / `admin123` if seeded via `setup.py`).
2. Set restaurant info in the Core section.
3. Create menu categories and items.
4. Manage reservations and contact messages.
5. Upload gallery images.

### Content Customization

- **Styling**: Edit `static/css/base.css`.
- **Templates**: Update files in `templates/`.
- **Views/Models**: Extend apps under `core/`, `menu/`, `reservations/`, `contact/`.

## Development

### Run Tests
```bash
python manage.py test
```

### Code Style
- Follow PEP 8
- Use meaningful names and add docstrings where appropriate
- Keep functions small and focused

### Adding Features
1. Add/modify models in the relevant app
2. Create views and forms
3. Add templates
4. Wire up URLs
5. Add tests and update docs

## Deployment

### Production Checklist
- [ ] Set `DEBUG=False`
- [ ] Use a strong `SECRET_KEY`
- [ ] Configure a production database (e.g., PostgreSQL)
- [ ] Configure static/media hosting
- [ ] Configure email settings (if used)
- [ ] Add SSL/HTTPS and security headers
- [ ] Configure logging/monitoring

### Recommended Hosting
- **Platforms**: Heroku, DigitalOcean, AWS
- **Database**: PostgreSQL (managed service)
- **Static/Media**: AWS S3 + CDN

## Contributing
1. Fork the repository
2. Create a feature branch
3. Make changes and add tests
4. Submit a pull request

## License
MIT — see `LICENSE` for details.

## Support
- Open an issue in the repository
- Check `QUICK_START.md` and this README

## Changelog

### 1.0.0
- Initial release with reservations, menu, gallery, contact, and responsive design

---

**DineEase** — Making restaurant management easier, one website at a time.
