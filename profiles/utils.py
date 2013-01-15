# -*- coding: utf-8 -*-

def normalize_twitter(username):
    """Twitter usernames for URLs should not include @"""
    if username[0] == "@":
        return username[1:]
    else:
        return username


def normalize_username(serivce, username):
    if service == "T":
        return normalize_twitter(instance.username)
