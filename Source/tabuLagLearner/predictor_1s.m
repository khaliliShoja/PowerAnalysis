function Y = predictor_1s(Data,Lags,prdSize)

n = length(Data)-prdSize;
Data = [Data; zeros(prdSize,1)];
Y = zeros(prdSize,1);
for i=1:prdSize
%     Y(i) = median(Data(n+i-Lags));
    Y(i) = mean(Data(n+i-Lags));
end

