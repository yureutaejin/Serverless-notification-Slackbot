#!/bin/bash
((cd ~/project/ && \/usr/local/bin/python3.8 slack_bot.py) >>  ~/project/cronlog.log 2>&1)
