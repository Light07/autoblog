# -*- coding: utf-8 -*-
import codecs
import logging
import sys

import os

import scrapy


class LogProcessor:
    def __init__(self, logger_name=__name__):
        # New a logger
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.INFO)

        # Create log file, specify format
        log_dir = os.path.dirname(os.path.dirname(__file__)) + '\logs'

        if not os.path.exists(log_dir):
            os.mkdir(log_dir)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -%(pathname)s  - %(message)s')

        # create file handler, console handler
        file_handler = logging.FileHandler(os.path.join(log_dir, 'log.log'))
        file_handler.setFormatter(formatter)

        c_handler = logging.StreamHandler(sys.stdout)
        c_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)
        self.logger.addHandler(c_handler)

    def info(self, msg):
        self.logger.info(msg)

    def debug(self, msg):
        self.logger.debug(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg, exc):
        self.logger.critical(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def exception(self, msg, exc_info):
        self.logger.exception(msg, exc_info=True)


logger = LogProcessor(scrapy.Spider.name)