#!/usr/bin/env python

"""
Downlod tiffs into filesystem

"""

import os
import sys

import pandas as pd

from downloader_app import shapefile_module as shpm
from downloader_app.settings import BASE_DIR
from downloader_app.tasks import download_source

LOCAL = os.path.join(BASE_DIR, "downloader_app")
sys.path.insert(0, LOCAL)


# Set the filepath and load in a shapefile.
SHP_PATH = os.path.join(LOCAL, "RJ_Mun97_region/RJ_Mun97_region.shp")
DOWNLOADFILES_PATH = os.path.join(LOCAL, "DownloadedFiles")


def main():
    # Parameters
    # Extract bounding box from shapefile
    point1, point2 = shpm.extract_shp_boundingbox(SHP_PATH)
    # iterate source list
    source = 'LandDAAC-v5-day'
    # date_start date_end last week
    # argparser(dt_start, dt_end)
    dates = (
        pd.date_range('2016-07-20', '2016-10-30', freq='8D')
        .strftime("%Y-%m-%d")
        .tolist()
    )
    print(dates)
    options = {
        'regrid': [3, 'cubic'],
        'keep_original': False,
        'time_series': True,
        'close_browser': True,
    }

    # Call funcrion
    download_source.delay(source, dates, point1, point2, options)


if __name__ == "__main__":
    main()