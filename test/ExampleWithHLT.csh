#!/bin/csh

# clean
rm $CMSSW_BASE/src/FastSimulation/Configuration/test/HLT.cff
rm $CMSSW_BASE/src/FastSimulation/Configuration/test/ExampleWithHLT.log
rm AODWithHLT.root

# create HLT.cff :  For 2_0_4, use /dev/CMSSW_2_0_0/HLT/V35
# For the adventurous user, you may specify the L1 Menu and a select number of HLT paths
# Usage: ./getFastSimHLTcff.py <Version from ConfDB> <Name of cff file> <optional L1 Menu> <optional subset of paths>
# The default L1 Menu for 2_0_4 is L1Menu2008_2E30
# Any path subset must be given as a comma-separated list: a,b,c
# NOTE: If you choose to run a subset of the HLT, you MUST specify the L1 Menu used
# If you choose another L1 Menu, you must also change the corresponding include in 
# FastSimulation/Configuration/test/ExampleWithHLT.cfg
$CMSSW_BASE/src/FastSimulation/Configuration/test/getFastSimHLTcff.py /dev/CMSSW_2_1_0_pre5/HLT/V14 $CMSSW_BASE/src/FastSimulation/Configuration/test/HLT.cff "L1Menu2008_2E30" "All"

# cmsRun 
cmsRun $CMSSW_BASE/src/FastSimulation/Configuration/test/ExampleWithHLT.cfg |& tee $CMSSW_BASE/src/FastSimulation/Configuration/test/ExampleWithHLT.log


