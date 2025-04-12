
registry = {}

def register_strategy(name):
    def decorator(func):
        registry[name] = func
        return func
    return decorator

def get_registered_strategies():
    return registry
