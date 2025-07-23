# Install script for directory: /tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/lpi" TYPE FILE FILES
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/lpi/lpi.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/lpi/type_lpi.h"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/dijkstra" TYPE FILE FILES "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/dijkstra/dijkstra.h")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/objscip" TYPE FILE FILES
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/objscip/objbenders.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/objscip/objbenderscut.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/objscip/objbranchrule.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/objscip/objcloneable.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/objscip/objconshdlr.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/objscip/objcutsel.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/objscip/objdialog.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/objscip/objdisp.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/objscip/objeventhdlr.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/objscip/objheur.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/objscip/objmessagehdlr.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/objscip/objnodesel.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/objscip/objpresol.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/objscip/objpricer.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/objscip/objprobcloneable.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/objscip/objprobdata.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/objscip/objprop.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/objscip/objreader.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/objscip/objrelax.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/objscip/objscipdefplugins.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/objscip/objscip.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/objscip/objsepa.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/objscip/objtable.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/objscip/objvardata.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/objscip/type_objcloneable.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/objscip/type_objprobcloneable.h"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/scip" TYPE FILE FILES
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/bandit.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/bandit_epsgreedy.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/bandit_exp3.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/bandit_exp3ix.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/bandit_ucb.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/benders.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/benders_default.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/benderscut.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/benderscut_feas.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/benderscut_feasalt.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/benderscut_int.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/benderscut_nogood.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/benderscut_opt.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/bendersdefcuts.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/bitencode.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/boundstore.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/branch_allfullstrong.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/branch_cloud.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/branch_distribution.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/branch_fullstrong.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/branch_gomory.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/branch.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/branch_inference.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/branch_leastinf.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/branch_lookahead.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/branch_mostinf.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/branch_multaggr.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/branch_nodereopt.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/branch_pscost.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/branch_random.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/branch_relpscost.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/branch_vanillafullstrong.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/clock.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/compr.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/compr_largestrepr.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/compr_weakcompr.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/concsolver.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/concsolver_scip.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/concurrent.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/conflict.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/conflict_graphanalysis.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/conflict_dualproofanalysis.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/conflict_general.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/conflictstore.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/cons_abspower.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/cons_and.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/cons_benders.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/cons_benderslp.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/cons_bounddisjunction.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/cons_cardinality.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/cons_components.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/cons_conjunction.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/cons_countsols.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/cons_cumulative.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/cons_disjunction.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/cons_fixedvar.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/cons.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/cons_indicator.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/cons_integral.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/cons_knapsack.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/cons_linear.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/cons_linking.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/cons_logicor.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/cons_nonlinear.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/cons_orbisack.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/cons_orbitope.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/cons_or.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/cons_pseudoboolean.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/cons_quadratic.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/cons_setppc.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/cons_soc.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/cons_sos1.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/cons_sos2.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/cons_superindicator.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/cons_symresack.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/cons_varbound.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/cons_xor.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/cutpool.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/cuts.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/cutsel.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/cutsel_ensemble.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/cutsel_hybrid.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/cutsel_dynamic.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/dbldblarith.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/debug.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/dcmp.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/def.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/dialog_default.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/dialog.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/disp_default.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/disp.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/event_globalbnd.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/event.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/event_estim.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/event_shadowtree.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/event_softtimelimit.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/event_solvingphase.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/expr.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/expr_abs.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/expr_entropy.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/expr_erf.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/expr_exp.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/expr_log.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/expr_pow.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/expr_product.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/expr_sum.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/expr_trig.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/expr_value.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/expr_var.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/expr_varidx.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/exprinterpret.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_actconsdiving.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_adaptivediving.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_bound.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_clique.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_coefdiving.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_completesol.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_conflictdiving.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_crossover.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_dins.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_distributiondiving.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_dps.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_dualval.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_farkasdiving.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_feaspump.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_fixandinfer.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_fracdiving.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_gins.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_guideddiving.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_indicator.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_indicatordiving.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_intdiving.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_intshifting.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heuristics.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_linesearchdiving.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_localbranching.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_locks.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_alns.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_lpface.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_multistart.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_mutation.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_mpec.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_nlpdiving.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_objpscostdiving.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_octane.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_ofins.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_oneopt.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_padm.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_proximity.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_pscostdiving.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_randrounding.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_rens.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_reoptsols.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_repair.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_rins.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_rootsoldiving.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_rounding.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_scheduler.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_shiftandpropagate.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_shifting.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_simplerounding.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_subnlp.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_sync.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_trivial.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_trivialnegation.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_trustregion.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_trysol.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_twoopt.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_undercover.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_vbounds.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_veclendiving.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_zeroobj.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/heur_zirounding.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/history.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/implics.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/interrupt.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/intervalarith.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/lapack_calls.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/lp.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/mem.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/message_default.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/message.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/misc.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/nlhdlr_bilinear.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/nlhdlr_convex.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/nlhdlr_default.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/nlhdlr_perspective.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/nlhdlr_quadratic.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/nlhdlr_quotient.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/nlhdlr_signomial.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/nlhdlr_soc.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/nlhdlr.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/nlp.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/nlpi.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/nlpioracle.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/nlpi_all.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/nlpi_filtersqp.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/nlpi_ipopt.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/nlpi_worhp.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/nodesel_bfs.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/nodesel_breadthfirst.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/nodesel_dfs.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/nodesel_estimate.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/nodesel.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/nodesel_hybridestim.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/nodesel_restartdfs.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/nodesel_uct.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/paramset.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/presol_boundshift.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/presol_milp.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/presol_convertinttobin.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/presol_domcol.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/presol_dualagg.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/presol_dualcomp.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/presol_dualinfer.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/presol_gateextraction.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/presol.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/presol_implics.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/presol_inttobinary.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/presol_qpkktref.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/presol_redvub.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/presol_sparsify.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/presol_dualsparsify.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/presol_stuffing.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/presol_trivial.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/presol_tworowbnd.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/presolve.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/pricer.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/pricestore.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/primal.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/prob.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/prop_dualfix.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/prop_genvbounds.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/prop.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/prop_nlobbt.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/prop_obbt.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/prop_probing.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/prop_pseudoobj.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/prop_redcost.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/prop_rootredcost.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/prop_symmetry.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/prop_sync.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/prop_vbounds.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/pub_branch.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/pub_bandit.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/pub_bandit_epsgreedy.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/pub_bandit_exp3.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/pub_bandit_exp3ix.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/pub_bandit_ucb.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/pub_benders.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/pub_benderscut.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/pub_compr.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/pub_conflict.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/pub_cons.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/pub_cutpool.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/pub_cutsel.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/pub_dcmp.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/pub_dialog.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/pub_disp.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/pub_event.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/pub_expr.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/pub_fileio.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/pub_heur.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/pub_history.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/pub_implics.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/pub_lp.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/pub_matrix.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/pub_message.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/pub_misc.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/pub_misc_linear.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/pub_misc_rowprep.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/pub_misc_select.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/pub_misc_sort.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/pub_nlhdlr.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/pub_nlp.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/pub_nlpi.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/pub_nodesel.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/pub_paramset.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/pub_presol.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/pub_pricer.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/pub_prop.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/pub_reader.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/pub_relax.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/pub_reopt.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/pub_sepa.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/pub_sol.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/pub_table.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/pub_tree.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/pub_var.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/rbtree.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/reader_bnd.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/reader_ccg.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/reader_cip.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/reader_cnf.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/reader_cor.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/reader_dec.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/reader_diff.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/reader_fix.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/reader_fzn.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/reader_gms.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/reader.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/reader_lp.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/reader_mps.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/reader_mst.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/reader_nl.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/reader_opb.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/reader_osil.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/reader_pbm.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/reader_pip.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/reader_ppm.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/reader_rlp.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/reader_sol.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/reader_smps.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/reader_sto.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/reader_tim.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/reader_wbo.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/reader_zpl.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/relax.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/reopt.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/retcode.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/scipbuildflags.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/scipcoreplugins.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/scipdefplugins.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/scipgithash.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/scip.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/scip_bandit.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/scip_benders.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/scip_branch.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/scip_compr.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/scip_concurrent.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/scip_conflict.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/scip_cons.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/scip_copy.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/scip_cut.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/scip_cutsel.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/scip_datastructures.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/scip_debug.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/scip_dcmp.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/scip_dialog.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/scip_disp.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/scip_event.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/scip_expr.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/scip_general.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/scip_heur.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/scip_lp.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/scip_mem.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/scip_message.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/scip_nlp.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/scip_nlpi.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/scip_nodesel.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/scip_numerics.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/scip_param.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/scip_presol.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/scip_pricer.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/scip_prob.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/scip_probing.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/scip_prop.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/scip_randnumgen.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/scip_reader.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/scip_relax.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/scip_reopt.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/scip_sepa.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/scip_sol.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/scip_solve.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/scip_solvingstats.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/scip_table.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/scip_timing.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/scip_tree.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/scip_validation.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/scip_var.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/scipshell.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/sepa_cgmip.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/sepa_clique.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/sepa_closecuts.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/sepa_aggregation.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/sepa_convexproj.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/sepa_disjunctive.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/sepa_eccuts.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/sepa_gauge.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/sepa_gomory.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/sepa.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/sepa_impliedbounds.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/sepa_interminor.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/sepa_intobj.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/sepa_lagromory.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/sepa_mcf.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/sepa_minor.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/sepa_mixing.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/sepa_oddcycle.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/sepa_rapidlearning.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/sepa_rlt.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/sepastore.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/sepa_zerohalf.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/set.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/sol.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/solve.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/stat.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/struct_bandit.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/struct_benders.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/struct_benderscut.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/struct_branch.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/struct_clock.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/struct_compr.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/struct_concsolver.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/struct_concurrent.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/struct_conflict.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/struct_conflictstore.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/struct_cons.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/struct_cutpool.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/struct_cuts.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/struct_cutsel.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/struct_dcmp.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/struct_dialog.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/struct_disp.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/struct_event.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/struct_expr.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/struct_heur.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/struct_history.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/struct_implics.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/struct_lp.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/struct_matrix.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/struct_mem.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/struct_message.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/struct_misc.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/struct_nlhdlr.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/struct_nlp.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/struct_nlpi.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/struct_nodesel.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/struct_paramset.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/struct_presol.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/struct_pricer.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/struct_pricestore.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/struct_primal.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/struct_prob.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/struct_prop.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/struct_reader.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/struct_relax.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/struct_reopt.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/struct_scip.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/struct_sepa.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/struct_sepastore.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/struct_set.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/struct_sol.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/struct_stat.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/struct_syncstore.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/struct_table.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/struct_tree.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/struct_var.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/struct_visual.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/symmetry.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/symmetry_graph.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/symmetry_orbitopal.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/symmetry_orbital.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/symmetry_lexred.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/syncstore.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/table_default.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/table.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/tree.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/treemodel.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_bandit.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_benders.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_benderscut.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_branch.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_clock.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_compr.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_concsolver.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_concurrent.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_conflict.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_conflictstore.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_cons.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_cutpool.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_cuts.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_cutsel.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_dcmp.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_dialog.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_disp.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_event.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_expr.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_exprinterpret.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_heur.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_history.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_implics.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_interrupt.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_lp.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_matrix.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_mem.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_message.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_misc.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_nlhdlr.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_nlp.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_nlpi.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_nodesel.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_paramset.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_presol.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_pricer.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_pricestore.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_primal.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_prob.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_prop.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_reader.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_relax.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_reopt.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_result.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_retcode.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_scip.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_sepa.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_sepastore.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_set.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_sol.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_stat.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_syncstore.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_table.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_timing.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_tree.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_var.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/type_visual.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/var.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/scip/visual.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/scip/scip/config.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/scip/scip/scip_export.h"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/tclique" TYPE FILE FILES
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/tclique/tclique_coloring.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/tclique/tclique_def.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/tclique/tclique.h"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/tinycthread" TYPE FILE FILES "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/tinycthread/tinycthread.h")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/tpi" TYPE FILE FILES
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/tpi/def_openmp.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/tpi/tpi.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/tpi/type_tpi.h"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/xml" TYPE FILE FILES
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/xml/xmldef.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/xml/xml.h"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/symmetry" TYPE FILE FILES
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/symmetry/build_sassy_graph.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/symmetry/compute_symmetry.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/symmetry/struct_symmetry.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/symmetry/type_symmetry.h"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/blockmemshell" TYPE FILE FILES "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/src/blockmemshell/memory.h")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/scip" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/scip")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/scip"
         RPATH "/tmp2/yshuang/fin.rag/scip/lib")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/bin" TYPE EXECUTABLE FILES "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/bin/scip")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/scip" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/scip")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/scip"
         OLD_RPATH "::::::::::::::::::::::::::::::"
         NEW_RPATH "/tmp2/yshuang/fin.rag/scip/lib")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/scip")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libscip.so.9.2.1.0"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libscip.so.9.2"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHECK
           FILE "${file}"
           RPATH "")
    endif()
  endforeach()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/lib/libscip.so.9.2.1.0"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/lib/libscip.so.9.2"
    )
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libscip.so.9.2.1.0"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libscip.so.9.2"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      if(CMAKE_INSTALL_DO_STRIP)
        execute_process(COMMAND "/usr/bin/strip" "${file}")
      endif()
    endif()
  endforeach()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libscip.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libscip.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libscip.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/lib/libscip.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libscip.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libscip.so")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libscip.so")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/scip/scip-targets.cmake")
    file(DIFFERENT _cmake_export_file_changed FILES
         "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/scip/scip-targets.cmake"
         "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/scip/src/CMakeFiles/Export/440faded5223945d68a0ef6070a73d3d/scip-targets.cmake")
    if(_cmake_export_file_changed)
      file(GLOB _cmake_old_config_files "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/scip/scip-targets-*.cmake")
      if(_cmake_old_config_files)
        string(REPLACE ";" ", " _cmake_old_config_files_text "${_cmake_old_config_files}")
        message(STATUS "Old export file \"$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/scip/scip-targets.cmake\" will be replaced.  Removing files [${_cmake_old_config_files_text}].")
        unset(_cmake_old_config_files_text)
        file(REMOVE ${_cmake_old_config_files})
      endif()
      unset(_cmake_old_config_files)
    endif()
    unset(_cmake_export_file_changed)
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/scip" TYPE FILE FILES "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/scip/src/CMakeFiles/Export/440faded5223945d68a0ef6070a73d3d/scip-targets.cmake")
  if(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Rr][Ee][Ll][Ee][Aa][Ss][Ee])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/scip" TYPE FILE FILES "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/scip/src/CMakeFiles/Export/440faded5223945d68a0ef6070a73d3d/scip-targets-release.cmake")
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/scip" TYPE FILE FILES
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/scip/CMakeFiles/scip-config.cmake"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/scip/scip-config-version.cmake"
    )
endif()

