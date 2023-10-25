from functools import wraps
from graphql.error import GraphQLError
from graphene import ResolveInfo


def custom_user_passes_test(test_func):
    def decorator(func):
        @wraps(func)
        @context(func)
        def wrapper(context, *args, **kwargs):
            if test_func(context.user):
                return func(*args, **kwargs)
            raise GraphQLError("Permission Denied")

        return wrapper
    return decorator

def context(f):
    def decorator(func):
        def wrapper(*args, **kwargs):
            info = next(arg for arg in args if isinstance(arg, ResolveInfo))
            return func(info.context, *args, **kwargs)

        return wrapper

    return decorator