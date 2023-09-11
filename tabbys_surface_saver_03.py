# Mass PBR Surfacer suite -> Lightwave surfacer Ver 0.1
# -- utility plugin -- surface to TEXT saver



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
# or you can just send me an M2 
import os, re, shutil


# bunch of variables and setup here *

#begin the fun
Directory = str()

class MSRF(lwsdk.IGeneric):

    def __init__(self, context):
        super(MSRF, self).__init__()

    def process(self, ga):

        def callback(id, data):
            if id == self.Directory:
                value = self.Directory.get_str()

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
        self.panel = self.ui.create('Tabby\'s Lightwave Surface Saver')
        self.Text = self.panel.text_ctl('', ["Select the folder to save the surface file to:"])
        self.panel.align_controls_vertical([self.Text])
        self.panel.size_to_layout(10, 10)
        self.Directory = self.panel.dir_ctl('Save Location', 60)
        self.Directory.set_str(Directory)
        self.Directory.set_event(callback)
        if self.panel.open(lwsdk.PANF_BLOCKING | lwsdk.PANF_CANCEL) == 0:
            print 'Ok, buh bye!! -- Aborted!'
            self.ui.destroy(self.panel)
            return lwsdk.AFUNC_OK
        else:
            OutputPath = str(self.Directory.get_str())
            lwsdk.command("StatusMsg '{" + str(OutputPath) + '}')
            #ScriptPath =  os.path.dirname(os.path.realpath(__file__))
            lwsdk.command("Surf_SaveText \"" + OutputPath + "\\" + SurfName + ".txt" + "\"")

        lwsdk.command("StatusMsg '{}" + SurfName + ".txt saved!!")
        return lwsdk.AFUNC_OK

ServerTagInfo = [
    ('TSB Surface Saver', lwsdk.SRVTAG_USERNAME | lwsdk.LANGID_USENGLISH),
    ('TSB_SRF_Save', lwsdk.SRVTAG_BUTTONNAME | lwsdk.LANGID_USENGLISH)
]

ServerRecord = {lwsdk.GenericFactory('TSB Surface Saver', MSRF): ServerTagInfo}