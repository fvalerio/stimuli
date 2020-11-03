from psychopy import visual, core, event

def drifting_gratings(grating_type, orientation, spatial_frequency, temporal_frequency, presentation_time, blank_time, windows):
    
    grating_stimuli = []
    
    for window in windows:
        grating_stimuli.append(visual.GratingStim(window, contrast = 0.8, tex = grating_type, sf = spatial_frequency, opacity = 0.0, size = (2.0*window.size[0], 2.0*window.size[1]), name = 'grating_stimulus', autoLog = False, units = 'deg'))

    orientation_flip = False
    for grating_stimulus in grating_stimuli:
        if orientation == 360 or orientation == 540:
            if orientation_flip:
                grating_stimulus.ori = orientation + 180
                orientation_flip = False
            else:
                grating_stimulus.ori = orientation
                orientation_flip = True
        elif  orientation == 315 or orientation == 495:
            if orientation_flip:
                grating_stimulus.ori = orientation - 90
                orientation_flip = False
            else:
                grating_stimulus.ori = orientation
                orientation_flip = True
        elif  orientation == 405 or orientation == 585:
            if orientation_flip:
                grating_stimulus.ori = orientation + 90
                orientation_flip = False
            else:
                grating_stimulus.ori = orientation
                orientation_flip = True
        else:
            grating_stimulus.ori = orientation
    
    first = True
    second = True
    
    clock = core.Clock()
    
    while clock.getTime() <= presentation_time + blank_time:
        if clock.getTime() <= presentation_time:
            if first:
                for grating_stimulus in grating_stimuli:
                    grating_stimulus.opacity = 1.0
                
                first = False
                
            for grating_stimulus in grating_stimuli:
                grating_stimulus.phase = clock.getTime()*temporal_frequency
                grating_stimulus.draw()
                
            for window in windows:
                window.flip()
    
        else:
            if second:
                for grating_stimulus in grating_stimuli:
                    grating_stimulus.opacity = 0.0
                    grating_stimulus.draw()
                
                second = False
            
            for window in windows:
                window.flip()   
        
        if event.getKeys(keyList = ['escape']):
            return 'quit'
        if event.getKeys(keyList = ['space']):
            return 'skip'
            
    return 'continue'