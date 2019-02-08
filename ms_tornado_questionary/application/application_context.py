import tornado.ioloop
import tornado.web

#import ui templates
#from view import partials

# import controllers
from ms_tornado_questionary.controller.questionary import QuestionaryHandler

# import connection
from ms_tornado_questionary.application.mongo_connection_manager import MongoConnectionManager


class ApplicationContext(tornado.web.Application):

    def __init__(self):

        handlers = [
            (r"/questionary", QuestionaryHandler)
            ]

        # template_path='C:/Users/andygg/PycharmProjects/tornado-formalyser/templates'
        settings = dict(
            #ui_modules=partials,
            #template_path='C:/programming/atom_workspace/issue_manager',
            #static_path='C:/programming/atom_workspace/issue_manager/',
            #xsrf_cookies=True,
            #cookie_secret='123456789',
            #login_url='/login'
        )

        tornado.web.Application.__init__(self, handlers, **settings)

        # TODO source out the connection information to a separate resource file
        self.db_uri = "mongodb://localhost:27017/questionary"
        self.connection_alias = "questionary-con"

        # create a connection manager and set up the connection
        mongo_con = MongoConnectionManager()
        mongo_con.generate_connection(
            mongodb_connection_uri=self.db_uri,
            connection_alias=self.connection_alias
        )

