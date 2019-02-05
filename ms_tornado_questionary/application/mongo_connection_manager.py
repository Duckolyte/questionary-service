from pymodm import connect


class MongoConnectionManager:

    def __init__(self):
        pass

    # def __init__(self, user_id, password):
    #     self.user_id = user_id
    #     self.password = password

    def generate_connection(self, mongodb_connection_uri, connection_alias):
        # generate the connection
        connect(mongodb_connection_uri, connection_alias)
