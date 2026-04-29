import os
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).resolve().parent))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sige.settings')

import django
django.setup()

# Auto-migrate on cold start
try:
    from django.core.management import call_command
    call_command('migrate', '--run-syncdb', verbosity=0)
except Exception:
    pass

from django.core.wsgi import get_wsgi_application
app = get_wsgi_application()
