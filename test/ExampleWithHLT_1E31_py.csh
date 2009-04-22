#!/bin/csh

# clean
rm -f $CMSSW_BASE/src/FastSimulation/Configuration/python/HLT_1E31_cff.py
rm -f $CMSSW_BASE/src/FastSimulation/Configuration/test/ExampleWithHLT_1E31.log
rm -f $CMSSW_BASE/src/FastSimulation/Configuration/python/blockHLT_1E31_cff.py
rm -f AODWithHLT.root

# create HLT.cff :  For 2_0_4, use /dev/CMSSW_2_0_0/HLT/V35
# For the adventurous user, you may specify the L1 Menu and a select number of HLT paths
# Usage: ./getFastSimHLTcff.py <Version from ConfDB> <Name of cff file> <optional L1 Menu> <optional subset of paths>
# The default L1 Menu for 2_0_4 is L1Menu2008_2E30
# Any path subset must be given as a comma-separated list: a,b,c
# NOTE: If you choose to run a subset of the HLT, you MUST specify the L1 Menu used
# If you choose another L1 Menu, you must also change the corresponding include in 
# FastSimulation/Configuration/test/ExampleWithHLT.cfg
set HLTVersion=`head -1 $CMSSW_BASE/src/FastSimulation/Configuration/test/HLTVersion1E31`

$CMSSW_BASE/src/FastSimulation/Configuration/test/getFastSimHLT_1E31_cff.py $HLTVersion "$CMSSW_BASE/src/FastSimulation/Configuration/python/HLT_1E31_cff.py" "$CMSSW_BASE/src/FastSimulation/Configuration/python/blockHLT_1E31_cff.py" "L1Menu_MC2009_v0" "All" 
#"HLTriggerFirstPath"
#"All"

# Set the environment 
cmsenv

# Compile the HLT_cff.py file
cd $CMSSW_BASE/src/FastSimulation/
scramv1 b python
cd -

# Run the example
cmsRun $CMSSW_BASE/src/FastSimulation/Configuration/test/ExampleWithHLT_1E31_cfg.py |& tee $CMSSW_BASE/src/FastSimulation/Configuration/test/ExampleWithHLT_1E31_py.log
