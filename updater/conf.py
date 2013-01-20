
__version__     = '2011.07.10-00'
__author__      = 'Scott Rogers'
__stability__   = 'alpha'
__copying__     = """Copyright (C) 2011 W. Scott Rogers
                      This program is free software.
                      You can redistribute it and/or modify it under the terms of the
                      GNU General Public License as published by the Free Software Foundation;
                      version 2 of the License.
                  """
import sys
import yaml

class Configuration(object):

    def __init__(self, confFile = 'conf/xiin.config.yml'):
        self = self
        self.conf = yaml.load(open(confFile, 'r'))
    #end

    def get_configuration(self, conf):
        return self.conf[conf]
    #end
#end