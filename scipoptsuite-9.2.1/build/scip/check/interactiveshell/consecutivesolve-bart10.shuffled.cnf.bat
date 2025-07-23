set display verblevel 0
set timing enabled FALSE
read "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip"/check/"instances/SAT/bart10.shuffled.cnf"
optimize
write statistics temp/bart10.shuffled.cnf_r1.stats
read "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip"/check/"instances/SAT/bart10.shuffled.cnf"
optimize
write statistics temp/bart10.shuffled.cnf_r2.stats
quit
