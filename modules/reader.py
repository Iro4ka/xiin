
__version__     = '2011.07.12-01'
__author__      = 'Scott Rogers, aka trash80'
__stability__   = 'alpha'
__copying__     = """Copyright (C) 2011 W. Scott Rogers \
                        This program is free software.
                        You can redistribute it and/or modify it under the terms of the
                        GNU General Public License as published by the Free Software Foundation;
                        version 2 of the License.
                    """
import os
from spinner import Spinner

################################################################################
####
####        Main xiin class
####
################################################################################

class Reader(object):

    def __init__(self):
        self = self
    #end

    def info(self, xiinArgDict):
        """
        Walks the directory.
        """
        print("Getting info")
        print('')

        spinner = Spinner()

        count = 1

        for root, dirs, files in os.walk(xiinArgDict.directory):
            for file in files:
                xiinArgDict.fullPathFile = os.path.join(root, file)
                self.__readFile(xiinArgDict)
                # show spinner when writing files
                if not xiinArgDict.display:
                    spinner.render(count)
                    count = count + 1
    #end

    def __readFile(self, xiinArgDict):
        """
        Opens a file and prep to read.
        """
        try:
            if os.stat(xiinArgDict.fullPathFile).st_size:
                with open(xiinArgDict.fullPathFile, 'r') as xiinArgDict.key:
                    _hash = self.__hash(xiinArgDict)
                    if xiinArgDict.display:
                        print(_hash)
                    elif xiinArgDict.filename is not None:
                        xiinArgDict.outputFile.writelines(_hash)
                    else:
                        print('ERROR: Nothing to do')
                        exit(8)
        except:
            pass
    #end

    def __hash(self, xiinArgDict):
        """
        Returns a key[ directory ]:value [contents] hash.
        """
        _hash = ''

        try:
            return '{0}:{1}\n'.format(
                str(xiinArgDict.fullPathFile),
                str(xiinArgDict.key.readlines()).replace('\\n','')
            )
        except:
            pass

        return _hash
    #end
#end