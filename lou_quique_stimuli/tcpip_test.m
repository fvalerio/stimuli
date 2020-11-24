
ServerSend = tcpip('10.93.14.247',50000,'NetworkRole','server', ...
    'OutputBufferSize', 2);
fopen(ServerSend);

fwrite(ServerSend, uint16(0), 'uint16');
fclose(ServerSend);
fprintf('sent');