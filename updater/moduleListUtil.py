
__version__     = '2011.07.10-00'
__author__      = 'Scott Rogers, aka trash80'
__stability__   = 'alpha'
__copying__     = """Copyright (C) 2011 W. Scott Rogers \
                        This program is free software.
                        You can redistribute it and/or modify it under the terms of the
                        GNU General Public License as published by the Free Software Foundation;
                        version 2 of the License.
                    """

from remoteModuleUtil import RemoteModuleUtil
from localModuleUtil import localModuleUtil
from baseModuleUtil import ModuleUtil

class List(ModuleUtil):
    """
    Compare the list of server module versions with local module version. Return
    a list of out of date modules.
    """

    def __init__(self):
        self = self
    #end

    def build_list(self, localModuleDict, remoteModuleDict):
        """
        Compare the versions of local and server modules to create a list of
        outdated modules.
        """

        downloadList = []

        # if localModuleDict is empty, then we need all the modules

        for module in remoteModuleDict:
            # module doesn't exist locally
            if len(localModuleDict) == 0 or module not in localModuleDict:
                downloadList.append(module)
            else:
                localVersion    = self.convertToDate(localModuleDict[module])
                remoteVersion   = self.convertToDate(remoteModuleDict[module])
                
                # compare versions
                if localVersion[0] == remoteVersion[0]:
                    # compare patch number
                    if localVersion[1] < remoteVersion[1]:
                        downloadList.append(module)

                if localVersion[0] < remoteVersion[0]:
                    downloadList.append(module)

        return downloadList
    #end

    def get_list(self, localUrl, remoteUrl):
        """
        Returns a list of modules requiring updates.
        """
        localModule         = localModuleUtil()
        remoteModule        = RemoteModuleUtil()
        remoteModuleDict    = remoteModule.get_module_dict(remoteUrl)
        localModuleDict     = localModule.get_module_dict(localUrl)
        downloadList        = self.build_list(localModuleDict, remoteModuleDict)

        return downloadList
    #end
#end