function [PItems, mp, delet] = destructiveIter(fitFunc,RemovableItems,PItems, States, Options)

MaxScore = Options.MaxScore;
if ~Options.parallel
    nThr = 0;
elseif isempty(Options.numThreads)
    p = gcp;
    nThr = min(length(RemovableItems),p.NumWorkers);
else
    nThr = Options.numThreads;
end

if isempty(RemovableItems)
    RemovableItems = unique(PItems);
end
RemovableItems = intersect(RemovableItems,unique(PItems));
Groups = unique(PItems);
Counts = grpstats(PItems, PItems, 'numel');
ignore = Groups(Counts<=Options.Min);
RemovableItems(ismember(RemovableItems,ignore)) = [];

chPerf = zeros(1,length(RemovableItems));
parfor (i=1:length(RemovableItems), nThr)
    Items = PItems;
    Items(find(Items==RemovableItems(i),1))=[];
    if any(strcmp(sprintf('%d_',sort(Items)), States)) % don't go to already passed states
        chPerf(i) = MaxScore;
    else
        chPerf(i) = fitFunc(Items);
    end
end
[mp,mi]=min(chPerf);
PItems(find(PItems==RemovableItems(mi),1))=[];
delet = RemovableItems(mi);
