%% Import data from text file
% Script for importing data from the following text file:
%
%    filename: D:\Programowanie\Python\pl-vACC-VS-CLStats\statistics.csv
%
% Auto-generated by MATLAB on 19-Mar-2021 00:43:24

%% Set up the Import Options and import the data
opts = delimitedTextImportOptions("NumVariables", 4);

% Specify range and delimiter
opts.DataLines = [2, Inf];
opts.Delimiter = ",";

% Specify column names and types
opts.VariableNames = ["Timestamp", "Departure", "Arrival", "Altitude"];
opts.VariableTypes = ["categorical", "categorical", "categorical", "double"];

% Specify file level properties
opts.ExtraColumnsRule = "ignore";
opts.EmptyLineRule = "read";

% Specify variable properties
opts = setvaropts(opts, ["Timestamp", "Departure", "Arrival", "Altitude"], "EmptyFieldRule", "auto");

% Import the data
statistics = readtable("D:\Programowanie\Python\pl-vACC-VS-CLStats\statistics.csv", opts);


%% Clear temporary variables
clear opts
%% Draw histogram with F365 boundary
subplot(4,2,1);
histogram(statistics.Altitude/100, [0 365 660]);
xlabel('Cruising Level [FL]')
ylabel('Number of flight plans')
title("F365")
%% Draw histogram with F355 boundary
subplot(4,2,2);
histogram(statistics.Altitude/100, [0 355 660]);
xlabel('Cruising Level [FL]')
ylabel('Number of flight plans')
title("F355")
%% Draw histogram with F345 boundary
subplot(4,2,3);
histogram(statistics.Altitude/100, [0 345 660]);
xlabel('Cruising Level [FL]')
ylabel('Number of flight plans')
title("F345")
%% Draw histogram with F355 boundary
subplot(4,2,4);
histogram(statistics.Altitude/100, [0 335 660]);
xlabel('Cruising Level [FL]')
ylabel('Number of flight plans')
title("F335")
%% Draw histogram with F325 boundary
subplot(4,2,5);
histogram(statistics.Altitude/100, [0 325 660]);
xlabel('Cruising Level [FL]')
ylabel('Number of flight plans')
title("F325")
%% Draw histogram with F315 boundary
subplot(4,2,6);
histogram(statistics.Altitude/100, [0 315 660]);
xlabel('Cruising Level [FL]')
ylabel('Number of flight plans')
title("F315")
%% Draw histogram with F305 boundary
subplot(4,2,7);
histogram(statistics.Altitude/100, [0 305 660]);
xlabel('Cruising Level [FL]')
ylabel('Number of flight plans')
title("F305")
%% Draw histogram with F295 boundary
subplot(4,2,8);
histogram(statistics.Altitude/100, [0 295 660]);
xlabel('Cruising Level [FL]')
ylabel('Number of flight plans')
title("F295")