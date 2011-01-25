#! /bin/bash

echo "Dumping GRun configuration"
hltGetConfiguration $(head -1 HLTVersionGRun) --fastsim > $CMSSW_BASE/src/FastSimulation/Configuration/python/HLT_GRun_cff.py
