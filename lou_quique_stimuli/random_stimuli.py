from psychopy import visual, core, event
from psychopy.visual import windowwarp
from gratings import drifting_gratings
from movies import natural_movies
from random import shuffle
import numpy     
import os

mouse = 'quique'
date = 20171214

random_movie_directory = 'C:' + os.sep + 'Quique' + os.sep + 'Random Movies'
imaging_session_directory = 'C:' + os.sep + 'Quique' + os.sep + 'Imaging Sessions' + os.sep + str(date)

movie_repetitions = 1

number_of_movies = 1

idle_color = -1

TTL_color = 1
TTL_time = 5.0

if not os.path.isdir(imaging_session_directory):
	os.mkdir(imaging_session_directory)
	
imaging_session_directory += os.sep + mouse
	
if not os.path.isdir(imaging_session_directory):
	os.mkdir(imaging_session_directory)

movie_order = list(range(number_of_movies))*movie_repetitions
shuffle(movie_order)
print('movie order: ' + str(movie_order))

i = 1

while os.path.isfile(imaging_session_directory + os.sep + mouse + '_random_movie_order_' + str(i) + '.txt'):
    i += 1
    
numpy.savetxt(imaging_session_directory + os.sep + mouse + '_random_movie_order_' + str(i) + '.txt', movie_order)

movies = []

for i in range(1, number_of_movies + 1):
    movies.append(random_movie_directory + os.sep + str(i) + '.mp4')

# make a window for the stimuli
main_window = visual.Window(monitor = 'NLW1', fullscr = True, color = [idle_color, idle_color, idle_color], useFBO = True, screen = 2)

# add a spherical warping
main_warper = windowwarp.Warper(main_window, warp = 'spherical', warpGridsize = 300, eyepoint = [0.5, 0.5], flipHorizontal = False, flipVertical = False)

print('Idling...')

# initialize screen to black before imaging
while True:        
    if event.getKeys(keyList = ['escape']):
        main_window.close()
        core.quit()
    if event.getKeys(keyList = ['space']):
        break

main_window.color = [TTL_color, TTL_color, TTL_color]

print('Starting...')
        
clock = core.Clock()

# set up 5 second bright trigger stimulus to let the imaging know when the VR has started
start = clock.getTime()
end = clock.getTime()

while end - start <= TTL_time:
    end = clock.getTime()
    
    if event.getKeys(keyList = ['escape']):
        main_window.close()
        core.quit()
    if event.getKeys(keyList = ['space']):
        break
    
    main_window.flip()   
    
main_window.color = [0, 0, 0]
main_window.flip()   

print('Presenting movies...')	

for m in movie_order:
    natural_movies(movies[m], blank_time = 3.0, windows = [main_window])

print('Done.')
	
main_window.close()
core.quit()