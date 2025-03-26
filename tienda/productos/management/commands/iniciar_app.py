import logging
from django.core.management.base import BaseCommand

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Inicia la aplicación y registra el evento en el log.'

    def handle(self, *args, **options):
        logger.info('La aplicación ha sido iniciada.')
        self.stdout.write(self.style.SUCCESS('Registro de inicio de la aplicación guardado en el log.'))
