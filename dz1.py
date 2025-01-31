# Логирование с использованием нескольких файлов
# Напишите скрипт, который логирует разные типы сообщений в разные файлы.
# Логи уровня DEBUG и INFO должны сохраняться в debug_info.log, а логи уровня
# WARNING и выше — в warnings_errors.log.

import logging

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

debug_info_handler = logging.FileHandler('debug_info.log', encoding='utf-8')
debug_info_handler.setLevel(logging.DEBUG)
debug_info_handler.setFormatter(formatter)

warnings_errors_handler = logging.FileHandler('warnings_errors.log', encoding='utf-8')
warnings_errors_handler.setLevel(logging.WARNING)
warnings_errors_handler.setFormatter(formatter)

logger = logging.getLogger('MultiFileLogger')
logger.setLevel(logging.DEBUG)

logger.addHandler(debug_info_handler)
logger.addHandler(warnings_errors_handler)

logger.debug("Это сообщение уровня DEBUG")
logger.info("Это сообщение уровня INFO")
logger.warning("Это сообщение уровня WARNING")
logger.error("Это сообщение уровня ERROR")
logger.critical("Это сообщение уровня CRITICAL")
