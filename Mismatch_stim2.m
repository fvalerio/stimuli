function varargout = Mismatch_stim2(varargin)
% MISMATCH_STIM2 MATLAB code for Mismatch_stim2.fig
%      MISMATCH_STIM2, by itself, creates a new MISMATCH_STIM2 or raises the existing
%      singleton*.
%
%      H = MISMATCH_STIM2 returns the handle to a new MISMATCH_STIM2 or the handle to
%      the existing singleton*.
%
%      MISMATCH_STIM2('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in MISMATCH_STIM2.M with the given input arguments.
%
%      MISMATCH_STIM2('Property','Value',...) creates a new MISMATCH_STIM2 or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before Mismatch_stim2_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to Mismatch_stim2_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help Mismatch_stim2

% Last Modified by GUIDE v2.5 17-Nov-2020 22:53:10

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @Mismatch_stim2_OpeningFcn, ...
                   'gui_OutputFcn',  @Mismatch_stim2_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before Mismatch_stim2 is made visible.
function Mismatch_stim2_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to Mismatch_stim2 (see VARARGIN)

% Choose default command line output for Mismatch_stim2
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes Mismatch_stim2 wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = Mismatch_stim2_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;



function edit1_Callback(hObject, eventdata, handles)
% hObject    handle to edit1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit1 as text
%        str2double(get(hObject,'String')) returns contents of edit1 as a double


% --- Executes during object creation, after setting all properties.
function edit1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function edit2_Callback(hObject, eventdata, handles)
% hObject    handle to edit2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit2 as text
%        str2double(get(hObject,'String')) returns contents of edit2 as a double


% --- Executes during object creation, after setting all properties.
function edit2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function edit3_Callback(hObject, eventdata, handles)
% hObject    handle to edit3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit3 as text
%        str2double(get(hObject,'String')) returns contents of edit3 as a double


% --- Executes during object creation, after setting all properties.
function edit3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in pushbutton1.
function pushbutton1_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
saveTrials = get(handles.checkbox2,'Value');
if saveTrials == 0
    asw = questdlg('You are NOT saving this trial. Are you sure this is right?');
    switch asw
        case 'Yes'
            disp ('As you command. I am only here to serve to my true master. YOU')
        case 'No'
            return
        case 'cancel'
            return
    end
end
directory = get(handles.edit1, 'String');


angles1 = [315 15 345 45];
angles2 = [0; 60; 30; 90];
angles3 = [90; 150; 120; 180];
angles4 = [180; 240; 210; 270];

duration  = str2double(get(handles.edit3, 'String'));


PsychDefaultSetup(2);
screenNumber = max(Screen('Screens'));
Screen('Preference', 'SkipSyncTests', 1);

white = WhiteIndex(screenNumber);
grey = white / 2;
black = BlackIndex(screenNumber);

[window, windowRect] = PsychImaging('OpenWindow', screenNumber, grey, [], 32, 2,...
    [], [],  kPsychNeed32BPCFloat);

Screen('Flip', window);

ifi = Screen('GetFlipInterval', window);

topPriorityLevel = MaxPriority(window);

[xCenter, yCenter] = RectCenter(windowRect);

gaborDimPixX = windowRect(3);
gaborDimPixY = windowRect(4);

sigma = gaborDimPixX;

contrast = 1;
aspectRatio = 5;

numCycles = 6;
freq = numCycles / gaborDimPixX;

% Build a procedural gabor texture
gabortex = CreateProceduralGabor(window, gaborDimPixX, gaborDimPixY,...
    [], [1 1 1 0.5], 1, 100);

dim = 8;
[x, y] = meshgrid(-dim:dim, -dim:dim);

% Calculate the distance in "Gabor numbers" of each gabor from the center
% of the array
dist = sqrt(x.^2 + y.^2);

% Cut out an inner annulus
innerDist = 3.5;
x(dist <= innerDist) = nan;
y(dist <= innerDist) = nan;

% Cut out an outer annulus
outerDist = 10;
x(dist >= outerDist) = nan;
y(dist >= outerDist) = nan;

% Select only the finite values
x = x(isfinite(x));
y = y(isfinite(y));

% Center the annulus coordinates in the centre of the screen
xPos = x .* gaborDimPixX + xCenter;
yPos = y .* gaborDimPixY + yCenter;

% Count how many Gabors there are
nGabors = numel(xPos);

% Make the destination rectangles for all the Gabors in the array
baseRect = [0 0 gaborDimPixX gaborDimPixY];
allRects = nan(4, nGabors);

for i = 1:nGabors
    allRects(:, i) = CenterRectOnPointd(baseRect, xPos(i), yPos(i));
end
tFreq = 2;
degPerSec = 360 * tFreq;
degPerFrame =  degPerSec * ifi;

% Randomise the Gabor orientations and determine the drift speeds of each gabor.
% This is given by multiplying the global motion speed by the cosine
% difference between the global motion direction and the global motion.
% Here the global motion direction is 0. So it is just the cosine of the
% angle we use. We re-orientate the array when drawing
gaborAngles = 0; % rand(1, nGabors) .* 180 - 90;
degPerFrameGabors = cosd(gaborAngles) .* degPerFrame;

% Randomise the phase of the Gabors and make a properties matrix. We could
% if we want have each Gabor with different properties in all dimensions.
% Not just orientation and drift rate as we are doing here.
% This is the power of using procedural textures
phaseLine = 0.5;% rand(1, nGabors) .* 360;
propertiesMat = repmat([NaN, freq, sigma, contrast, aspectRatio, 0, 0, 0],...
    nGabors, 1);
propertiesMat(:, 1) = phaseLine';

vbl = Screen('Flip', window);

waitframes = 1;

timerGlobal = tic;

trig = get(handles.checkbox1,'Value');
l = 1;
loops = str2double(get(handles.edit2, 'String'));

angles1 = repmat(angles1, loops, 1);
RandStream('dsfmt19937');
y = datasample(1:loops,loops, 'Replace', false);
p = str2double(get(handles.edit5, 'String'));
nv = loops*(p/100);
idx  = find(y <= nv);
angles1(idx, 2) = -1;

while l <= loops
    if l == 1 && trig == 1
        ServerSend = tcpip('10.93.15.144',50000,'NetworkRole','server', ...
            'OutputBufferSize', 2);
        fopen(ServerSend);
        fwrite(ServerSend, uint16(0), 'uint16');
        fclose(ServerSend);
        delete(ServerSend);
        ServerSend = [];
        timerGlobal = tic;
        newStim = 0;
    elseif l == 1 && trig == 0
        timerGlobal = tic;
        newStim = 0;
    end
    tb  = tic;
    cb = 0;
    while toc(tb) < duration
        cb = cb + 1;
        if cb == 1
            Screen('FillRect', window, [0 0 0]);
            Screen('Flip', window, 0, 1);
            newStim = newStim + 1;
            Stim.ID{newStim} = 'black';
            Stim.timing(newStim) = toc(timerGlobal);
        end
    end
    for i = 1: size(angles1, 2)
        count = 0;
        timerval = tic;
        while toc(timerval) < duration
            count = count +1;
            if count ==  1
                if angles1(l,i) == -1
                    Screen('FillRect', window, [0.5 0.5 0.5]);
                    Screen('Flip', window, 0, 1);
                    newStim = newStim + 1;
                    Stim.ID{newStim} = 'omission';
                    Stim.timing(newStim) = toc(timerGlobal);
                else
                    Screen('BlendFunction', window, 'GL_ONE', 'GL_ZERO');
                    Screen('DrawTexture', window, gabortex, [], [], angles1(l,i),...
                        [], [], [], [], kPsychDontDoRotation, propertiesMat');
                    Screen('Flip', window, 0, 1);
                    newStim = newStim + 1;
                    Stim.ID{newStim} = angles1(i);
                    Stim.timing(newStim) = toc(timerGlobal);
                end
            end
        end
    end
    l = l +1;
end

if saveTrials == 1
    currentCounterValue = str2double(get(handles.edit4, 'String'));
    newString = sprintf('%d', int32(currentCounterValue +1));
    set(handles.edit4, 'String', newString );
    Stim.trialNumber = currentCounterValue;
    Folder = '\Stim';
    filename = ['\' num2str(currentCounterValue)];
    if ~exist([directory Folder], 'dir')
        mkdir([directory Folder])
    end
    save([directory Folder filename], 'Stim')
end

sca;
% --- Executes on button press in checkbox1.
function checkbox1_Callback(hObject, eventdata, handles)
% hObject    handle to checkbox1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of checkbox1


% --- Executes on button press in checkbox2.
function checkbox2_Callback(hObject, eventdata, handles)
% hObject    handle to checkbox2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of checkbox2



function edit4_Callback(hObject, eventdata, handles)
% hObject    handle to edit4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit4 as text
%        str2double(get(hObject,'String')) returns contents of edit4 as a double


% --- Executes during object creation, after setting all properties.
function edit4_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function edit5_Callback(hObject, eventdata, handles)
% hObject    handle to edit5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit5 as text
%        str2double(get(hObject,'String')) returns contents of edit5 as a double


% --- Executes during object creation, after setting all properties.
function edit5_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end
