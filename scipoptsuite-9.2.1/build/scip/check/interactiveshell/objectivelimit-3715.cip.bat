set load "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip"/check/coverage/settings/"default".set
read "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip"/check/"instances/Issue/3715.cip"
set limits objective "0.01"
optimize
validatesolve "0" "0"
quit
