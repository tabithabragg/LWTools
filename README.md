# LWTools

This repository is the home of my Lightwave 3D python plugins and other tools and toys I am developing to better (re)integrate Lightwave into a greatly expanded toolchain and workflow.    

To install: 

Download the following files to wherever you store your 3rd party lW plugins.  Since these are in pre-alpha state, I recommend a seperate location than your production plugin set.  But that's up to you.  

  The plugins will show up in Lightwave as: 
    TSB Surface Loader 
    TSB Surface Saver 

tabbys_surface_loader_02.py 
tabbys_surface_saver_03.py

Add them to Layout the same as you would any Lightwave plugin.  

You can add them to a button, if you want.   I call them with  ctrl-space then type tsb and select which one I want.  

To Use:  

Saver: 
  select the single surface you want to save to a text sufrace file: 
  activate the TSB Surface Saver plugin
  Select the directory to save your surface file to.
  modify the filename from <selectedsurface>.txt if you desire. 
  hit ok. 

Loader:
  select the single sufrace you want to load a surface text file saved from TSB Surface Saver plugin onto
  activate the tSB Surface Loader plugin
  Select the file to load. 
  hit ok.
  Lightwave will prompt you to find images if they are not in the path listed in the surface text file, the same as if you loaded an object that
    references images it can't find.  
  


added: Sept 11, 2023

tabbys_surface_loader_02.py
  Initial version is functioal and has been tested on a basic object and surface under LW 2020.0.3.  Further testing with Octane surfaces and other versions needed. 

test_project 
  this is a test lW project that contains 
    scenes -- scene file 
    objects -- lw and obj objects of a cube.   lW obj has a pbsdf nodal surface.  obj version was used in substance painter to make a pretty surface for it.
    images -- the pbr images needed for the surface.  these were exported from substance painter using the ASM - PBR Metallic Roughness (starter_assets) template
    substance -- the substance painter file (.spp) for this project.  For my sins, I'm on the latest Adobe cloud version:  9.0.0.2585
    Surfaces -- this is where I saved the .txt vesion of the surface definition to.   You can save it anywhere.  The saver defaults to the surface name, but you 
                have the opportunity to modify that before hitting OK.  

Two new files added on Sept 10, 2023: 

tabbys_surface_saver_02.py
  saves the selected surface to the chosen directory and filename instead of defaulting to plugin location and surface.txt
  loader should be ready in a day or two if I have time tomorrow to fix one thing in it.  Like how to spawn a "file selection" dialog
  instead of a "directory selection" dialog.   Python docs here really are an adventure.  <grin>

surfacing_logic_flow_001.py
  this is just a comment block that's an 'stream of consciousness' attempt to get the logic flow for how to parse surface names, image names
  user selections and a few other bits of logic that I want to implement in this.   Expect this file to grow and change over time.  And I really
  really, really miss my translucent green 1970s era IBM programming logic flow templates.  May have to hit ebay to dig one up.   
