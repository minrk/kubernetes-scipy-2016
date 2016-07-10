import tornado
from .handlers import *

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/newspark", SparkHandler),
    (r"/newdask", DaskHandler),
    (r"/newipyparallel", IPythonParallelHandler),
    (r"/new_sparknamespace", SparkNameSpaceHandler),
], debug=True)
