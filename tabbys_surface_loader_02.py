# Mass PBR Surfacer suite -> Lightwave surfacer Ver 0.1
# -- utility plugin -- loads TEXT version of surface 
#                       saved by TSB Surface Saver

# -- This is the header that tells Lightwave "Hey, I'm a plugin!!"
__author__ = 'Tabitha Bragg'
__maintainer__ = 'Tabitha Bragg'
__copyright__ = 'Tabitha Bragg'
__email__ = 'TabithaArt@pm.me'
__date__ = 'Sept 10, 2023'
__version__ = '0.3'
__status__ = 'Alpha'
__lwver__ = '2018'
# need to figure out proper version for lw2018+ 
# also need to make a version, if possible, for lw2015 and earlier

# Yeah...  pull in all that juicy sdk library goodness
import lwsdk

# lwsdk.pris has some simple goodies.  These let you store and recall plugin
# state and variables betweeen calls.  May add more later as needed. 
from lwsdk.pris import globalrecall, globalstore

# Oh yeah... need  some goodies from the Operating system side. 
# shutil == high level file handling
# re == regex (ugh... can't get away from it sometimes...)
# os == make it OS agnostic.  yeah... should let it run on OS-X.  Need testers!!!
# or you can just send me an M2 Mac
import os, re, shutil


# bunch of variables and setup here *

#begin the fun
FileName = str()

class MSRF(lwsdk.IGeneric):

    def __init__(self, context):
        super(MSRF, self).__init__()

    def process(self, ga):

        def callback(id, data):
            if id == self.FileName:
                value = self.FileName.get_str()

        UserObjSelect = []
        UserSurfSelect = []
        SufName = []
        # https://static.lightwave3d.com/sdk/2020/python/globalsurfedfuncs.html?highlight=lwsurfedfuncs#lwsdk.LWSurfEdFuncs.getSelection
        SurfID = lwsdk.LWSurfEdFuncs().getSelection(-1)
        if not SurfID:
                lwsdk.command("StatusMsg '{}Select a Surface!!!")
                return 0
        UserObjSelect = lwsdk.LWInterfaceInfo().selected_items()[0]
        # https://static.lightwave3d.com/sdk/2020/python/globalsurfacefuncs.html?highlight=lwsurfacefuncs#lwsdk.LWSurfaceFuncs.name
        UserSurfSelect = lwsdk.LWSurfaceFuncs().name(SurfID)
        SurfName = UserSurfSelect

        self.ui = lwsdk.LWPanels()
        self.panel = self.ui.create('Tabby\'s Lightwave Surface Loader')
        self.Text = self.panel.text_ctl('', ["Select the surface file to load:"])
        self.panel.align_controls_vertical([self.Text])
        self.panel.size_to_layout(10, 10)
        self.FileName = self.panel.file_ctl('Load File', 60)
        self.FileName.set_str(FileName)
        self.FileName.set_event(callback)
        if self.panel.open(lwsdk.PANF_BLOCKING | lwsdk.PANF_CANCEL) == 0:
            print 'Ok, buh bye!! -- Aborted!'
            self.ui.destroy(self.panel)
            return lwsdk.AFUNC_OK
        else:
            FileSRFName = str(self.FileName.get_str())
            lwsdk.command("StatusMsg '{" + str(FileSRFName) + '}')
            #ScriptPath =  os.path.dirname(os.path.realpath(__file__))
            lwsdk.command("Surf_LoadText \"" + FileSRFName +"\"")
            #lwsdk.command("Surf_SaveText \"" + OutputPath"\"")

        lwsdk.command("StatusMsg '{}" + SurfName + "updated!!")
        return lwsdk.AFUNC_OK

ServerTagInfo = [
    ('TSB Surface Loader', lwsdk.SRVTAG_USERNAME | lwsdk.LANGID_USENGLISH),
    ('TSB_SRF_Load', lwsdk.SRVTAG_BUTTONNAME | lwsdk.LANGID_USENGLISH)
]

ServerRecord = {lwsdk.GenericFactory('TSB Surface Loader', MSRF): ServerTagInfo}