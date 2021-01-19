from django.core.management import BaseCommand

from ...registry import get_nosql_models


class Command(BaseCommand):
    def handle(self, *args, **options):
        for name, nosql_model in get_nosql_models().items():
            print(f"Migrating model {name}...")
            nosql_model.create_table(wait=True)
