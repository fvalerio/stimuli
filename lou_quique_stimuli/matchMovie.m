function matchMovie()

    %MATCHMOVIE() Prepares videos in .MP4 format for PsychoPy presentation.
    %   MATCHMOVIE() converts videos in .MP4 format to grayscale and matches their mean and variance in luminance.
    
    try
        [movieName, moviePath] = uigetfile('.mp4', 'Please select movie.');
    catch
        waitfor(msgbox('Error: Please select valid movie.'));
        error('Please select valid movie.');
    end

    try
        movie = VideoReader([moviePath, movieName]);
    catch
        waitfor(msgbox('Error: Could not read movie.'));
        error('Could not read movie.');
    end

    % set the start and finish of the movie in seconds
    crop = [0, movie.Duration];

    % create new video object with same framerate as original and matched luminances between frames
    matchedMovie = VideoWriter([moviePath, 'matched_', movieName], 'MPEG-4');
    matchedMovie.FrameRate = movie.FrameRate;
    open(matchedMovie);

    % reassure user that all is well
    disp('Converting to gray-scale and matching luminance...');

    start = crop(1);
    finish = crop(2);

    movie.CurrentTime = start;

    if finish > movie.Duration
        finish = movie.Duration;
    end

    while movie.CurrentTime <= finish
        image = cell(1, 1);

        try
            image{1} = readFrame(movie);
        catch
            if movie.CurrentTime == movie.Duration
                break
            else
                waitfor(msgbox('Error: Ran out of frames.'));
                error('Ran out of frames.');
            end
        end
        
        % the monitor doesn't support resolutions above 1080p, so why bother
        if size(image{1}, 1) > 1080
            image{1} = imresize(image{1}, [1080, 1080*(size(image{1}, 2)/size(image{1}, 1))]);
        end

        image{1} = rgb2gray(image{1});
        image = lumMatch(image, [], [127.5, 72.1249]);

        % write frames to new video
        writeVideo(matchedMovie, image{1});
    end

    close(matchedMovie);

    % reassure user
    disp('Done.');

end