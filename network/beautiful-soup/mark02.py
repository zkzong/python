from markupsafe import Markup, escape

class User(object):

    def __init__(self, id, username):
        self.id = id
        self.username = username

    def __html_format__(self, format_spec):
        if format_spec == 'link':
            return Markup('<a href="/user/{0}">{1}</a>').format(
                self.id,
                self.__html__(),
            )
        elif format_spec:
            raise ValueError('Invalid format spec')
        return self.__html__()

    def __html__(self):
        return Markup('<span class=user>{0}</span>').format(self.username)

user = User(1, 'foo')
print(Markup('<p>User: {0:link}').format(user))
