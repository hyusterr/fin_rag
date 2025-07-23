read /tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/check/instances/MIP/stein27_inf.lp
read /tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/check/mipstarts/stein27_inf.lp.mst
presolve
validatesolve +infinity +infinity
read /tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/check/instances/MIP/stein27_inf.lp
read /tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/check/mipstarts/stein27_inf.lp.mst
set heuristics completesol beforepresol FALSE
optimize
validatesolve +infinity +infinity
quit
