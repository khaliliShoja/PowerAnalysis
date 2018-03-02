function Y = predictor(Data,Lags,prdSize)

n = length(Data);
Data = [Data; zeros(prdSize,1)];
for i=1:prdSize
    Data(n+i) = median(Data(n+i-Lags));
%     Data(n+i) = expm1(mean(log1p(Data(n+i-Lags))));
% Data(n+i) = expm1(median(log1p(Data(n+i-Lags))));
end

Y = Data(n+1:end);