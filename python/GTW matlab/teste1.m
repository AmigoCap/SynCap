clear all;
cercle=csvread('cercle.csv');
MoCap=cercle(200:5700,4:6)/1000;
Acc=cercle(500:3350,1:3);

%% algorithm parameter

parCca = st('d', 3, 'lams', 0);
parPdtw = [];
%arPimw = st('lA', 1, 'lB', 1);
parGN = st('nItMa', 2, 'inp', 'linear');
parGtw = st('nItMa', 20, 'debg', 'n');


X0s = {MoCap';Acc'}
Xs = pcas(X0s, st('d', 3, 'cat', 'n'));

ns = cellDim(Xs, 2);
l = round(max(ns) * 1.1);
bas = baTems(l, ns, 'pol', [5 .5], 'tan', [5 1 1]);

%% utw (initialization)
aliUtw = utw(Xs, bas, []);

%% gtw
aliGtw = gtw(X0s, bas, aliUtw, [], parGtw, parCca, parGN);
%% show sequence
shAliCmpOne(X0s, Xs, {aliGtw}, [], parCca, parGN);
