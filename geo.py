#-*- coding: utf-8 -*-

import os
import sys

from os.path import join, exists

import urllib2

def getRequest(url):

    request = urllib2.Request(url)

    request.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)')

    try:

        try:

            response = urllib2.urlopen(request,timeout=20)

            return response.read() #.decode('gbk','ignore').encode('utf-8') #.replace(u'�','')

        except Exception,e:

            print "erorr %s %s" % (url,e)

            return None



    except urllib2.HTTPError, e:

        print e.code





def saveToFile(filepath,filename,content):

    #with open(join("/data/scrapy/comms/", filename), 'wb') as f:

    with open(join(filepath,filename), 'wb') as f:

            f.write(content)





if __name__ == '__main__':

    AppID='j82cmzLV34F2vGpGjDNtsO7LvG58IRe5nzW6sgkCBjf.1Kb1j0Et2q04ksM_ThCv3rc-'
    place=raw_input('Enter the place:')
    Geo="http://where.yahooapis.com/v1/places.q('%s')?appid=%s"%(place,AppID)
    htmlstr=getRequest(Geo)
    saveToFile('.','gettest.xml',htmlstr)
