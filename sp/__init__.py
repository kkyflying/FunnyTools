# -*- coding: utf-8 -*-
__author__ = 'kky'

from .user_agents import __USER_AGENTS
import random


def get_user_agents():
    r"""
    有35个不同的user_agents,
    随机返回一个user_agents,
    :return: string, user_agents
    """
    return random.choice(__USER_AGENTS)

