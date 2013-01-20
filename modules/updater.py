

def __update_xiin(self):
    """
    Update all modules to the newest versions.d
    """
    # update xiin modules
    update = SelfUpdate()
    update.update_all(self.localUrl, self.remoteUrl)
#end

################################################################################
####
####        xiin self updater class
####
################################################################################

class SelfUpdate(object):

    def __init__(self, blocksize = 1024):
        self = self
        self.blockSize = blocksize
        self.modUpdateList = ['base.py', 'PythonVersionCheck.py', 'reader.py', 'spinner.py', 'uploader.py']
    #end

    def update_all(self, localUrl, remoteUrl):
        """
        Iterates over the module list.
        """
        for modUpdate in self.modUpdateList:
            self.download(remoteUrl + modUpdate, localUrl + modUpdate)
    #end

    def download(self, source, destination):
        """
        Download a module.
        """
        import urllib2
        connection  = urllib2.urlopen(source)
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
#end