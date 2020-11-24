ServerSend = tcpip('10.93.14.247',50000,'NetworkRole','server', ...
'OutputBufferSize', 2);

time = [];
for i=1:10000
    i
    fopen(ServerSend);
    fwrite(ServerSend, uint16(0), 'uint16');
    time(end+1) = now;
    fclose(ServerSend);
end
