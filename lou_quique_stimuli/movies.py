from psychopy import visual, core, event
        
def natural_movies(movie, blank_time, windows):
    
    movie_stimuli = []
    
    for window in windows:
        movie_stimuli.append(visual.MovieStim(window, filename = movie, volume = 0.0, loop = False, opacity = 0.0, size = (window.size[0], window.size[1]), name = 'movie_stimulus', autoLog = False, units = 'pix'))

    for movie_stimulus in movie_stimuli:
        movie_stimulus.opacity = 1.0
    
    clock = core.Clock()
    
    while movie_stimulus.duration - clock.getTime() >= 0.1:
        for movie_stimulus in movie_stimuli:
            movie_stimulus.draw()
        
        for window in windows:
            window.flip()
        
        if event.getKeys(keyList = ['escape']):
            return 'quit'
        if event.getKeys(keyList = ['space']):
            return 'skip'
        
    for movie_stimulus in movie_stimuli:
        movie_stimulus.opacity = 0.0
        movie_stimulus.draw()
        
    for window in windows:
        window.flip()
    
    start = clock.getTime()
    end = clock.getTime()
    
    while end - start <= blank_time:
        end = clock.getTime()
        
        if event.getKeys(keyList = ['escape']):
            return 'quit'
        if event.getKeys(keyList = ['space']):
            return 'skip'
            
    return 'continue'