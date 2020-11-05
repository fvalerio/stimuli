from psychopy import visual, core, event
from psychopy.visual import windowwarp
from gratings import drifting_gratings
from movies import natural_movies
from random import shuffle
import datetime
import numpy
import os

from psychopy import visual, monitors
my_monitor = monitors.Monitor(name='NLW1')
my_monitor.setSizePix((1920, 1200))
my_monitor.setWidth(24)
my_monitor.setDistance(100)
my_monitor.saveMon()

mouse = 'vincent'
date = 20201029

imaging_session = '000'
data_set = '000'

grating_type = 'sqr'

warping = False

# natural_movie_directory = 'C:' + os.sep + 'Quique' + os.sep + 'Natural Movies'
# imaging_session_directory = 'C:' + os.sep + 'Quique' + os.sep + 'Imaging Sessions' + os.sep + str(date)

# set the orientations (in degrees) of  the gratings
orientations = numpy.linspace(270.0, 585.0, 8)

# set how many grating cycles you want per degree
spatial_frequencies = [0.05]

# set how many cycles you want per second for the gratings
temporal_frequencies = [1.0, 2.0, 4.0, 8.0, 16.0]

grating_repetitions = 10

movie_repetitions = 5

number_of_movies = 5

idle_color = -1

# if not os.path.isdir(imaging_session_directory):
# 	os.mkdir(imaging_session_directory)
#
# imaging_session_directory += os.sep + mouse
#
# if not os.path.isdir(imaging_session_directory):
# 	os.mkdir(imaging_session_directory)

# file_name = imaging_session_directory + os.sep + mouse + '_' + imaging_session + '_' + data_set + ' grating times.txt'

# set a pseudo-random sequence to show the gratings, images, and movies
grating_order = [[o, s, t] for o in orientations for s in spatial_frequencies for t in temporal_frequencies]*grating_repetitions
shuffle(grating_order)
print('grating order: ' + str(grating_order))

movie_order = list(range(number_of_movies))*movie_repetitions
shuffle(movie_order)
print('movie order: ' + str(movie_order))

# movies = []

# for i in range(1, number_of_movies + 1):
#     movies.append(natural_movie_directory + os.sep + str(i) + '.mp4')

# # make a window for the stimuli
main_window = visual.Window(monitor = 'NLW1', fullscr = True, color = [idle_color, idle_color, idle_color], useFBO = True, screen = 1)

if warping:

	# add a spherical warping
	main_warper = windowwarp.Warper(main_window, warp = 'spherical', warpGridsize = 300, eyepoint = [0.5, 0.5], flipHorizontal = False, flipVertical = False)

print('Ready...')

# initialize screen to black before imaging
# while True:
#     if event.getKeys(keyList = ['escape']):
#         main_window.close()
#         core.quit()
#     if event.getKeys(keyList = ['space']):
#         break

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

grating_times = []

print('Presenting gratings...')

for orientation, spatial_frequency, temporal_frequency in grating_order:
    temp = str(datetime.datetime.now().time())
    temp = temp.split(':')

    time = 0.0

    for i in range(len(temp)):
        time += float(temp[i])*(60.0**i)

    grating_times.append([orientation, spatial_frequency, temporal_frequency, time])

    command = drifting_gratings(grating_type, orientation, spatial_frequency, temporal_frequency, presentation_time = 2.0, blank_time = 3.0, windows = [main_window])

    temp = str(datetime.datetime.now().time())
    temp = temp.split(':')

    time = 0.0

    for i in range(len(temp)):
        time += float(temp[i])*(60.0**i)

    grating_times.append([orientation, spatial_frequency, temporal_frequency, time])

    if command == 'quit':
        # numpy.savetxt(file_name, grating_times)
        main_window.close()
        core.quit()

# numpy.savetxt(file_name, grating_times)

print('Presenting movies...')

for m in movie_order:
    # command = natural_movies(movies[m], blank_time = 3.0, windows = [main_window])

    if command == 'quit':
        main_window.close()
        core.quit()

print('Done.')

main_window.close()
core.quit()
