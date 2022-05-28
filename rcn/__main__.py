import argparse

from rcn import configure, profile

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=["login", "profile"])
    parser.add_argument('--auth-server', default="http://localhost:8080/backend", help="Url of the authorization server")
    parser.add_argument("--profile",default="default", help="configure a specific profile. Default - default")
    parser.add_argument("--username", help="username")
    parser.add_argument("--password-stdin", action='store_true',)

    namespace = parser.parse_args()

    profile_name = namespace.profile
    # actions = namespace.actions
    action = namespace.action
    username = namespace.username
    backendServer = namespace.__getattribute__('auth_server')

    if action == "login":
        configure(profile=profile_name, username=username, backendServer=backendServer, stdinPassword=namespace.__getattribute__("password_stdin"))
    # if actions[0] == "profile":
    #     profile(actions[1:])

    # configure("admin", "admin", "http://localhost:8080/backend", "default")