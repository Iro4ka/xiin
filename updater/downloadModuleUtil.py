
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
import urllib2

class DownloadModuleUtil(object):

    def __init__(self, blocksize = 8192):
        self = self
        self.blockSize = blocksize
    #end

    def download(self, source, destination): #moduleURIName):
        """
        Download a new version of a module
        """
        connection  = urllib2.urlopen(source)
        self.set_module_dir(destination)
        
        try:
            with open(destination, 'w') as localFile:
                while True:
                    modLine = connection.read(self.blockSize)
                    if not modLine:
                        break
                    localFile.write(modLine)
            return True
        except:
            return False
    #end

    def set_block_size(self, blocksize):
        self.blockSize = blocksize
    #end

    def get_block_size(self):
        return self.blockSize
    #end

    def set_module_dir(self, destination):
        """
        Creates a place for xiin modules if the folder doesn't exist.
        """
        directory = os.path.dirname(destination)
        if not os.path.isdir(directory):
            os.makedirs(directory)
    #end
#end