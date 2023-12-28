import logging
import logging.config
import datetime

CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "colored": {
            "()": "colorlog.ColoredFormatter",
            "fmt": "%(thin_white)s%(asctime)s%(reset)s %(log_color)s%(levelname)-8s%(reset)s [%(blue)s%(name)s%(reset)s] %(purple)s%(funcName)s%(reset)s: %(message_log_color)s%(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
            "log_colors": {
                "DEBUG": "white",
                "INFO": "cyan",
                "WARNING": "bold_yellow",
                "ERROR": "bold_red",
                "CRITICAL": "bg_bold_red,bold_white",
            },
            "secondary_log_colors": {
                "message": {
                    "DEBUG": "thin_white",
                    "INFO": "white",
                    "WARNING": "yellow",
                    "ERROR": "red",
                    "CRITICAL": "bold_red",
                }
            },
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "formatter": "colored",
        },
        "disabled": {
            "class": "logging.NullHandler",
        },
    },
    "loggers": {
        "": {
            "handlers": ["console"],
            "level": "INFO",
        },
        "discord": {
            "handlers": ["disabled"],
            "propagate": False,
        },
    },
}

logging.config.dictConfig(CONFIG)

# logging.basicConfig(level=logging.INFO)
