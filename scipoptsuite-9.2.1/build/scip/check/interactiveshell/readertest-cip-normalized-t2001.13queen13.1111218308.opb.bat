set heur emph off
read "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip"/check/"instances/PseudoBoolean/normalized-t2001.13queen13.1111218308.opb"
write problem temp/normalized-t2001.13queen13.1111218308.opb.cip
presolve
write transproblem temp/normalized-t2001.13queen13.1111218308.opb_trans.cip
set heur emph def
read temp/normalized-t2001.13queen13.1111218308.opb_trans.cip
optimize
validatesolve "+infinity" "+infinity"
read temp/normalized-t2001.13queen13.1111218308.opb.cip
optimize
validatesolve "+infinity" "+infinity"
quit
