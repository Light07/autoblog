BlueReaderAccount = {'username':'thinkbig', 'password':'P@ssw0rd'}

# tags: rss resource name
# list value are the xpath of the target article:
# first one is he xpath of the target article title.
# second one is the xpath of the target article content.
tags_contents_mapping = {
    "卢松松博客": [".//*[@class='post-content']/div[1]/h1", ".//*[@class='post-content']/dd/child::*[not(@id='wenad')]"],
    "雷锋网": [".//*[ @class ='article-title']/div/h1", ".//*[@class='wrapper clr']/div[1]/div[1]"],
    "雪球": [".//*[@id='app']/div[2]/article/h1", ".//*[@id='app']//*[@class='article__bd__detail']//p"],
    "小众软件": [".//*[@id='content']/div[1]/h2", ".//*[@class='entry-content']"],
    "互联网的那点事": [".//*[@class='post article']/h1", ".//*[@class='post article']/div[2]/div[3]"],
    "八卦新闻": [".//*[@id='article-container']/div[2]/div[1]/div[1]/h1", ".//*[@id='mp-editor']/p"],
    "战隼的学习探索": [".//*[@class='section entry']/div[1]/h1", ".//*[@class='section entry']/div[1]/div"],
    "调查与记录": [".//*[@id='article-zone-a']/div[2]/div/h3", ".//*[@id='article-zone-a']/div[2]/div/div[@class='content']/div/text()"],
    "阮一峰的网络日志":[".//*[@id='page-title']", ".//*[@id='main-content']"],
    "酷 壳 – CoolShell":[".//*[@id='main']/article/header/h1", ".//*[@id='main']/article/div"],
    "知乎日报": [".//*[@class='main-wrap content-wrap']/div[@class='headline']/div/h1",
                                 ".//*[@class='main-wrap content-wrap']/div[@class='content-inner']/div[1]/div"]
                         }