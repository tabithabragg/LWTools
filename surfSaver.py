# Mass PBR Surfacer suite -> Lightwave surfacer Ver 0.1
# -- utility plugin -- surface to TEXT saver

# I know there are others out there but none of them fit my workflow.
# If I'm going to spend hours adjusting myself to someone else's idea 
# of how to do something, I might as well spend a few of those writing 
# this so I can only have to spend those hours **once** and get back to
# animating.  

# I retain the copyright on this plugin, however am releasing to the 
# Lightwave community to be used, expanded, modified, and generally
# folded, spindled, mutilated, morphed, boned, VDB'd, and rendered. But 
# never fractured.  That thing never worked right and I don't think even 
# Stuart in his heyday could fix it at this point.
# So do what you want with this little plugin but if you distribute it,
# distribute the source so others can use, modify and learn from it. 

# I originally had a whole paragraph here about how Viz and Newtek had 
# given up on Lightwave but as long as we the artists never give up, and 
# keep building onto it with new tools and techniques, it'll live on as 
# long as we do.   But there must have been someone at Viz who woke up 
# with a moment of clarity (rare, I know!) and set our beloved Lightwave 
# go to a new home.   It'll be a long, hard road for our new family at 
# Lightwave Digital, but the family's still here and we're still doing 
# what we've allways done.    Rendering something!  

# I want to give a HUGE shout out and thanks for Ryan Royce for his 
# forum posts and discussions elsewhere, as well as his sample code from
# quite a while back that showed the use of the 
# lwsdk.command("Surf_SaveText") and lwsdk.command("Surf_LoadText") 
# functions.  Without those and quite a few hours doing differential 
# experiments with various surfacing setups, I'd have never figured out
# all the little nuances of building my main template going into version
# 1.0 of this package.   Thank you again, Ryan and all the rest of the 
# community for filling the gaps for us. 

# Unlike several other renditions of this style of plugin out there that
# build surfaces automatically for LW, I am using a trick called a HERE 
# document.  This allows me to craft a very easy to follow and modify
# template that's as close to identical to what comes out of the 
# Surf_SaveText function.   (check the output of TB_SaveSurf.py)
# I'm considering building a template system but that'll come after
# at least the next two sooooper-seeekrit-squirrel projects in the works
# that were the real reason I started this whole adventure in LW python
# in the first place.  

# Wow... that's a lot of comments.  I probably shouldn't write things 
# like this at 4:20am on less than 8 hours sleep in the last 60hours 
# with a major migraine, but I gotta find some way to ignore the pain
# of the migraine and the worst pain of "professional" Java developers
# at my $dayJob. 


# -- This is the header that tells Lightwave "Hey, I'm a plugin!!"
__author__ = 'Tabitha Bragg'
__maintainer__ = 'Tabitha Bragg'
__copyright__ = 'Tabitha Bragg'
__email__ = 'TabithaArt@pm.me'
__date__ = 'May 17, 2023'
__version__ = '0.2'
__status__ = 'Alpha'
__lwver__ = '11'

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
    ('TSB Surface Saver', lwsdk.SRVTAG_BUTTONNAME | lwsdk.LANGID_USENGLISH)
]

ServerRecord = {lwsdk.GenericFactory('TSB Surfacer', MSRF): ServerTagInfo}
