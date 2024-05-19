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

api_id = 28136850
api_hash = "ef27e112f853d3779d38204f7800ba24"
bot_token = "7056596416:AAFp3ZH8ugPoHlNKysl7jwlO8Kx08wULSXM"
auth_users = "841021123"
sudo_users = [int(num) for num in auth_users.split(",")]
osowner_users = "841021123"
owner_users = [int(num) for num in osowner_users.split(",")]


import os



api_id = 3748059

api_hash = os.environ.get("API_HASH", "f8c9df448f3ba20a900bc2ffc8dae9d5")

bot_token = os.environ.get("BOT_TOKEN")

auth_users = os.environ.get("AUTH_USERS", "5591734243,1369808729")

sudo_users = [int(num) for num in auth_users.split(",")]

osowner_users = os.environ.get("OWNER_USERS", "5591734243,1369808729")

owner_users = [int(num) for num in osowner_users.split(",")]
