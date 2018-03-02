close all
clear
addpath('Tabu')

T = readtable('..\..\Data\Power\fixed\df_all.csv');

Target = T.ActualAIL;

opt = getDefaultTabuOptions();
opt.Tol = 20;
opt.Verbose=1;
opt.Plot = 1;

AllLags = [1:23 24:24:(400*24)];
vlSize = length(find(T.Date.Year == 2016));
tsSize = length(find(T.Date.Year >= 2017));
ts2018 = 1344;

vlTarget = Target(end-tsSize-vlSize-max(AllLags)-1:end-tsSize);
tsTarget = Target(end-tsSize-vlSize-max(AllLags)-1:end);

% L=myTabu(@(x)(fitness(x,vlTarget, vlSize)),AllLags,[],[1],opt)

L = [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 22 22 23 23 23 23 23 144 168 8736];

fitness(L, vlTarget, vlSize, 1, datenum(T.Date(end-tsSize-vlSize+1:end-tsSize)), T.Day_AheadForecastedAIL(end-tsSize-vlSize+1:end-tsSize), @RMSE), datetick('x')
fitness(L, tsTarget, tsSize, 1, datenum(T.Date(end-tsSize+1:end)), T.Day_AheadForecastedAIL(end-tsSize+1:end), @RMSE), datetick('x')
fitness(L, Target, ts2018, 1, datenum(T.Date(end-ts2018+1:end)), T.Day_AheadForecastedAIL(end-ts2018+1:end), @RMSE), datetick('x')
