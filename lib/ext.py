#!/usr/bin/env python
# -*- coding:utf-8 -*-

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def quotesql(text):
    return text.replace("\\", "\\\\").replace("'", "''")