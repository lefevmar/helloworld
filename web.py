import falcon

from wsgiref import simple_server

class DemoResource:

    def on_get(self, req, resp):

        name = req.params.get("name", "john doe")
        resp.media = "coucou " + name + " !"

#create web server
application = falcon.API()

#add api routes
application.add_route('/demo', DemoResource())

#main for debug only (not used in production)
if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', 8000, application)
    httpd.serve_forever()