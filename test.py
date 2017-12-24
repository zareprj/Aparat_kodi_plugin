# -*- coding: utf-8 -*-
# Module: default
# Author: Roman V. M.
# Created on: 28.11.2014
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html

import sys
from urllib import urlencode
from urlparse import parse_qsl
import urllib2
import simplejson as json
import xml.etree.ElementTree as ET

def get_videos(category):
    """
    Get the list of videofiles/streams.

    Here you can insert some parsing code that retrieves
    the list of video streams in the given category from some site or server.

    .. note:: Consider using `generators functions <https://wiki.python.org/moin/Generators>`_
        instead of returning lists.

    :param category: Category name
    :type category: str
    :return: the list of videos in the category
    :rtype: list
    """
            
    
    url = 'http://www.aparat.com/etc/api/'+category
    content = urllib2.urlopen(url)
    json_object = json.load(content)
    VIDEOST=[]
    d={}
    print 'start'
    for i in json_object[category]:
	d["name"]=i['title']	
	d["thumb"]=i['big_poster']
	video_url='https://www.aparat.com/video/video/embed/vt/frame/pid/0/showadstart/no/showvideo/yes/videohash/{0}?data[as]=1'.format(i['uid'])
	config_url='http://www.aparat.com/video/video/config/videohash/{0}/watchtype/site'.format(i['uid'])
	print config_url
	try:
		content2 = urllib2.urlopen(config_url)
		tree = ET.fromstring(content2.read())	
 		d["video"]=tree[0].text 
	except:
		continue			
	d["genre"]=category
	VIDEOST.append(d.copy())
    return VIDEOST



if __name__ == '__main__':
   print get_videos('mostviewedvideos')
    
