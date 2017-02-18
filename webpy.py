#!/usr/bin/env python
import web
import json

log = 'log'

urls = (
    '/hello/', 'index'
)

f = open(log,'a')


class index:
    def POST(self):
        data = web.data()

        f = open(log, 'a')
        f.write(data)  # python will convert \n to os.linesep
        f.write('\n')  # python will convert \n to os.linesep
        f.close()  # you can omit in most cases as the destructor will call it

        print data

        return "Hello " + data + "!\n"

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()