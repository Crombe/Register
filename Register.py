#coding=gbk
__author__ = 'Administrator'

import urllib2
import urllib
import httplib


'''
GET /checklogin.jsp?username=%B3%C2%B3%BF&password=000000&Submit2=%C8%B7%C8%CF%B5%C7%C2%BC HTTP/1.1
Host: 192.168.1.183
Connection: keep-alive
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36
Referer: http://192.168.1.183/login.jsp
Accept-Encoding: gzip, deflate, sdch
Accept-Language: zh-CN,zh;q=0.8
Cookie: JSESSIONID=7BF427A676FC3F992E4C816A1ECAF8EF
'''
class Register():
    values = {}
    values['username'] = '陈晨'
    values['password'] = '000000'
    data = urllib.urlencode(values)

    geturl = "/checklogin.jsp?" + data +"&Submit2=%C8%B7%C8%CF%B5%C7%C2%BC"
    indexurl = "/index.jsp"
    httpClient = None


    def moveRequest(self):
        response = self.httpClient.getresponse()
        print "aaa"
        #print response.getheaders()
        if response.status == 302:
            print "status 302"

        location = response.getheader('location')
        print "location: " + location
        print "move url: " + location[20:]
        move_url = location[20:]
        if self.httpClient:
            self.httpClient.request('GET',move_url,  '', {"Host":" 192.168.1.183",
                                      "User-Agent":  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87",
                                          "Referer": "http://192.168.1.183/login.jsp",
                                          "Connection": "keep-alive",
                                                     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                                                     "Cookie": "JSESSIONID=2DA02459C2A5D92793659CF25865F61C"})
            response = self.httpClient.getresponse()
            print response.status
            print response.read()


    def Request(self):
        try:
            self.httpClient = httplib.HTTPConnection('192.168.1.183', 80, timeout = 1000)
            self.httpClient.request('GET', self.geturl, '', {"Host":" 192.168.1.183",
                                              "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87",
                                                  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                                                  "Referer": "http://192.168.1.183/login.jsp",
                                                  "Connection": "keep-alive",
                                                  "Cookie": "JSESSIONID=2DA02459C2A5D92793659CF25865F61C"})
            #response = self.httpClient.getresponse()
            #print response.status

            self.moveRequest()
            print 'bbbbb'
            self.moveRequest()
            response = self.httpClient.getresponse()
            print response.status
        except Exception, e:
            print e
        finally:
            if self.httpClient:
                self.httpClient.close()

    def RequestIndex(self):
        try:
            self.httpClient = httplib.HTTPConnection('192.168.1.183', 80, timeout = 100)
            self.httpClient.request('GET', self.indexurl, '', {"Host":" 192.168.1.183",
                                              "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87",
                                                  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                                                  "Referer": "http://192.168.1.183",
                                                  "Connection": "keep-alive",
                                                  "Cookie": "JSESSIONID=2DA02459C2A5D92793659CF25865F61C"})
            #response = self.httpClient.getresponse()
            #print response.status


            print 'ccccc'

            response = self.httpClient.getresponse()
            print response.status
            print response.read()


        except Exception, e:
            print e
        finally:
            if self.httpClient:
                self.httpClient.close()


if __name__ == '__main__':
   register = Register()
   register.Request()
   register.RequestIndex()


'''
values = {}
values['username'] = '陈晨'
values['password'] = '000000'
data = urllib.urlencode(values)

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent' : user_agent}
print data
geturl = "http://192.168.1.183/checklogin.jsp?" + data + "&Submit2=%C8%B7%C8%CF%B5%C7%C2%BC"
url = "http://192.168.1.183/checklogin.jsp?"

request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.read()
'''