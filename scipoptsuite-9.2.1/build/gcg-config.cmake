if(NOT TARGET libgcg)
  include("${CMAKE_CURRENT_LIST_DIR}/gcg-targets.cmake")
endif()

if(0)
   set(SCIP_DIR "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/scip")
   find_package(SCIP QUIET CONFIG)
endif()

set(GCG_LIBRARIES libgcg)
set(GCG_INCLUDE_DIRS "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src")
set(GCG_FOUND TRUE)
