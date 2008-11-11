import FWCore.ParameterSet.Config as cms

source = cms.Source("FlatRandomPtGunSource",
    PGunParameters = cms.untracked.PSet(
        MaxPt = cms.untracked.double(35.0),
        MinPt = cms.untracked.double(35.0),
        # you can request more than 1 particle
        #untracked vint32  PartID = { 211, 11, -13 }
        PartID = cms.untracked.vint32(11),
        MaxEta = cms.untracked.double(0.5),
        MaxPhi = cms.untracked.double(-1.99),
        MinEta = cms.untracked.double(0.5),
        MinPhi = cms.untracked.double(-2.01) ## it must be in radians

    ),
    Verbosity = cms.untracked.int32(0), ## for printouts, set it to 1 (or greater)   

    AddAntiParticle = cms.untracked.bool(False), ## back-to-back particles

    firstRun = cms.untracked.uint32(1)
)


