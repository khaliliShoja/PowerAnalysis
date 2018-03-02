function [finalItems, bestPerf, Perf, ItemsArr] = myTabu(fitFunc,AvailableItems,RemovableItems,PItems,Options)

if nargin<2 || isempty(AvailableItems)
    AvailableItems = 1:50;
end
if nargin<3
    RemovableItems = [];
end
if nargin<4
    PItems = [];
end
if nargin<5 
    Options = getDefaultTabuOptions();
end

Options = updateStruct(getDefaultTabuOptions(),Options);

bestPerf = fitFunc(PItems);
bestIter = 1;
ItemsArr = {PItems};
States = {sprintf('%d_', sort(PItems))};

if Options.Verbose
    fprintf('%d %d | Initial Perf: %g\n', 1, length(PItems), bestPerf);
end
if Options.Plot
    figure;ax=gca;xlabel('Iterations');ylabel('fitness')
    hold on
    if ~isempty(PItems)
        plot(0,bestPerf,'b.'); drawnow
    end
    xlim([0,Options.MaxIter])
end

for c=1:Options.MaxIter
    tic;
    [Items1, Perf1, delet] = destructiveIter(fitFunc,RemovableItems,PItems, States, Options);
    [Items2, Perf2, added] = constructiveIter(fitFunc,AvailableItems,PItems,bestPerf, States, Options);
    if Perf1 <= Perf2
        PItems = Items1;
        mp = Perf1;
    else
        PItems = Items2;
        mp = Perf2;
    end
    ItemsArr{c+1} = PItems;
    States{c+1} = sprintf('%d_', sort(PItems));
    Perf(c+1) = mp;
    if mp<=bestPerf
        bestPerf = mp;
        bestIter = c+1;
    end
    if Options.Verbose
        if Perf1 <= Perf2
            fprintf('%d %d | deleted Item: %d, Perf: %g | best(%d|%g) %g\n', c+1, length(PItems), delet, mp, bestIter, bestPerf, toc);
        else
            fprintf('%d %d | added Item: %d, Perf: %g | best(%d|%g) %g\n', c+1, length(PItems), added, mp, bestIter, bestPerf, toc);
        end
    end
    if Options.Plot
        plot(ax,c,mp,'b.'); drawnow
    end
    if c-bestIter >= Options.Tol || bestPerf<=Options.Target
        break
    end
end
finalItems = sort(ItemsArr{bestIter});
