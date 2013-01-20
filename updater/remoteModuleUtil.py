
__version__     = '2011.07.10-00'
__author__      = 'Scott Rogers, aka trash80'
__stability__   = 'alpha'
__copying__     = """Copyright (C) 2011 W. Scott Rogers \
                        This program is free software.
                        You can redistribute it and/or modify it under the terms of the
                        GNU General Public License as published by the Free Software Foundation;
                        version 2 of the License.
                    """

import urllib2
from spinner import Spinner
from baseModuleUtil import ModuleUtil
from htmlModuleUtil import HtmlModuleUtil

class RemoteModuleUtil(ModuleUtil):

    def __init__(self):
        self = self
    #end

    def get_module_dict(self, remoteUrl):
        """
        Returns a dictionary of module(key):version(value) of server side modules.
        """
        moduleDict       = {}
        spinner          = Spinner()
        remoteModuleList = self.get_module_list(remoteUrl)
        count = 1

        for moduleName in remoteModuleList:
            spinner.render(count)
            urlFull = '{0}/{1}'.format(remoteUrl, moduleName)
            moduleVersion = self.get_module_version(urlFull)
            moduleDict[str(moduleName)] = str(moduleVersion)
            count = count + 1

        return moduleDict
    #end

    def get_module_list(self, xiinUrlDir):
        """
        Returns a list of server side module names.
        """
        parser      = HtmlModuleUtil()
        connection  = urllib2.urlopen(xiinUrlDir)
        response    = connection.read()
        
        parser.feed(response)
        parser.close()

        return parser.get_list()
    #end

    def get_module_version(self, xiinUrlMod):
        """
        Returns the version of a module.
        """
        connection      = urllib2.urlopen(xiinUrlMod)
        dirtyVersion    = connection.readlines()[1]

        return self.clean(dirtyVersion)
    #end

    def set_url_home(self, xiinUrl):
        self.urlHome = xiinUrl
    #end

    def get_url_home(self):
        return self.urlHome
    #end

    def set_url_directory(self, xiinDir):
        self.urlDirectory = xiinDir
    #end

    def get_url_directory(self):
        return self.urlDirectory
    #end
#end
