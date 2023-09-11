## Comments from the top of surfSaver.py -- rewrite for overall
## surfKit plugin set.

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