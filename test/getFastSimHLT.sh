#! /bin/sh
rm -f "$CMSSW_BASE/src/FastSimulation/Configuration/python/HLT_8E29_cff.py" "$CMSSW_BASE/src/FastSimulation/Configuration/python/blockHLT_8E29_cff.py"
rm -f "$CMSSW_BASE/src/FastSimulation/Configuration/python/HLT_1E31_cff.py" "$CMSSW_BASE/src/FastSimulation/Configuration/python/blockHLT_1E31_cff.py"

HLTVersion8E29=`head -1 $CMSSW_BASE/src/FastSimulation/Configuration/test/HLTVersion8E29`
HLTVersion1E31=`head -1 $CMSSW_BASE/src/FastSimulation/Configuration/test/HLTVersion1E31`

$CMSSW_BASE/src/FastSimulation/Configuration/test/getFastSimHLT_8E29_cff.py $HLTVersion8E29 "$CMSSW_BASE/src/FastSimulation/Configuration/python/HLT_8E29_cff.py" "$CMSSW_BASE/src/FastSimulation/Configuration/python/blockHLT_8E29_cff.py" "L1Menu_Commissioning2009_v0" "All" 
$CMSSW_BASE/src/FastSimulation/Configuration/test/getFastSimHLT_1E31_cff.py $HLTVersion1E31 "$CMSSW_BASE/src/FastSimulation/Configuration/python/HLT_1E31_cff.py" "$CMSSW_BASE/src/FastSimulation/Configuration/python/blockHLT_1E31_cff.py" "L1Menu_MC2009_v0" "All" 
