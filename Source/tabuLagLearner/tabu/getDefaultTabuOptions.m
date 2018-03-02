function opt = getDefaultTabuOptions()

opt.Tol = 10;
opt.Plot = true;
opt.Verbose = true;
opt.MaxIter=100;
opt.Target = -inf;
opt.MaxScore = inf;
opt.Min = 0;
opt.Max = inf;
opt.parallel = true;
opt.numThreads = [];
