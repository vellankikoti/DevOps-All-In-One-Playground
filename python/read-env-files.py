import os

def read_env_var(var_name):
    value = os.getenv(var_name)
    if value:
        print(f"{var_name}={value}")
    else:
        print(f"{var_name} is not set")

read_env_var('HOME')
