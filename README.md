# Auto generated blog framework

## What's this project for?

This project is an auto-generated blog framework, By specifying rss sources, people may have their own blog system built
automatically and smartly -- articles only take your fancy.

This project is a outcome of my self-learning for scrapy -- a powerful web crawl framework.

## Brief structure of the project
This project based on scrapy and hexo. 
Scrapy is one of the best framework which powered by network spider crawl to get internet contents.
Hexo is a very good blog system with plenty of themes templated which let user build their own blog rapidly.

- Use a rss website(bluereader.org) to collect all of the topics that interest you and based on the categories user created, let
spider to crawl all of the contents for use.
- Convert the html contents to a format that hexo can use directly, based on specific themes of course.
- processing, clean, save then generate & publish the contents to public.

## Precondition

- You should have hexo installed. Check site [Hexo](https://hexo.io/) for detail.
- You should download and installed the suitable themes of Hexo. Check site [Hexo Themes](https://hexo.io/themes/) for detail.
(This project use Asnippet).
- Configure your theme properly based on hexo tutorial.

## How to use

Simply download this repro then run "daily_scheduld_task.py" file under autoblog/tools, then switch to command line within
the root folder and type
>hexo clean

>hexo g

>hexo s

then open your browser , type http://127.0.0.1:4000 and that's it.

## Publish to public
- You may use jenkins or schedule task to let it run daily automatically.
- You should have a domain for use and bind this repro to your domain.

## Known issues:
- Some image within articles doesn't shown correctly, because they are referred via hyper-link.
- Some articles may not show all of the contents correctly due to the library tomd it not powerful enough.

## To do list:
- Fix the bugs mentioned above
- Middlewares for IP proxy is not developed well, better to auto update the ip pools and remove the invalid ones.
- Themes categories need to configured manually, better automize this process.

