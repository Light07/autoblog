# -*- coding: utf-8 -*-
import traceback

import re
import requests

from autoblog.tools.log_processor import logger


class SiteUrlEnum:
    BLUE_READER = 'http://bluereader.org'

class SharedAPI(object):

    def __init__(self):
        self.s = requests.session()
        self.header_form = {'Content-Type': 'application/x-www-form-urlencoded', 'charset': 'UTF-8'}
        self.header_json = {'Content-Type': 'application/json', 'charset': 'UTF-8'}

    def get_blue_reader_token(self, username=None, pwd=None):

        login_url = SiteUrlEnum.BLUE_READER + '/index.php?do=login&act=submit'
        parameter = {'refer':SiteUrlEnum.BLUE_READER, 'user':username, 'pwd':pwd}
        try:
            p = self.s.post(login_url, data=parameter, headers=self.header_form, verify=False)
            if int(p.status_code) == 200:
                c = self.s.get(SiteUrlEnum.BLUE_READER).content.decode('utf-8')
                regex_str = r'''name="token" value="(.*?)">'''
                property_regex = re.compile(regex_str)
                return property_regex.search(c).group(1)
        except:
                logger.exception('get token failed', exc_info=True)
