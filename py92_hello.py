#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    # body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    body = '''{
                "name": "中国",
                "province": [{
                    "name": "黑龙江",
                    "cities": {
                        "city": ["哈尔滨", "大庆"]
                    }
                }, {
                    "name": "广东",
                    "cities": {
                        "city": ["广州", "深圳", "珠海"]
                    }
                }, {
                    "name": "台湾",
                    "cities": {
                        "city": ["台北", "高雄"]
                    }
                }, {
                    "name": "新疆",
                    "cities": {
                        "city": ["乌鲁木齐"]
                    }
                }]
            }
    '''
    # return [body.encode('utf-8')]
    return [body.encode('gbk')]