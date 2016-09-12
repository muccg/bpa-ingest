# -*- coding: utf-8 -*-
"""
Utility functions to fetch data from web server
"""

import os
import sys
import glob
import requests
from bs4 import BeautifulSoup
from ..util import make_logger

import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

logger = make_logger(__name__)

project_name_passwd_map = {
    "mm": "BPA_MM_DOWNLOADS_PASSWORD",
    "melanoma": "BPA_MELANOMA_DOWNLOADS_PASSWORD",
    "base": "BPA_BASE_DOWNLOADS_PASSWORD",
    "users": "BPA_USERS_DOWNLOADS_PASSWORD",
    "gbr": "BPA_GBR_DOWNLOADS_PASSWORD",
}


def get_password(project_name):
    """Get downloads password for project from environment """

    def complain_and_quit():
        logger.error("Please set shell variable {} to current BPA {} project password".format(password_env,
                                                                                              project_name))
        sys.exit()

    password_env = project_name_passwd_map.get(project_name, None)
    if password_env is None:
        logger.error("project_name `%s' not defined in project_name_passwd_map" % (project_name))
        sys.exit()

    if password_env not in os.environ:
        complain_and_quit()

    password = os.environ[password_env]
    if password == "":
        complain_and_quit()

    return password


class Fetcher():
    """ facilitates fetching data from webserver """

    def __init__(self, target_folder, metadata_source_url, auth):
        self.target_folder = target_folder
        self.metadata_source_url = metadata_source_url
        self.auth = auth

        self._ensure_target_folder_exists()

    def _ensure_target_folder_exists(self):
        if not os.path.exists(self.target_folder):
            from distutils.dir_util import mkpath

            mkpath(self.target_folder)

    def clean(self):
        """ Clean up existing contents """
        files = glob.glob(self.target_folder + "/*")
        for f in files:
            os.remove(f)

    def fetch(self, name):
        """ fetch file from server """
        target = os.path.join(self.target_folder, name)
        target_tmp = target + '.tmp_{}'.format(os.getpid())
        if os.access(target, os.R_OK):
            return
        logger.info("Fetching {0} from {1}".format(name, self.metadata_source_url))
        r = requests.get(self.metadata_source_url + "/" + name, stream=True, auth=self.auth, verify=False)
        with open(target_tmp, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        os.rename(target_tmp, target)

    def fetch_metadata_from_folder(self):
        """ downloads metadata from archive """
        response = requests.get(self.metadata_source_url, stream=True, auth=self.auth, verify=False)
        for link in BeautifulSoup(response.content, "html.parser").find_all("a"):
            metadata_filename = link.get("href")
            if metadata_filename.endswith(".xlsx") or \
                    metadata_filename.endswith(".txt") or \
                    metadata_filename.endswith(".csv") or \
                    metadata_filename.endswith(".zip") or \
                    metadata_filename.endswith(".gz") or \
                    metadata_filename.endswith(".md5"):
                self.fetch(metadata_filename)
