# Install script for directory: /tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/tmp2/yshuang/fin.rag/scip")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set default install directory permissions.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/usr/bin/objdump")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/gcg" TYPE FILE FILES
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/branch_empty.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/branch_bpstrong.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/branch_generic.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/branch_orig.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/branch_relpsprob.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/branch_ryanfoster.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/class_conspartition.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/class_indexpartition.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/miscvisualization.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/class_pricingcontroller.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/class_pricingtype.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/class_partialdecomp.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/class_detprobdata.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/class_stabilization.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/class_varpartition.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/clscons.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/clsvar.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/colpool.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/cons_decomp.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/cons_decomp.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/cons_integralorig.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/cons_masterbranch.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/cons_origbranch.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/dec_compgreedily.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/dec_connected_noNewLinkingVars.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/dec_connectedbase.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/dec_consclass.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/dec_constype.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/dec_dbscan.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/dec_densemasterconss.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/dec_generalmastersetcover.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/dec_generalmastersetpack.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/dec_generalmastersetpart.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/dec_mastersetcover.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/dec_mastersetpack.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/dec_mastersetpart.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/dec_mst.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/dec_neighborhoodmaster.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/dec_postprocess.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/dec_staircase_lsp.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/dec_stairheur.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/dec_varclass.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/decomp.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/def.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/dialog_gcg.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/dialog_graph.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/dialog_master.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/disp_gcg.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/disp_master.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/event_bestsol.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/event_display.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/event_mastersol.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/event_relaxsol.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/event_solvingstats.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/gcg.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/gcgcol.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/gcg_general.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/gcggithash.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/gcgplugins.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/gcgpqueue.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/gcgsort.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/heur_gcgcoefdiving.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/heur_gcgdins.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/heur_gcgfeaspump.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/heur_gcgfracdiving.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/heur_gcgguideddiving.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/heur_gcglinesdiving.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/heur_gcgpscostdiving.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/heur_gcgrens.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/heur_gcgrins.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/heur_gcgrounding.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/heur_gcgshifting.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/heur_gcgsimplerounding.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/heur_gcgveclendiving.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/heur_gcgzirounding.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/heur_greedycolsel.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/heur_mastercoefdiving.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/heur_masterdiving.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/heur_masterfracdiving.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/heur_masterlinesdiving.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/heur_mastervecldiving.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/heur_origdiving.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/heur_relaxcolsel.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/heur_restmaster.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/heur_setcover.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/heur_xpcrossover.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/heur_xprins.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/masterplugins.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/nodesel_master.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/objdialog.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/objpricer_gcg.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/params_visu.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/presol_roundbound.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/pricer_gcg.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/pricestore_gcg.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/pricingjob.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/pricingprob.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/pub_clscons.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/pub_clsvar.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/pub_colpool.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/pub_decomp.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/pub_gcgcol.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/pub_gcgheur.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/pub_gcgsepa.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/pub_gcgpqueue.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/pub_gcgvar.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/pub_pricingjob.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/pub_pricingprob.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/pub_score.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/pub_solver.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/reader_blk.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/reader_cls.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/reader_dec.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/reader_gp.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/reader_ref.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/reader_tex.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/relax_gcg.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/scip_misc.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/score_bender.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/score_border.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/score_classic.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/score_fawh.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/score_forswh.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/score_maxwhite.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/score_spfawh.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/score_spfwh.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/score_strong.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/score.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/sepa_basis.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/sepa_master.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/solver.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/solver_cliquer.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/solver_knapsack.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/solver_mip.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/solver_xyz.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/stat.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/struct_branchgcg.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/struct_colpool.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/struct_decomp.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/struct_detector.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/struct_gcgcol.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/struct_gcgpqueue.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/struct_pricestore_gcg.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/struct_pricingjob.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/struct_pricingprob.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/struct_score.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/struct_solver.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/struct_vardata.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/type_branchgcg.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/type_classifier.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/type_colpool.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/type_consclassifier.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/type_decomp.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/type_detector.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/type_gcgcol.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/type_gcgpqueue.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/type_masterdiving.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/type_origdiving.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/type_parameter.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/type_pricestore_gcg.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/type_pricingjob.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/type_pricingprob.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/type_pricingstatus.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/type_score.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/type_solver.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/type_varclassifier.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/wrapper_partialdecomp.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/symmetry/automorphism.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/symmetry/automorphism.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/symmetry/pub_automorphism.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/gcg/dec_isomorph.h"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/graph" TYPE FILE FILES
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/graph/bipartitegraph.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/graph/bipartitegraph_def.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/graph/bridge.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/graph/columngraph.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/graph/columngraph_def.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/graph/graph.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/graph/graph_def.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/graph/graph_gcg.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/graph/graph_interface.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/graph/graph_tclique.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/graph/graphalgorithms.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/graph/graphalgorithms_def.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/graph/hypercolgraph.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/graph/hypercolgraph_def.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/graph/hypergraph.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/graph/hypergraph_def.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/graph/hyperrowcolgraph.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/graph/hyperrowcolgraph_def.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/graph/hyperrowgraph.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/graph/hyperrowgraph_def.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/graph/matrixgraph.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/graph/matrixgraph_def.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/graph/rowgraph.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/graph/rowgraph_def.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/gcg/src/graph/weights.h"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/gcg" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/gcg")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/gcg"
         RPATH "/tmp2/yshuang/fin.rag/scip/lib:/usr/local/lib")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/bin" TYPE EXECUTABLE FILES "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/bin/gcg")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/gcg" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/gcg")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/gcg"
         OLD_RPATH "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/lib:/usr/local/lib:"
         NEW_RPATH "/tmp2/yshuang/fin.rag/scip/lib:/usr/local/lib")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/gcg")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libgcg.so.3.7.1.0"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libgcg.so.3.7"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHECK
           FILE "${file}"
           RPATH "/usr/local/lib")
    endif()
  endforeach()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/lib/libgcg.so.3.7.1.0"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/lib/libgcg.so.3.7"
    )
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libgcg.so.3.7.1.0"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libgcg.so.3.7"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHANGE
           FILE "${file}"
           OLD_RPATH "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/lib:/usr/local/lib:"
           NEW_RPATH "/usr/local/lib")
      if(CMAKE_INSTALL_DO_STRIP)
        execute_process(COMMAND "/usr/bin/strip" "${file}")
      endif()
    endif()
  endforeach()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libgcg.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libgcg.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libgcg.so"
         RPATH "/usr/local/lib")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/lib/libgcg.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libgcg.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libgcg.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libgcg.so"
         OLD_RPATH "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/lib:/usr/local/lib:"
         NEW_RPATH "/usr/local/lib")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libgcg.so")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/gcg/gcg-targets.cmake")
    file(DIFFERENT _cmake_export_file_changed FILES
         "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/gcg/gcg-targets.cmake"
         "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/gcg/src/CMakeFiles/Export/55a8c2330c2af6b35ecce0f90032ca65/gcg-targets.cmake")
    if(_cmake_export_file_changed)
      file(GLOB _cmake_old_config_files "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/gcg/gcg-targets-*.cmake")
      if(_cmake_old_config_files)
        string(REPLACE ";" ", " _cmake_old_config_files_text "${_cmake_old_config_files}")
        message(STATUS "Old export file \"$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/gcg/gcg-targets.cmake\" will be replaced.  Removing files [${_cmake_old_config_files_text}].")
        unset(_cmake_old_config_files_text)
        file(REMOVE ${_cmake_old_config_files})
      endif()
      unset(_cmake_old_config_files)
    endif()
    unset(_cmake_export_file_changed)
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/gcg" TYPE FILE FILES "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/gcg/src/CMakeFiles/Export/55a8c2330c2af6b35ecce0f90032ca65/gcg-targets.cmake")
  if(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Rr][Ee][Ll][Ee][Aa][Ss][Ee])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/gcg" TYPE FILE FILES "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/gcg/src/CMakeFiles/Export/55a8c2330c2af6b35ecce0f90032ca65/gcg-targets-release.cmake")
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/gcg" TYPE FILE FILES "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/gcg/CMakeFiles/gcg-config.cmake")
endif()

