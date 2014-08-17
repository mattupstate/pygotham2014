# -*- coding: utf-8 -*-
"""
    utils
    ~~~~~
"""
import os
import sys
import traceback
import datetime

from logging import StreamHandler, Formatter, ERROR

def init_logger(app):
    # Add a handler to log to stdout
    class LogFormatter(Formatter):
        def __init__(self):
            super(LogFormatter, self).__init__(
                '[app] %(asctime)s | %(levelname)s | %(message)s | %(pathname)s:%(lineno)d'
            )

        def formatTime(self, record, datefmt=None):
            return '%s+00:00' % datetime.datetime.utcnow().isoformat().split('.')[0]

        def formatException(self, exc):
            return '[app] %s | EXCEPTION | %s' % (
                self.formatTime(None), traceback.format_exc(exc).encode('string_escape'))

    handler = StreamHandler(sys.stdout)
    handler.setFormatter(LogFormatter())
    app.logger.addHandler(handler)

    # Catch all exceptions in the app and log the traceback
    @app.errorhandler(Exception)
    def onerror(e):
        app.logger.exception(repr(e))
        return 'Internal Server Error', 500
