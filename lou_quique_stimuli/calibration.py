from psychopy import monitors
from matplotlib import pyplot
from scipy import optimize
import numpy

def calculate_gamma():

    def monitor_function(x, a, b, c, d):
        return a*((x + b)**c) + d
    
    # gamma = 1.95
    # brightness 24%
    # contrast 88%
    
    # test
    stimulus_input = numpy.linspace(0, 1, 5)
    corrected_output = numpy.array([0.8, 25.3, 49.5, 83.8, 112.0])
        
    # data collected at 30% brightness, 88% contrast
    #stimulus_input = numpy.linspace(0, 1, 5)
    #corrected_output = numpy.array([1.1, 1.2, 8.1, 38.8, 111.5])
    
    # data collected at %60 brightness, %50 contrast
    #stimulus_input = numpy.linspace(0, 1, 3)
    #corrected_output = numpy.array([1.4, 27.8, 100.7])
    
    # data collected at 25% brightness, 75% contrast
    #stimulus_input = numpy.linspace(0, 1, 21)
    #corrected_output = numpy.array([0.8, 0.8, 0.8, 0.8, 0.8, 1.1, 1.8, 3.0, 4.5, 6.6, 9.0, 12.3, 16.4, 21.4, 26.8, 34.1, 42.9, 53.5, 70.9, 93.4, 103.6])
    
    pyplot.plot(stimulus_input, corrected_output)
    
    # this is for the old monitor
    #corrected_output = numpy.array([1.0, 3.0, 6.0, 11.0, 18.0, 26.0, 38.0, 51.0, 66.0, 83.0, 104.0])
    
    #minimum = numpy.min(corrected_output)
    #maximum = numpy.max(corrected_output)
    
    #corrected_output[:] = corrected_output[:] - (maximum - 3.0*minimum)/2.0
    
    #corrected_output[:] = corrected_output[:]/numpy.max(corrected_output)
    
    #parameters, covariance = optimize.curve_fit(monitor_function, stimulus_input, corrected_output, p0 = [1.0, 1.0, 2.0, -0.5])
    
    table = monitors.GammaCalculator(inputs = stimulus_input, lums = corrected_output)
    
    return table.gamma

def calibrate_monitor(name, width, distance, gamma, screen_resolution = [1920, 1080]):
    
    monitor = monitors.Monitor(name, width = width, distance = distance, gamma = gamma)
    
    monitor.setSizePix(screen_resolution)
    
    monitor.saveMon()