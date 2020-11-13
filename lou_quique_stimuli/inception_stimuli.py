'''
Adapted from Quique's visual_stimuli.py

@author: Vincent
'''

from psychopy import visual, core, event
from psychopy.visual import windowwarp
from gratings import drifting_gratings
from movies import natural_movies
from scenes import natural_scenes
from random import shuffle
import datetime
import numpy
import os
import random

#from psychopy import visual, monitors
#my_monitor = monitors.Monitor(name='NLW1')
#my_monitor.setSizePix((1920, 1200))
#my_monitor.setWidth(24)
#my_monitor.setDistance(100)
#my_monitor.saveMon()

mouse = 'vincent'
date = 20201106

imaging_session = '000'
data_set = '003'

grating_type = 'sqr'

warping = False

image_directory = 'C:' + os.sep + 'Vincent' + os.sep + 'test_grayscale'
imaging_session_directory = 'C:' + os.sep + 'Vincent' + os.sep + 'Imaging Sessions' + os.sep + str(date)
imaging_session_directory += os.sep + mouse

number_of_movies = 50
movie_repetitions = 10

idle_color = -1

# 
movies = []
for file in os.listdir(image_directory):
    if file.lower().endswith(".jpeg"):
        movies.append(file)

# create the directory to save the data file to
if not os.path.isdir(imaging_session_directory):
 	os.makedirs(imaging_session_directory)

file_name = imaging_session_directory + os.sep + mouse + '_' + imaging_session + '_' + data_set + ' image_times.txt'

# set a pseudo-random sequence to show the images
movie_order = list(range(number_of_movies))*movie_repetitions
shuffle(movie_order)
print('movie order: ' + str(movie_order))

# # make a window for the stimuli
main_window = visual.Window(monitor = 'NLW1', fullscr = True, color = [idle_color, idle_color, idle_color], useFBO = True, screen = 1)

# if warping:
# 	# add a spherical warping
# 	main_warper = windowwarp.Warper(main_window, warp = 'spherical', warpGridsize = 300, eyepoint = [0.5, 0.5], flipHorizontal = False, flipVertical = False)

stimulus = image_directory + os.sep + movies[1]


print('Ready...')

# initialize screen to black before imaging
while True:
    if event.getKeys(keyList = ['escape']):
        main_window.close()
        core.quit() 
    if event.getKeys(keyList = ['space']):
        break

print('Initializing...')

main_window.color = [0, 0, 0]

clock = core.Clock()

# wait for 10 seconds to let scanbox start scanning
start = clock.getTime()
end = clock.getTime()

while end - start <= 10.0:
    end = clock.getTime()

    if event.getKeys(keyList = ['escape']):
        main_window.close()
        core.quit() 
    if event.getKeys(keyList = ['space']):
        break

main_window.flip()

print('Presenting images...')

grating_times = []

for m in movie_order:
    temp = str(datetime.datetime.now().time())
    temp = temp.split(':')

    time = 0.0

    for i in range(len(temp)):
        time += float(temp[i])*(60.0**i)

    # grating_times.append([movies[m], time])
    grating_times.append([str(movies[m]), time])

    blank = float(random.randrange(300,500)) / 1000
    print(blank)
    command = natural_scenes(image_directory + os.sep + movies[m], presentation_time = 0.5, blank_time = blank, window = main_window)

    temp = str(datetime.datetime.now().time())
    temp = temp.split(':')

    time = 0.0

    for i in range(len(temp)):
        time += float(temp[i])*(60.0**i)

    grating_times.append([str(movies[m]), time])

    if command == 'quit':
        numpy.savetxt(file_name, grating_times, fmt='%s')
        main_window.close()
        core.quit()

numpy.savetxt(file_name, grating_times, fmt='%s')

print('Done.')

main_window.close()
core.quit()
