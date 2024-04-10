import json
import structlog

from django.core.management.base import BaseCommand
from django.db import ProgrammingError

logger = structlog.get_logger(__name__)


class Command(BaseCommand):
    def __init__(self):
        super().__init__()

    def handle(self, *args, **options):
      logger.info(f'args: ${args}')
      logger.info(f'options: ${options}')
      name = options['name']
      logger.info(f'Hello ${name} !!')

    def add_arguments(self, parser):
        parser.add_argument('--name', nargs='?', default='', type=str)
