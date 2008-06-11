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

# Famos sequences (With fake conditions)
process.load("FastSimulation.Configuration.CommonInputsFake_cff")
process.load("FastSimulation.Configuration.FamosSequences_cff")

# L1 Emulator and HLT Setup
process.load("FastSimulation.HighLevelTrigger.HLTSetup_cff")

# L1 Menu and prescale factors : useful for testing all L1 paths
process.load("Configuration.StandardSequences.L1TriggerDefaultMenu_cff")

# HLT paths -- defined from ConfigDB
# This one is created on the fly by FastSimulation/Configuration/test/ExampleWithHLT.csh
process.load("FastSimulation.Configuration.HLT_cff")

# Simulation sequence
process.simulation = cms.Sequence(process.simulationWithFamos)
# You many not want to simulate everything
process.famosSimHits.SimulateCalorimetry = True
process.famosSimHits.SimulateTracking = True
# Parameterized magnetic field
process.VolumeBasedMagneticFieldESProducer.useParametrizedTrackerField = True
# Number of pileup events per crossing
process.famosPileUp.PileUpSimulator.averageNumber = 0.0

# No reconstruction - only HLT
process.HLTEndSequence = cms.Sequence(process.dummyModule)
 
# To write out events 
process.load("FastSimulation.Configuration.EventContent_cff")
process.o1 = cms.OutputModule("PoolOutputModule",
    process.AODSIMEventContent,
    fileName = cms.untracked.string('AODWithHLT.root')
)
process.outpath = cms.EndPath(process.o1)


# Keep the logging output to a nice level #
# service = Timing { }
# process.load("FWCore.MessageService.MessageLogger_cfi")
# process.MessageLogger.destinations = ['pyDetailedInfo.txt']


