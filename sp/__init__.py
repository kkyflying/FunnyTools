# -*- coding: utf-8 -*-
__author__ = 'kky'

from .user_agents import USER_AGENTS
import random


def get_user_agents():
    r"""
    随机返回一个user_agents
    :return: string, user_agents
    """
    return random.choice(USER_AGENTS)