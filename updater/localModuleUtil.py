
__version__     = '2011.07.10-00'
__author__      = 'Scott Rogers, aka trash80'
__stability__   = 'alpha'
__copying__     = """Copyright (C) 2011 W. Scott Rogers \
                        This program is free software.
                        You can redistribute it and/or modify it under the terms of the
                        GNU General Public License as published by the Free Software Foundation;
                        version 2 of the License.
                    """
                    
import os
from baseModuleUtil import ModuleUtil

class localModuleUtil(ModuleUtil):

    def __init__(self):
        self = self
    #end

    def get_module_dict(self, url):
        """
        Creates a dictionary of module(key):version(value) of local modules.
        """
        
        localmoduleDict = {}
        localmoduleList = self.get_module_list(url)

        for localmodule in localmoduleList:
            module = '{0}/{1}'.format(url, localmodule)
            localmoduleDict[localmodule] = self.get_module_version(module)

        return localmoduleDict
    #end

    def get_module_list(self, url):
        """
        Returns a list of local module names.
        """

        localmoduleList = []

        for module in os.listdir(url):
            if not '.svn' in module:
                moduleName = module.split('.')
                if len(moduleName) > 1:
                    ext = moduleName[len(moduleName) - 1]
                    if ext == 'py' or ext == 'yml':
                        localmoduleList.append(module)

        return localmoduleList
    #end

    def get_module_version(self, module):
        """
        Returns the version for a module.
        """

        with open(module, 'r') as currentModule:
            localVersion = currentModule.readlines()[1]
            return self.clean(localVersion)
    #end

    def set_dir(self, dir):
        self.xiinDir = dir
    #end

    def get_dir(self):
        return self.xiinDir
    #end
#end