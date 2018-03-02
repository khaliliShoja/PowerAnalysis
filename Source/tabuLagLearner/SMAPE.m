function smape=SMAPE(act, prd)

act = (act(:));
prd = (prd(:));

n=length(act);
smape=100*nansum( abs(act-prd) ./ (abs(act+prd)/2) ) / n;