# -*- coding: utf-8 -*-
__author__ = 'kky'

from .user_agents import __get_user_agents

import requests
from lxml import etree



url_source_ip = 'http://www.xicidaili.com/wt/'

headers = {
    "User-Agent":__get_user_agents()
}

high_hide = '高匿'

def __get_ip_page(page):
    r"""
    爬取每一页的ip地址,只保留高匿的地址
    :param page: 爬取第几页
    :return: ip list
    """
    html = requests.get(url_source_ip+str(page),headers=headers)
    selector = etree.HTML(html.text)
    content = selector.xpath('//table[@id="ip_list"]/tr')
    ips = []
    for each in content:
        ip = each.xpath('td[2]/text()')
        port = each.xpath('td[3]/text()')
        ishide = each.xpath('td[5]/text()')
        if len(ip) != 0 and len(port)!=0 and len(ishide)!=0:
            if ishide[0] == high_hide:
                s = '%s:%s'%(ip[0],port[0])
                ips.append(s)
    return ips