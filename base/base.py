import functools

class GameBaseException(Exception):
    default_message = 'Erro base'
    error_return = False
    handled_exceptions = tuple()


    # def __str__(self, *args, **kwargs):
    #     msg = super(GameBaseException, self).__str__()
    #     return '%s: %s' % (self.default_message, msg)

    @classmethod
    def catch_exception(cls, f):
        @functools.wraps(f)
        def func(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except (cls,) + cls.handled_exceptions as e:
                print('%s: %s' % (cls.default_message, e))
                return cls.error_return
        return func