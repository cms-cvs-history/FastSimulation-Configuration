import FWCore.ParameterSet.Config as cms

process = cms.Process("HLT")

# Number of events to be generated
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)

# Include the RandomNumberGeneratorService definition
process.load("FastSimulation.Configuration.RandomServiceInitialization_cff")

# Generate ttbar events
process.load("FastSimulation.Configuration.ttbar_cfi")

# L1 Menu and prescale factors : useful for testing all L1 paths
process.load("Configuration.StandardSequences.L1TriggerDefaultMenu_cff")
# Other choices are
# L1 Menu 2008 2x10E30 - Prescale
# process.load("L1TriggerConfig/L1GtConfigProducers/Luminosity/lumi1030/L1Menu2008_2E30_cff")
# L1 Menu 2008 2x10E30 - No Prescale
#process.load("L1TriggerConfig/L1GtConfigProducers/Luminosity/lumi1030/L1Menu2008_2E30_Unprescaled_cff")
# L1 Menu 2008 2x10E31 - Prescale
# process.load("L1TriggerConfig/L1GtConfigProducers/Luminosity/lumi1031/L1Menu2008_2E31_cff")
# L1 Menu 2008 2x10E31 - No Prescale
# process.load("L1TriggerConfig/L1GtConfigProducers/Luminosity/lumi1031/L1Menu2008_2E31_Unprescaled_cff")
# L1 Menu 2008 10E32 - Prescale 
# process.load("L1TriggerConfig/L1GtConfigProducers/Luminosity/lumi1x1032/L1Menu2007_cff")
# L1 Menu 2008 10E32 - No Prescale 
# process.load("L1TriggerConfig/L1GtConfigProducers/Luminosity/lumi1x1032/L1Menu2007_Unprescaled_cff")


# Common inputs, with fake conditions
process.load("FastSimulation.Configuration.CommonInputsFake_cff")

# L1 Emulator and HLT Setup
process.load("FastSimulation.HighLevelTrigger.HLTSetup_cff")

# Famos sequences
process.load("FastSimulation.Configuration.FamosSequences_cff")

# Parametrized magnetic field (new mapping, 4.0 and 3.8T)
#process.load("Configuration.StandardSequences.MagneticField_40T_cff")
process.load("Configuration.StandardSequences.MagneticField_38T_cff")
process.VolumeBasedMagneticFieldESProducer.useParametrizedTrackerField = True

# HLT paths -- defined from ConfigDB
# This one is created on the fly by FastSimulation/Configuration/test/ExampleWithHLT_py.csh
process.load("FastSimulation.Configuration.HLT_cff")

# Simulation sequence
process.simulation = cms.Sequence(process.simulationWithFamos)
# You many not want to simulate everything
process.famosSimHits.SimulateCalorimetry = True
process.famosSimHits.SimulateTracking = True
# Number of pileup events per crossing
process.famosPileUp.PileUpSimulator.averageNumber = 0.0

# No reconstruction - only HLT
process.HLTEndSequence = cms.Sequence(process.dummyModule)

# HLT schedule
process.schedule = cms.Schedule()
process.schedule.extend(process.HLTSchedule)

# To write out events 
process.load("FastSimulation.Configuration.EventContent_cff")
process.o1 = cms.OutputModule("PoolOutputModule",
    process.AODSIMEventContent,
    fileName = cms.untracked.string('AODWithHLT.root')
)
process.outpath = cms.EndPath(process.o1)

# Add endpaths to the schedule
process.schedule.append(process.outpath)

# Keep the logging output to a nice level #
# process.Timing =  cms.Service("Timing")
# process.load("FWCore/MessageService/MessageLogger_cfi")
# process.MessageLogger.destinations = cms.untracked.vstring("pyDetailedInfo.txt")

# Make the job crash in case of missing product
process.options = cms.untracked.PSet( Rethrow = cms.untracked.vstring('ProductNotFound') )
