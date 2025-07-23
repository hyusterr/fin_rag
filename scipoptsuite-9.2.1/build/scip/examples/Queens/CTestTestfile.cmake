# CMake generated Testfile for 
# Source directory: /tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/examples/Queens
# Build directory: /tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/scip/examples/Queens
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(examples-queens-build "/usr/local/lib/python3.10/dist-packages/cmake/data/bin/cmake" "--build" "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build" "--config" "Release" "--target" "queens")
set_tests_properties(examples-queens-build PROPERTIES  RESOURCE_LOCK "libscip" _BACKTRACE_TRIPLES "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/examples/Queens/CMakeLists.txt;28;add_test;/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/examples/Queens/CMakeLists.txt;0;")
add_test(examples-queens-1 "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/bin/examples/queens" "1")
set_tests_properties(examples-queens-1 PROPERTIES  DEPENDS "examples-queens-build" _BACKTRACE_TRIPLES "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/examples/Queens/CMakeLists.txt;52;add_test;/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/examples/Queens/CMakeLists.txt;0;")
add_test(examples-queens-2 "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/bin/examples/queens" "2")
set_tests_properties(examples-queens-2 PROPERTIES  DEPENDS "examples-queens-build" _BACKTRACE_TRIPLES "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/examples/Queens/CMakeLists.txt;52;add_test;/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/examples/Queens/CMakeLists.txt;0;")
add_test(examples-queens-4 "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/bin/examples/queens" "4")
set_tests_properties(examples-queens-4 PROPERTIES  DEPENDS "examples-queens-build" _BACKTRACE_TRIPLES "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/examples/Queens/CMakeLists.txt;52;add_test;/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/examples/Queens/CMakeLists.txt;0;")
add_test(examples-queens-8 "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/bin/examples/queens" "8")
set_tests_properties(examples-queens-8 PROPERTIES  DEPENDS "examples-queens-build" _BACKTRACE_TRIPLES "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/examples/Queens/CMakeLists.txt;52;add_test;/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/examples/Queens/CMakeLists.txt;0;")
add_test(examples-queens-16 "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/bin/examples/queens" "16")
set_tests_properties(examples-queens-16 PROPERTIES  DEPENDS "examples-queens-build" _BACKTRACE_TRIPLES "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/examples/Queens/CMakeLists.txt;52;add_test;/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/examples/Queens/CMakeLists.txt;0;")
