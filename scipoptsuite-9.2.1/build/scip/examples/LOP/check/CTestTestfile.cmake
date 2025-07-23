# CMake generated Testfile for 
# Source directory: /tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/examples/LOP/check
# Build directory: /tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/scip/examples/LOP/check
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(examples-lop-build "/usr/local/lib/python3.10/dist-packages/cmake/data/bin/cmake" "--build" "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build" "--config" "Release" "--target" "lop")
set_tests_properties(examples-lop-build PROPERTIES  RESOURCE_LOCK "libscip" _BACKTRACE_TRIPLES "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/examples/LOP/check/CMakeLists.txt;19;add_test;/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/examples/LOP/check/CMakeLists.txt;0;")
add_test(examples-lop-ex1 "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/bin/examples/lop" "-f" "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/examples/LOP/check/../data/ex1.lop" "-o" "3100" "3100")
set_tests_properties(examples-lop-ex1 PROPERTIES  DEPENDS "examples-lop-build" PASS_REGULAR_EXPRESSION "Validation         : Success" RESOURCE_LOCK "libscip" _BACKTRACE_TRIPLES "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/examples/LOP/check/CMakeLists.txt;41;add_test;/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/examples/LOP/check/CMakeLists.txt;0;")
add_test(examples-lop-t65i11xx "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/bin/examples/lop" "-f" "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/examples/LOP/check/../data/t65i11xx.lop" "-o" "16389651" "16389651")
set_tests_properties(examples-lop-t65i11xx PROPERTIES  DEPENDS "examples-lop-build" PASS_REGULAR_EXPRESSION "Validation         : Success" RESOURCE_LOCK "libscip" _BACKTRACE_TRIPLES "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/examples/LOP/check/CMakeLists.txt;41;add_test;/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/examples/LOP/check/CMakeLists.txt;0;")
add_test(examples-lop-t70x11xx "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/bin/examples/lop" "-f" "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/examples/LOP/check/../data/t70x11xx.lop" "-o" "343471236" "343471236")
set_tests_properties(examples-lop-t70x11xx PROPERTIES  DEPENDS "examples-lop-build" PASS_REGULAR_EXPRESSION "Validation         : Success" RESOURCE_LOCK "libscip" _BACKTRACE_TRIPLES "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/examples/LOP/check/CMakeLists.txt;41;add_test;/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/examples/LOP/check/CMakeLists.txt;0;")
