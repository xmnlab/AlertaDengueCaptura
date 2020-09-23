from celery.utils.log import get_task_logger
from dotenv import load_dotenv

from downloader_app import tiff_downloader as td
from downloader_app.celeryapp import app

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
        logger.info("Capturando {} {}".format(source, dates))
        td.download_tiffs(source, dates, point1, point2, opt)

    except Exception as e:
        logger.error(
            "Error capturando from {} at {} error: {}".format(source, dates, e)
        )
        return

    return
