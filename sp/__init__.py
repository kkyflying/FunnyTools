# -*- coding: utf-8 -*-
__author__ = 'kky'


from .ip import __get_ip_page

from .user_agents import __get_user_agents,__get_user_agents_list

def __write(file,txt):
    with open(file,'a') as f:
        f.write(txt)

def get_user_agents_list():
    r"""
    返回全部的user_agents
    :return: list
    """
    return __get_user_agents_list()

def get_user_agents():
    r"""
    有35个不同的user_agents,
    随机返回一个user_agents,
    :return: string, user_agents
    """
    return __get_user_agents()


def get_ip(page_num,file_path):
    r"""
    获取高匿名ip
    :param page_num: 需要多少页ip
    :param file_path: 保存ip的文件路径
    :return:
    """
    for page in range(1,page_num):
        ips = __get_ip_page(page)
        for ip in ips:
            __write(file_path,ip+'\n')


