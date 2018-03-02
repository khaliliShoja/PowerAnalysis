function fit = fitness(Lags, Data, prdSize, Plot, Xaxis, OtherMethod, err)

if nargin<4
    Plot = false;
end
if nargin <5
    Xaxis = 1:prdSize;
end
if nargin <6
    OtherMethod = [];
end
if nargin <7
    err = @SMAPE; % RMSE or SMAPE
end

if isempty(Lags)
    fit = inf;
    return
end
Target = Data(end-prdSize+1:end);
Output = predictor_1s(Data, Lags, prdSize);
fit = err(Target, Output);

if Plot
    figure;
    plot(Xaxis, Target);
    hold all
    plot(Xaxis, Output)
    if ~isempty(OtherMethod)
        plot(Xaxis, OtherMethod)
        title(['fitness(' char(err) '): ' num2str(fit) ' vs ' num2str(err(Target, OtherMethod))])
        legend('Actual', 'Our Method', 'Old Method')
    else
        title(['fitness(' char(err) '): ' num2str(fit)])
        legend('Actual', 'Our Method')
    end
end

