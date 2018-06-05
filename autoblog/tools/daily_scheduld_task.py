import arrow
import os

import time

from autoblog.tools.log_processor import logger
from autoblog.spiders.bluereaderspider import BlogSpider
from autoblog.tools.move_file import MoveFile


class DailyScheduleTask:
    def __init__(self):
        self.time = arrow.utcnow().to('Asia/Shanghai').format("YYYY-MM-DD HH:mm:ss")
        self.cwd = os.path.dirname(os.path.dirname(__file__))
        logger.info("Start daily spider run at %s" % self.time)

    def run(self):
        os.chdir(os.path.dirname(os.path.dirname(__file__)))
        command = r'scrapy crawl %s' % BlogSpider.name
        os.system(command)
        time.sleep(600)

    def move_article(self, source,target):
        while True:
            if os.path.exists(source) and len(os.listdir(source)) >0:
                MoveFile.move_file(source, target)
                break
            else:
                time.sleep(600)

    def publish_articles(self, hexo_root):
        command_clean = r'hexo --cwd %s clean'% hexo_root
        command_g = r'hexo --cwd %s g'% hexo_root
        command_d = r'hexo --cwd %s d'% hexo_root
        os.system(command_clean)
        time.sleep(300)
        os.system(command_g)
        time.sleep(600)
        os.system(command_d)

if __name__ =="__main__":
    daily_run = DailyScheduleTask()
    daily_run.run()
    daily_run.move_article(r'd:\test')
    daily_run.publish_articles(r'd:\autoblog')