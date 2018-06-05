# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
import arrow
import re

import os

from autoblog.tools.log_processor import logger


class AutoblogPipeline(object):
    def __init__(self):
        self.file_path = os.path.dirname(os.path.dirname(__file__))+ os.sep + "articles"
        if not os.path.exists(self.file_path):
            os.mkdir(self.file_path)

    def open_spider(self, spider):
        logger.info(spider.name + ' --starts')

    def close_spider(self, spider):
        logger.info(spider.name + ' --ends')

    def process_item(self, item, spider):
        file_path = self.file_path + os.sep + '%s.md' % re.sub('[\/:*?"<>|]', '-', item["title"])
        with codecs.open(file_path, 'w+', encoding='utf-8') as file:
            file.writelines("---" + "\n")
            file.writelines("title: '%s'" % str(item["title"]) + "\n")
            file.writelines("date: '%s'" % str(item["date"]) + "\n")
            file.writelines("tags: '%s'" % item["tags"] + "\n")
            file.writelines("categories: '%s'" % item["categories"] + "\n")
            file.writelines("---" + "\n")
            line = json.dumps(item["contents"], ensure_ascii=False)
            line = line.split(r'\n')
            # Comments parts are for Next Theme of hexo.
            # if item["desc"] and item["desc"] !="":
            #     file.writelines(item["desc"] + "\n")
            # else:
            #     file.writelines("%s," % item["title"] + "\n")
            # file.writelines('<!--more-->' + "\n")
            for content in line:
                if content != '"' and content !='':
                    file.writelines(content + "\n")
            file.writelines('''原文请参见: %s ''' %item["url"] + "\n")