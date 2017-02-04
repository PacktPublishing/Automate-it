import tornado.ioloop
import tornado.web
import httplib2

#Asynchronous Request Handler
class AsyncHandler(tornado.web.RequestHandler):
        @tornado.web.asynchronous
        def get(self):
            http = httplib2.Http()
            self.response, self.content = http.request("http://ip.jsontest.com/", "GET")
            self._async_callback(self.response, self.content)

	#Work happens in an async way in a callback	
        def _async_callback(self, response, content):
            print "Content:", content
            print "Response:\nStatusCode: %s Location: %s" %(response['status'], response['content-location'])
            self.finish()
            tornado.ioloop.IOLoop.instance().stop()

#Request route
application = tornado.web.Application([
        (r"/", AsyncHandler)], debug=True)

#Start the event loop
if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
