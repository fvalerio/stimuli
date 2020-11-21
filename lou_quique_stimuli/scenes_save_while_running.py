# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 19:38:34 2020

@author: Vincent
"""
from psychopy import visual, core, event
import os

def natural_scenes_save(image, presentation_time, blank_time, window):

    image_stimulus = visual.ImageStim(window, opacity = 0.0, size = (1.5*window.size[0]/1.5, 1.5*window.size[1]/1.125), name = 'image_stimulus', autoLog = False, units = 'pix')
#    image_stimulus = visual.ImageStim(window, opacity = 0.0, name = 'image_stimulus', autoLog = False, units = 'pix')

    image_stimulus.setImage(image)

    first = True
    second = True
    
    clock = core.Clock()
	
    while clock.getTime() <= presentation_time + blank_time:
        if clock.getTime() <= presentation_time:
            if first:
                image_stimulus.opacity = 1.0
			
                image_stimulus.draw()
                window.flip()
				
                first = False
                
                # add lines to save presented frames
                window.getMovieFrame('front')
                window.saveMovieFrames(os.path.splitext(image)[0] + '_rescaled.png')
        else:
            if second:
                image_stimulus.opacity = 0.0
				
                image_stimulus.draw()
                window.flip()
				
                second = False
			
        if event.getKeys(keyList = ['escape']):
            return 'quit'
        if event.getKeys(keyList = ['space']):
            return