import mechanicalsoup
import re

class WhatBoxAPI:
    def __init__(self, username=None, password=None):
        self.mk = mechanicalsoup.StatefulBrowser()
        self.username = username
        self.password = password
        self.login()

    def login(self):
        self.mk.open('https://whatbox.ca/login')
        self.mk.select_form()
        self.mk['username'] = self.username
        self.mk['password'] = self.password
        self.mk['keeplogged'] = '1'
        self.mk.submit_selected()
        r = self.mk.open('https://whatbox.ca/')
        if r.status_code != 200:
            raise Exception('Login failed')

    def logout(self):
        self.mk.open('https://whatbox.ca/logout')

    def storage_usage(self):
        r = self.mk.open('https://whatbox.ca/manage')
        usage = re.search('<span class="usage_disk_test" title="(.+?) used">', r.text).group(1)

    def upload_usage(self):
        r = self.mk.open('https://whatbox.ca/manage')
        usage = re.search('<span class="auto usage_traffic_text">(.+?)</span>', r.text).group(1)    

    def traffic_reset_time(self):
        r = self.mk.open('https://whatbox.ca/manage')
        usage = re.search('<span> "Traffic resets in: " <time datetime="(.+?)" title="(.+?)">', r.text).group(2)

    def traffic_reset_distance(self):
        r = self.mk.open('https://whatbox.ca/manage')
        usage = re.search('<span> "Traffic resets in: " <time datetime="(.+?)" title="(.+?)">(.+?)</time>', r.text).group(3)
        
