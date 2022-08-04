import os

class MissingEnvironmentVariable(Exception):
    pass


def get_my_env_var(var_name):
    try:
        envvar = os.environ[var_name]
        return envvar
    except KeyError:
        raise MissingEnvironmentVariable(f"{var_name} does not exist")