import argparse

from rcn.http.client import RCNHttpClient, configDir
from yaml import SafeLoader, load, dump, SafeDumper
import os
from getpass import getpass
import rcn.profile_func
from rcn.models.profile import ProfileDomain
from rcn.utils import saveObjectAsYaml
from rcn.utils.cli import getInput

def profile(actions):
    if actions[0] == "ls":
        rcn.profile_func.ls()
    elif actions[0] == "set-default":
        rcn.profile_func.setDefault(actions[1])
    elif actions[0] == "configure":
        rcn.profile_func.configure(actions[1])
    elif actions[0] == "delete":
        rcn.profile_func.delete(actions[1])

def configure(profile, username=None, backendServer=None, **kwargs):
    profileDomain = ProfileDomain()

    profileDomain.backendServer = backendServer
    if kwargs['stdinPassword']:
        password = input().strip()
    else:
        password = getpass("").strip()

    client = RCNHttpClient(server=profileDomain.backendServer)
    response = client.login({
        "username": username,
        "password": password
    }).json()

    profileDomain.token = response['jwt']
    profileDomain.profile = profile

    saveObjectAsYaml(profileDomain, profile, createFolder=False)