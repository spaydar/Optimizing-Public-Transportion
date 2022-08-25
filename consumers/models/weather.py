"""Contains functionality related to Weather"""
import logging


logger = logging.getLogger(__name__)


class Weather:
    """Defines the Weather model"""

    def __init__(self):
        """Creates the weather model"""
        self.temperature = 70.0
        self.status = "sunny"

    def process_message(self, message):
        """Handles incoming weather data"""
        logger.info("Processing weather message")
        #
        #
        # DONE: Process incoming weather messages. Set the temperature and status.
        #
        #
        try:
            value = message.value()
            self.temperature = value['temperature']
            self.status = value['status']
            logger.info(f'Set weather: temperature {self.temperature}, status {self.status}')
        except Exception as e:
            logger.error(f'Error parsing message fields: {e}')
