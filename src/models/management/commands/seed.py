from django.core.management.base import BaseCommand
import random
from address.models import Address, Locality, State, Country

from logging import getLogger

from models.models import (
    Customer,
    CustomerRecord,
    Payment
)


log = getLogger(__name__)

# python manage.py seed --mode=refresh

""" Clear all data and creates cusotmers """
MODE_REFRESH = 'refresh'

""" Clear all data and do not create any object """
MODE_CLEAR = 'clear'

class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(self, options['mode'])
        self.stdout.write('done.')


def clear_data():
    """Deletes all the table data"""
    log.info("Deleting customers")
    Customer.objects.all().delete()
    CustomerRecord.objects.all().delete()


def create_customer(local, payment_types):
    """Creates an customer object combining different elements from the list"""
    log.info("Creating customer")

    active_options = [True, False]
    first_name_options = ["Bob", "Jane", "Joe", "Hank", "Jill", "Tom", "Alice"]
    last_name_options = ["Smith", "Adams", "Thompson", "Berry", "Phillips"]


    a = Address(
            street_number="1",
            route="Some Street",
            locality=local,
            raw="1 Some Street, Charlottesvile, VA"
        )
    a.save()

    c = Customer(
        active=random.choice(active_options),
        first_name=random.choice(first_name_options),
        last_name=random.choice(last_name_options),
        address=a
    )
    c.save()


    cr = CustomerRecord(
         customer=c,
         num_meals=1,
         payment_type=random.choice(payment_types)
     )
    cr.save()

    log.info("{} customer created.".format(c))
    return c

def run_seed(self, mode):
    """ Seed database based on mode

    :param mode: refresh / clear 
    :return:
    """
    # Clear data from tables
    clear_data()
    if mode == MODE_CLEAR:
        return
    
    payment_types = []

    try:
        country = Country(name="US")
        country.save()
        state = State(name="VA", country=country)
        state.save()
        local = Locality(name="Charlottesville", postal_code="22911", state=state)
        local.save()
    except:
        local = Locality.objects.first()

    try:
        p1 = Payment(name="debit")
        p1.save()
        p2 = Payment(name="credit")
        p2.save()
        p3 = Payment(name="cash")
        p3.save()

        payment_types = [p1,p2,p3]
    except:
        payment_types = Payment.objects.all()
    

    # Creating 30 customers
    for i in range(30):
        try:
            create_customer(local,payment_types)
        except:
            pass