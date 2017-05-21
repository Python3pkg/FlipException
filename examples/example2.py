#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flipexception import FlipException


try:
    raise FlipException("Error getting lalala")
except Exception as e:
    print(str(e))

try:
    raise FlipException("Error getting value")
except FlipException as e:
    print(str(e))

try:
    raise FlipException
except FlipException as e:
    print(str(e))

