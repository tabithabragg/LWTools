"""
surface name definition

a_b_...n{_01..x...y} where {_0} is empty
 There will *always* be an entry with no numeric.  This is *BASE* surface name name 
 If there are more than one instance of that surface, they will be numbered _0# .. ####
 assume max 4 digits. More than that tends to (currently) be problematic.
 
example
 bob_house_door
 bob_house_window
 bob_house_window_01
 bob_house_window_02
 sue_hatpin
 leslie_blazer_pocket
 leslie_blazer_cloth
 leslie_blazer_button
 leslie_blazer_button_01
 leslie_blazer_button_02
 leslie_blazer_button_03

Desired functionality

Select all surfaces or groups of surfaces (if no surfaces, assume all surfaces selected)

If user selects "load manual texture set" then:
    open directory and list all files in chosen directory:
        User selects image
        Strip last _xyz of name portion to get basename for image. 
            assumption is last portion _xyz is image "purpose" 
                ie: basecolor, roughness, etc..
            load list of basename_* and build array of IMG_basenames for later use. 

If user selects "automatic assignment" (or something cool sounding)
    open directory and list all files in chosen directory:
        build list of IMG_basenames of image files with last _xyz portion removed
            assumption is last _xzy is purpose of file, ie.. basecolor, etc... 

With arrays of images files, proceed: 
            
If user flag == "base name only" then iterate through list and build array of SRF_basenames.

If user flag =/= "base name only" assume image name include numerics or surface names are unique and match surface names.

determine basename for image textures: 
    ie: leslie_blazer_button_basecolor
        leslie_blazer_button_roughness
        leslie_blazer_button_metalic
        leslie_blazer_button_bump
        leslie_blazer_button_normal
        etc...  (those are most common with refraction, opacity, or occlusion a close second)

Arrays: 

IMG_basename == to be assigned to surface.
SRF_basename == basename of surface without numeric extension if more than one instance of that surface basename present

    If batch *not* selected, assign single image set selected to all selected surfaces. 
        IMG_basename does not need to match SRF_basename

    if batch *is* selected:
        iterate through array of SRF_basename and build selected SRF_basename and SRF_basename_##N surfaces where 
            basenames match.  
                Use other flags set for uvmap, bump strength, transparent vs clip, octane vs native, etc... as appropriate
                save each surface created to "objectname_surfacename_YYYYMMDDhhmm.text" to differentiate it from prior runs if flag is set.
                    if 'preserve surface.txt' not selected, save surace to objectname_basename.txt
 
    


"""