import os
import sys
from pathlib import Path

# Add the project root to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sige.settings')

# Run migrations automatically on cold start (Vercel serverless)
from django.core.wsgi import get_wsgi_application

try:
    import django
    django.setup()
    from django.db import connection
    from django.core.management import call_command
    call_command('migrate', '--run-syncdb', verbosity=0)
except Exception:
    pass

application = get_wsgi_application()

# Vercel expects `app`
app = application
