
__version__     = '2011.07.10-00'
__author__      = 'Scott Rogers, aka trash80'
__stability__   = 'alpha'
__copying__     = """Copyright (C) 2011 W. Scott Rogers \
                        This program is free software.
                        You can redistribute it and/or modify it under the terms of the
                        GNU General Public License as published by the Free Software Foundation;
                        version 2 of the License.
                    """

from moduleListUtil import List
from remoteModuleUtil import RemoteModuleUtil
from downloadModuleUtil import DownloadModuleUtil

class SelfUpdate(object):
    
    def __init__(self):
        self = self
    #end

    def update(self, localUrl, remoteUrl):
        updater         = DownloadModuleUtil()
        modList         = List()
        modUpdateList   = modList.get_list(localUrl, remoteUrl)

        if len(modUpdateList) > 0:
            for modUpdate in modUpdateList:
                updater.download(remoteUrl + modUpdate, localUrl + modUpdate)
    #end

    def update_all(self, localUrl, remoteUrl):
        updater         = DownloadModuleUtil()
        remoteModule    = RemoteModuleUtil()
        modUpdateList   = remoteModule.get_module_list(remoteUrl)

        for modUpdate in modUpdateList:
            updater.download(remoteUrl + modUpdate, localUrl + modUpdate)
    #end
#end
