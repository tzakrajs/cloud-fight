import json
import tornado.web

from core import route

# Test ListUsers
@route('/api/users')
class ListUsers (tornado.web.RequestHandler):
    def get(self):
        user_list = list(users.keys())
        self.write(json.dumps(user_list))

# Test GetUser
@route('/api/user')
class GetUser (tornado.web.RequestHandler):
    def get(self):
        user_id = self.get_argument('id', None)
        user_info = users.get(int(user_id))
        self.write(json.dumps(user_info))
