%load chrips

fTarget = "C:\Users\Utilizador\Desktop\chirp_1s.trc";

fileID = fopen(fTarget);
C = textscan(fileID, '%s %s %s %s %s %s %s %s %s %s');
fclose(fileID);

Fs = 192000; %Hz


C = C{2};
C = C(18:end);
D = cellfun(@(x) str2num(x), C);
ts = 0:1/Fs:numel(D)/Fs; ts = ts(1:end-1);
%%
figure; 
subplot(211);
plot(ts, D);
xlabel('time(s)');
ylabel('DAC Amplitude (V)')
subplot(212);
spectrogram(D,128,120,512,Fs, 'yaxis')