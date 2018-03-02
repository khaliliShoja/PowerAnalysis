function [PItems, mp, added]=constructiveIter(fitFunc,AvailableItems,PItems,bestPerf,States,Options)

MaxScore = Options.MaxScore;

if ~Options.parallel
    nThr = 0;
elseif isempty(Options.numThreads)
    p = gcp;
    nThr = min(length(AvailableItems),p.NumWorkers);
else
    nThr = Options.numThreads;
end

AvailableItems = unique(AvailableItems); % AvailableItems is sorted
Groups = unique(PItems);
Counts = grpstats(PItems, PItems, 'numel');
ignore = Groups(Counts>=Options.Max);
AvailableItems(ismember(AvailableItems,ignore)) = [];

chPerf = zeros(size(AvailableItems))+inf;
parfor (i=1:length(AvailableItems),nThr)
% for i=1:length(AvailableItems)
    if length(unique(PItems))==1 && AvailableItems(i)==PItems(end)
        continue
    end
    Items = [PItems AvailableItems(i)];
    if any(strcmp(sprintf('%d_',sort(Items)), States)) % don't go to already passed states
        chPerf(i) = MaxScore;
    else
        chPerf(i) = fitFunc(Items);
    end
end
chPerf(chPerf==bestPerf)=inf; % don't include childs with same performance
[mp,mi]=min(chPerf);
PItems = [PItems AvailableItems(mi)];
added = AvailableItems(mi);
