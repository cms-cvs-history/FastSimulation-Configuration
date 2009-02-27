# /dev/CMSSW_3_1_0/pre2/HLT/V123 (CMSSW_3_1_X_2009-02-25-0700_HLT2)

import FWCore.ParameterSet.Config as cms


HLTConfigVersion = cms.PSet(
  tableName = cms.string('/dev/CMSSW_3_1_0/pre2/HLT/V123')
)

block_hltL1NonIsoLargeWindowElectronPixelSeeds = cms.PSet(
  searchInTIDTEC = cms.bool( True ),
  HighPtThreshold = cms.double( 35.0 ),
  r2MinF = cms.double( -0.3 ),
  DeltaPhi1Low = cms.double( 0.23 ),
  DeltaPhi1High = cms.double( 0.08 ),
  ePhiMin1 = cms.double( -0.045 ),
  PhiMin2 = cms.double( -0.01 ),
  LowPtThreshold = cms.double( 5.0 ),
  z2MinB = cms.double( -0.2 ),
  dynamicPhiRoad = cms.bool( False ),
  ePhiMax1 = cms.double( 0.03 ),
  DeltaPhi2 = cms.double( 0.0040 ),
  SizeWindowENeg = cms.double( 0.675 ),
  rMaxI = cms.double( 0.2 ),
  rMinI = cms.double( -0.2 ),
  preFilteredSeeds = cms.bool( False ),
  r2MaxF = cms.double( 0.3 ),
  pPhiMin1 = cms.double( -0.03 ),
  initialSeeds = cms.InputTag( "globalMixedSeeds" ),
  pPhiMax1 = cms.double( 0.045 ),
  hbheModule = cms.string( "hbhereco" ),
  SCEtCut = cms.double( 5.0 ),
  z2MaxB = cms.double( 0.2 ),
  fromTrackerSeeds = cms.bool( False ),
  hcalRecHits = cms.InputTag( "hltHbhereco" ),
  maxHOverE = cms.double( 0.2 ),
  hbheInstance = cms.string( "" ),
  PhiMax2 = cms.double( 0.01 ),
  hOverEConeSize = cms.double( 0.1 )
)
block_hltL1IsoLargeWindowElectronPixelSeeds = cms.PSet(
  searchInTIDTEC = cms.bool( True ),
  HighPtThreshold = cms.double( 35.0 ),
  r2MinF = cms.double( -0.3 ),
  DeltaPhi1Low = cms.double( 0.23 ),
  DeltaPhi1High = cms.double( 0.08 ),
  ePhiMin1 = cms.double( -0.045 ),
  PhiMin2 = cms.double( -0.01 ),
  LowPtThreshold = cms.double( 5.0 ),
  z2MinB = cms.double( -0.2 ),
  dynamicPhiRoad = cms.bool( False ),
  ePhiMax1 = cms.double( 0.03 ),
  DeltaPhi2 = cms.double( 0.0040 ),
  SizeWindowENeg = cms.double( 0.675 ),
  rMaxI = cms.double( 0.2 ),
  rMinI = cms.double( -0.2 ),
  preFilteredSeeds = cms.bool( False ),
  r2MaxF = cms.double( 0.3 ),
  pPhiMin1 = cms.double( -0.03 ),
  initialSeeds = cms.InputTag( "globalMixedSeeds" ),
  pPhiMax1 = cms.double( 0.045 ),
  hbheModule = cms.string( "hbhereco" ),
  SCEtCut = cms.double( 5.0 ),
  z2MaxB = cms.double( 0.2 ),
  fromTrackerSeeds = cms.bool( False ),
  hcalRecHits = cms.InputTag( "hltHbhereco" ),
  maxHOverE = cms.double( 0.2 ),
  hbheInstance = cms.string( "" ),
  PhiMax2 = cms.double( 0.01 ),
  hOverEConeSize = cms.double( 0.1 )
)
block_hltL1NonIsoStartUpElectronPixelSeeds = cms.PSet(
  searchInTIDTEC = cms.bool( True ),
  HighPtThreshold = cms.double( 35.0 ),
  r2MinF = cms.double( -0.096 ),
  DeltaPhi1Low = cms.double( 0.23 ),
  DeltaPhi1High = cms.double( 0.08 ),
  ePhiMin1 = cms.double( -0.025 ),
  PhiMin2 = cms.double( -0.0050 ),
  LowPtThreshold = cms.double( 5.0 ),
  z2MinB = cms.double( -0.06 ),
  dynamicPhiRoad = cms.bool( False ),
  ePhiMax1 = cms.double( 0.015 ),
  DeltaPhi2 = cms.double( 0.0040 ),
  SizeWindowENeg = cms.double( 0.675 ),
  rMaxI = cms.double( 0.11 ),
  rMinI = cms.double( -0.11 ),
  preFilteredSeeds = cms.bool( False ),
  r2MaxF = cms.double( 0.096 ),
  pPhiMin1 = cms.double( -0.015 ),
  initialSeeds = cms.InputTag( "globalMixedSeeds" ),
  pPhiMax1 = cms.double( 0.025 ),
  hbheModule = cms.string( "hbhereco" ),
  SCEtCut = cms.double( 5.0 ),
  z2MaxB = cms.double( 0.06 ),
  fromTrackerSeeds = cms.bool( False ),
  hcalRecHits = cms.InputTag( "hltHbhereco" ),
  maxHOverE = cms.double( 0.2 ),
  hbheInstance = cms.string( "" ),
  PhiMax2 = cms.double( 0.0050 ),
  hOverEConeSize = cms.double( 0.1 )
)
block_hltL1NonIsoElectronPixelSeeds = cms.PSet(
  searchInTIDTEC = cms.bool( True ),
  HighPtThreshold = cms.double( 35.0 ),
  r2MinF = cms.double( -0.08 ),
  DeltaPhi1Low = cms.double( 0.23 ),
  DeltaPhi1High = cms.double( 0.08 ),
  ePhiMin1 = cms.double( -0.025 ),
  PhiMin2 = cms.double( -0.0010 ),
  LowPtThreshold = cms.double( 5.0 ),
  z2MinB = cms.double( -0.05 ),
  dynamicPhiRoad = cms.bool( False ),
  ePhiMax1 = cms.double( 0.015 ),
  DeltaPhi2 = cms.double( 0.0040 ),
  SizeWindowENeg = cms.double( 0.675 ),
  rMaxI = cms.double( 0.11 ),
  rMinI = cms.double( -0.11 ),
  preFilteredSeeds = cms.bool( False ),
  r2MaxF = cms.double( 0.08 ),
  pPhiMin1 = cms.double( -0.015 ),
  initialSeeds = cms.InputTag( "globalMixedSeeds" ),
  pPhiMax1 = cms.double( 0.025 ),
  hbheModule = cms.string( "hbhereco" ),
  SCEtCut = cms.double( 5.0 ),
  z2MaxB = cms.double( 0.05 ),
  fromTrackerSeeds = cms.bool( False ),
  hcalRecHits = cms.InputTag( "hltHbhereco" ),
  maxHOverE = cms.double( 0.2 ),
  hbheInstance = cms.string( "" ),
  PhiMax2 = cms.double( 0.0010 ),
  hOverEConeSize = cms.double( 0.1 )
)
block_hltL1IsoStartUpElectronPixelSeeds = cms.PSet(
  searchInTIDTEC = cms.bool( True ),
  HighPtThreshold = cms.double( 35.0 ),
  r2MinF = cms.double( -0.096 ),
  DeltaPhi1Low = cms.double( 0.23 ),
  DeltaPhi1High = cms.double( 0.08 ),
  ePhiMin1 = cms.double( -0.025 ),
  PhiMin2 = cms.double( -0.0050 ),
  LowPtThreshold = cms.double( 5.0 ),
  z2MinB = cms.double( -0.06 ),
  dynamicPhiRoad = cms.bool( False ),
  ePhiMax1 = cms.double( 0.015 ),
  DeltaPhi2 = cms.double( 0.0040 ),
  SizeWindowENeg = cms.double( 0.675 ),
  rMaxI = cms.double( 0.11 ),
  rMinI = cms.double( -0.11 ),
  preFilteredSeeds = cms.bool( False ),
  r2MaxF = cms.double( 0.096 ),
  pPhiMin1 = cms.double( -0.015 ),
  initialSeeds = cms.InputTag( "globalMixedSeeds" ),
  pPhiMax1 = cms.double( 0.025 ),
  hbheModule = cms.string( "hbhereco" ),
  SCEtCut = cms.double( 5.0 ),
  z2MaxB = cms.double( 0.06 ),
  fromTrackerSeeds = cms.bool( False ),
  hcalRecHits = cms.InputTag( "hltHbhereco" ),
  maxHOverE = cms.double( 0.2 ),
  hbheInstance = cms.string( "" ),
  PhiMax2 = cms.double( 0.0050 ),
  hOverEConeSize = cms.double( 0.1 )
)
block_hltL1IsoElectronPixelSeeds = cms.PSet(
  searchInTIDTEC = cms.bool( True ),
  HighPtThreshold = cms.double( 35.0 ),
  r2MinF = cms.double( -0.08 ),
  DeltaPhi1Low = cms.double( 0.23 ),
  DeltaPhi1High = cms.double( 0.08 ),
  ePhiMin1 = cms.double( -0.025 ),
  PhiMin2 = cms.double( -0.0010 ),
  LowPtThreshold = cms.double( 5.0 ),
  z2MinB = cms.double( -0.05 ),
  dynamicPhiRoad = cms.bool( False ),
  ePhiMax1 = cms.double( 0.015 ),
  DeltaPhi2 = cms.double( 0.0040 ),
  SizeWindowENeg = cms.double( 0.675 ),
  rMaxI = cms.double( 0.11 ),
  rMinI = cms.double( -0.11 ),
  preFilteredSeeds = cms.bool( False ),
  r2MaxF = cms.double( 0.08 ),
  pPhiMin1 = cms.double( -0.015 ),
  initialSeeds = cms.InputTag( "globalMixedSeeds" ),
  pPhiMax1 = cms.double( 0.025 ),
  hbheModule = cms.string( "hbhereco" ),
  SCEtCut = cms.double( 5.0 ),
  z2MaxB = cms.double( 0.05 ),
  fromTrackerSeeds = cms.bool( False ),
  hcalRecHits = cms.InputTag( "hltHbhereco" ),
  maxHOverE = cms.double( 0.2 ),
  hbheInstance = cms.string( "" ),
  PhiMax2 = cms.double( 0.0010 ),
  hOverEConeSize = cms.double( 0.1 )
)
block_hltL3TrajectorySeed = cms.PSet(
  EtaR_UpperLimit_Par1 = cms.double( 0.25 ),
  Eta_fixed = cms.double( 0.2 ),
  beamSpot = cms.InputTag( "offlineBeamSpot" ),
  OnDemand = cms.double( -1.0 ),
  Rescale_Dz = cms.double( 3.0 ),
  Eta_min = cms.double( 0.1 ),
  Rescale_phi = cms.double( 3.0 ),
  PhiR_UpperLimit_Par1 = cms.double( 0.6 ),
  DeltaZ_Region = cms.double( 15.9 ),
  Phi_min = cms.double( 0.1 ),
  PhiR_UpperLimit_Par2 = cms.double( 0.2 ),
  vertexCollection = cms.InputTag( "pixelVertices" ),
  Phi_fixed = cms.double( 0.2 ),
  DeltaR = cms.double( 0.2 ),
  EtaR_UpperLimit_Par2 = cms.double( 0.15 ),
  UseFixedRegion = cms.bool( False ),
  Rescale_eta = cms.double( 3.0 ),
  UseVertex = cms.bool( False ),
  EscapePt = cms.double( 1.5 )
)
