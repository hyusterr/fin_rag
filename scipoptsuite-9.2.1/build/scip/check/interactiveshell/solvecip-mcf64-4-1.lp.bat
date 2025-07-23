read "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip"/check/"instances/Indicator/mcf64-4-1.lp"
write problem temp/mcf64-4-1.lp.cip
read temp/mcf64-4-1.lp.cip
optimize
validatesolve "10" "10"
quit
