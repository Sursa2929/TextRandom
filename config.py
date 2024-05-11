#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

#Bot Created by Surya Bishnoi love ❤️ B 

API_ID = os.environ.get("API_ID")

API_HASH = os.environ.get("API_HASH")

BOT_TOKEN = os.environ.get("BOT_TOKEN")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 841021123))

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6775997216").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)

