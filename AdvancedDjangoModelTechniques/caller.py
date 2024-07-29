import os
import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Customer
from django.core.exceptions import ValidationError
# Create queries within functions
customer = Customer(
    name="Svetlin Nakov",
    age=19,
    email="nakov@example.com",
    phone_number="+359111111111",
    website_url="https://nakov.com/"
)

try:
    customer.full_clean()
    customer.save()

except ValidationError as e:
    print('\n'.join(e.messages))
