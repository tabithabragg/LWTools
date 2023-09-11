# Mass PBR Surfacer suite -> Lightwave surfacer Ver 0.1
# -- utility plugin -- surface to TEXT saver

# Loads a surface from the plaintext file saved from the
# 'TSB Surface Saver' plugin. 
# 
# Select the surface you want to update and activate this
# plugin.  It will ask you to select the surface file to load.
# NOTE:  This will **OVERWRITE** the current selected surface.
#

# This and the Saver plugin are based very heavily on the 
# great sample plugin by Ryan Royce.  Without the aweomse
# community of devs and artists dedicated to Lightwave, we 
# would never have survived the Dark Times of the post CORE
# apocalypse at Newtek.


# -- This is the header that tells Lightwave "Hey, I'm a plugin!!"
__author__ = 'Tabitha Bragg'
__maintainer__ = 'Tabitha Bragg'
__copyright__ = 'Tabitha Bragg'
__email__ = 'TabithaArt@pm.me'
__date__ = 'Sept 1, 2023'
__version__ = '0.2'
__status__ = 'Alpha'
__lwver__ = '11'
# need to find out what lwver to put since this is 2018+ only


import lwsdk
import os

# Select the first surface in the selected object.
UserSelection = lwsdk.LWInterfaceInfo().selected_items()[0]

#begin the fun
Directory = str()
SurfFile = str()

class MSRF(lwsdk.IGeneric):

    def __init__(self, context):
        super(MSRF, self).__init__()

    def process(self, ga):

        def callback(id, data):
            if id == self.SurfFile:
                value = self.SurfFile.get_str()

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
        self.SurfFile = self.panel.dir_ctl('Surface File', 60)
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
            lwsdk.command("Surf_LoadText \"" + OutputPath + "\\" + SurfName + ".txt" + "\"")

        lwsdk.command("StatusMsg '{}" + SurfName + ".txt loaded!!")
        return lwsdk.AFUNC_OK

ServerTagInfo = [
    ('TSB Surface Loader', lwsdk.SRVTAG_USERNAME | lwsdk.LANGID_USENGLISH),
    ('TSB Surface Loader', lwsdk.SRVTAG_BUTTONNAME | lwsdk.LANGID_USENGLISH)
]

ServerRecord = {lwsdk.GenericFactory('TSB Surface Loader', MSRF): ServerTagInfo}

#ScriptPath = os.path.dirname(os.path.realpath(__file__))
#f=open(ScriptPath + "\\SurfaceData.txt","w")
#f.write(NodeBuild)
#lwsdk.command("Surf_SaveText \"" + ScriptPath + "\\SurfaceData.txt" + "\"")
# Seek is needed to ensure Python finishes writing the file before any more lines are executed.
#f.seek(0)

#f.close

# With file written, apply the surface file to the currently selected surface.
lwsdk.command("Surf_LoadText \"" + ScriptPath + "\\SurfaceData.txt" + "\"")