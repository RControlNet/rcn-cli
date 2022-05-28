from pathlib import Path

import ruamel.yaml
from yaml import load, SafeLoader
import os

from rcn.models.profile import ProfileDomain

configDir = f"{Path.home()}/.rcn/"
if not os.path.exists(configDir):
    os.makedirs(configDir)

yaml = ruamel.yaml.YAML()


class RCNFilters(object):
    def __init__(self, name = None, configuration = None):
        self.name = name
        self.configuration = configuration


class RCNConfig(object):
    def __init__(self):
        self.credentials = None
        self.clientJson = []
        self.token = None
        self.filters = [RCNFilters(name="ior_research.utils.filterchains.RControlNetMessageFilter")]
        self.streamer = None

    def dumpasfile(self, profile):
        saveObjectAsYaml(self, profile)

yaml.register_class(RCNFilters)
yaml.register_class(RCNConfig)
yaml.register_class(ProfileDomain)

def saveObjectAsYaml(obj, filename, createFolder=True):
    if not os.path.exists(os.path.join(configDir, filename)):
        os.makedirs(os.path.join(configDir, filename))

    filePath = os.path.join(configDir, filename if createFolder else "", f"{filename}.yml")
    with open(filePath, "w") as stream:
        yaml.dump(obj, stream)

def loadYamlAsClass(filePath):
    with open(filePath, "r") as stream:
        return yaml.load(stream)
