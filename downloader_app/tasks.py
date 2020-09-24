import os
import sys

from celery.utils.log import get_task_logger
from dotenv import load_dotenv

from downloader_app.celeryapp import app
from downloader_app.tiff_downloader import download_tiffs as td

# from downloader_app.tiff_downloader import caramba


work_dir = os.getcwd()
route_abs = os.path.dirname(os.path.abspath(work_dir))
sys.path.insert(0, route_abs)


load_dotenv()

logger = get_task_logger("downloader_app")


@app.task
def add(x, y):
    return x + y


@app.task
def download_source(source, dates, point1, point2, opt=False):
    """
    Download satelite tiff files and save it to the directory 'downloadedFiles'.
    """

    try:
        logger.info("Fetch {} {}".format(source, dates))
        td(source, dates, point1, point2, opt)

    except Exception as e:
        logger.error(
            "Error fetch from {} at {} error: {}".format(source, dates, e)
        )
        return

    return
