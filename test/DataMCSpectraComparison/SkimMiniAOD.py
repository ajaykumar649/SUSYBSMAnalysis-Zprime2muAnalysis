import  FWCore.ParameterSet.Config as cms
## Declare process
process = cms.Process("MuonSkim")
 
## Declare input
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring('/store/mc/Phys14DR/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/MINIAODSIM/PU20bx25_tsg_PHYS14_25_V1-v1/00000/788396C0-9D6F-E411-97DF-002590494E34.root',
                                                              '/store/mc/Phys14DR/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/MINIAODSIM/PU20bx25_tsg_PHYS14_25_V1-v1/00000/3023C1A6-D56F-E411-B210-002590AC4C08.root',
                                                              '/store/mc/Phys14DR/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/MINIAODSIM/PU20bx25_tsg_PHYS14_25_V1-v1/00000/90575C8B-D56F-E411-A39B-0025904B1420.root',
                                                              '/store/mc/Phys14DR/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/MINIAODSIM/PU20bx25_tsg_PHYS14_25_V1-v1/00000/FCEF82CA-9D6F-E411-A2FC-002481E0D5CE.root',
                                                              '/store/mc/Phys14DR/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/MINIAODSIM/PU20bx25_tsg_PHYS14_25_V1-v1/10000/44B8EEE7-9A6F-E411-8858-002590DB0640.root',
                                                              '/store/mc/Phys14DR/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/MINIAODSIM/PU20bx25_tsg_PHYS14_25_V1-v1/10000/F03F87D0-9A6F-E411-8BC4-00266CFFA5E0.root'))

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32( -1 ) )

## Message logger configuration
process.MessageLogger = cms.Service("MessageLogger")
 
## Selection of good muons
from PhysicsTools.PatAlgos.selectionLayer1.muonSelector_cfi import *
process.goodMuons = selectedPatMuons.clone(
    src="slimmedMuons",
    cut='isGlobalMuon && pt>20. ',
    )
 
## Define output file
#process.TFileService = cms.Service("TFileService",
 #  fileName = cms.string('analyzePatZToMuMu.root')    )


process.OutModule=cms.OutputModule('PoolOutputModule',
                                   dataset = cms.untracked.PSet(datatier = cms.untracked.string('USER')),
                                   fileName=cms.untracked.string('miniAOD_skimmed.root'),
                                   outputCommands=cms.untracked.vstring('keep *')
                                   )

process.p = cms.Path(process.goodMuons) 
process.out=cms.EndPath(process.OutModule)                                                       
   


