from jupyter_server.auth.identity import PasswordIdentityProvider

c.ServerApp.allow_remote_access = True
c.ServerApp.allow_origin = '*'
c.ServerApp.root_dir = "/home/REDACTED/jupyter-env/notebooks"

