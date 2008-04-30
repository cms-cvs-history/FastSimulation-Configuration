#!/bin/csh

# clean
rm $CMSSW_BASE/src/FastSimulation/Configuration/test/HLT.cff
rm $CMSSW_BASE/src/FastSimulation/Configuration/test/AODWithHLT.root
rm $CMSSW_BASE/src/FastSimulation/Configuration/test/ExampleWithHLT.log

# create HLT.cff :  For 2_0_4, use /dev/CMSSW_2_0_0/HLT/V35
$CMSSW_BASE/src/FastSimulation/Configuration/test/getFastSimHLTcff.py /dev/CMSSW_2_0_0/HLT/V35 $CMSSW_BASE/src/FastSimulation/Configuration/test/HLT.cff

# cmsRun 
cmsRun $CMSSW_BASE/src/FastSimulation/Configuration/test/ExampleWithHLT.cfg |& tee $CMSSW_BASE/src/FastSimulation/Configuration/test/ExampleWithHLT.log


