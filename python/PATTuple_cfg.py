#!/usr/bin/env python

import FWCore.ParameterSet.Config as cms

# Standard CMSSW configuration (mostly standard in PAT tuple/tools
# use).


process = cms.Process('PAT')
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(100))
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))
#process.source = cms.Source('PoolSource', fileNames = cms.untracked.vstring('file:PlaceHolder.root'))
#process.source = cms.Source('PoolSource', fileNames =cms.untracked.vstring('/store/mc/Phys14DR/DYJetsToEEMuMu_M-9500_13TeV-madgraph/AODSIM/PU20bx25_PHYS14_25_V1-v2/00000/18C7C360-E076-E411-9E2F-E0CB4E19F9BC.root'))
#process.source = cms.Source('PoolSource', fileNames = cms.untracked.vstring('root://xrootd.unl.edu//store/relval/CMSSW_7_4_0/RelValProdTTbar_13/AODSIM/MCRUN2_74_V7D_pxBest_gs7115-v1/00000/9081056A-10E7-E411-A322-00259059391E.root'))
process.source = cms.Source('PoolSource', fileNames = cms.untracked.vstring('file:9081056A-10E7-E411-A322-00259059391E.root'))

    # Load services needed to run the PAT.
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
#process.GlobalTag.globaltag = cms.string('PHY1474_25V2')
process.GlobalTag.globaltag = cms.string('MCRUN2_74_V6B')

process.load('FWCore.MessageLogger.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 5000
process.MessageLogger.cerr.threshold = 'INFO'
process.MessageLogger.categories.append('PATSummaryTables')
process.MessageLogger.cerr.PATSummaryTables = cms.untracked.PSet(limit = cms.untracked.int32(10)) ### instead of -1 federica

## switch to uncheduled mode
process.options.allowUnscheduled = cms.untracked.bool(True)

process.load('PhysicsTools.PatAlgos.patSequences_cff')

    # Define the output file with the output commands defining the
    # branches we want to have in our PAT tuple.
process.out = cms.OutputModule('PoolOutputModule',
                               fileName = cms.untracked.string('testMETFilter.root'),
                               # fileName = cms.untracked.string('file:PlaceHolder.root'),
                               SelectEvents = cms.untracked.PSet( SelectEvents = cms.vstring('p') ),
                               #SelectEvents   = cms.untracked.PSet(SelectEvents = cms.vstring('HLT_Mu*')),
                               outputCommands = cms.untracked.vstring('drop *',
                                                                      'keep patElectrons_cleanPatElectrons__*',
                                                                      'keep patMuons_cleanPatMuons__*',
                                                                      'keep patJets_cleanPatJets__*',
                                                                      'keep patPhotons_cleanPatPhotons__*',
                                                                      'keep patMETs_patMETs*__PAT',
                                                                      'keep recoGenParticles_prunedMCLeptons_*_*',
                                                                      'keep recoGenJets_selectedPatJets_genJets_*',
                                                                      'keep recoBaseTagInfosOwned_selectedPatJets_tagInfos_*',
                                                                      'keep GenEventInfoProduct_*_*_*',
                                                                      'keep GenRunInfoProduct_*_*_*',
                                                                      'keep *_offlineBeamSpot_*_*',
                                                                      'keep *_offlinePrimaryVertices_*_*',
                                                                      'keep edmTriggerResults_TriggerResults__HLT*',
                                                                      'keep edmTriggerResults_TriggerResults__REDIGI*',
                                                                      'keep L1GlobalTriggerObjectMaps_l1L1GtObjectMap_*_*', # drop later if embedding of L1 into PAT works fine
                                                                      'keep L1GlobalTriggerReadoutRecord_gtDigis__RECO',
                                                                      'keep *_hltTriggerSummaryAOD__HLT*',
                                                                      'keep *_hltTriggerSummaryAOD__REDIGI*',
                                                                      'keep edmTriggerResults_TriggerResults__PAT', # for post-tuple filtering on the goodData paths
                                                                      'keep PileupSummaryInfos_addPileupInfo_*_*',   # may be needed for pile-up reweighting   
 
                                                                      'keep patTriggerObjects_patTrigger_*_PAT', 
                                                                      'keep patTriggerFilters_patTrigger_*_PAT', 
                                                                      'keep patTriggerPaths_patTrigger_*_PAT', 
                                                                      'keep patTriggerEvent_patTriggerEvent_*_PAT', 
                                                                      'drop *_cleanPatMuons_*_*', 
                                                                      'keep *_cleanPatMuonsTriggerMatch_*_PAT', 
                                                                      'keep *_cleanPatMuonsTriggerMatch_*_*', 
                                                                      'keep *_patTrigger_*_*', 
                                                                      'keep *_patTriggerEvent_*_*', 
                                                                      'keep *_patMETsPF_*_*',
                                                                      )
                               )
############ electrons
from PATTools import addHEEPId
addHEEPId(process)
#process.heepPatElectrons = cms.EDFilter('PATElectronSelector',
 #                                       src = cms.InputTag('patElectrons'),
 #                                      cut = cms.string('userInt("HEEPId") == 0')
   #                                     )

#process.patDefaultSequence.replace(process.selectedPatElectrons, process.selectedPatElectrons * process.heepPatElectrons)
#process.countPatLeptons.electronSource = cms.InputTag('heepPatElectrons')
#process.countPatLeptons.minNumber = 2

del process.patTaus.tauIDSources.againstElectronMVA5raw
del process.patTaus.tauIDSources.againstMuonMedium
process.cleanPatTaus.preselection = process.cleanPatTaus.preselection.value().replace('againstMuonMedium', 'againstMuonTight') #now Tight is the default choice

process.patMuons.embedTrack = True

############ muon preselection
from PhysicsTools.PatAlgos.selectionLayer1.muonSelector_cfi import *
process.selectedPatMuons = selectedPatMuons.clone(#cut = "isTrackerMuon || isGlobalMuon",
                                                    cut = "isTrackerMuon & isGlobalMuon & pt > 20. & abs(eta) < 2.4",
                                                    #   src = cms.InputTag("selectedPatMuons"),# default
                                                    filter = cms.bool(True))

from PhysicsTools.PatAlgos.selectionLayer1.muonCountFilter_cfi import *
process.countPatMuons.minNumber = cms.uint32(1)

#process.countPatMuons = cms.EDFilter("CandViewCountFilter",
 #                                    src = cms.InputTag("selectedPatMuons"),
  #                                   minNumber = cms.uint32(1),
   #                                  filter = cms.bool(True)
    #                                 )


#process.countPatMuons.minNumber = cms.uint32(1)
#process.countPatMuons.src = cms.InputTag("selectedPatMuons")
#process.countPatMuons.minNumber = cms.uint32(2)

from PhysicsTools.PatAlgos.tools.metTools import addMETCollection 
addMETCollection(process, labelName='patMETsPF', metSource='pfMetT1')

from PhysicsTools.PatAlgos.tools.jetTools import switchJetCollection #to be checked
switchJetCollection(process, 
                    jetSource = cms.InputTag('ak4PFJets'),
                    jetCorrections = ('AK4PF', cms.vstring(['L1FastJet', 'L2Relative','L3Absolute']), 'Type-1'),
                    btagDiscriminators = ['jetBProbabilityBJetTags',
                                          'jetProbabilityBJetTags',
                                          'trackCountingHighPurBJetTags',
                                          'trackCountingHighEffBJetTags',
                                          'simpleSecondaryVertexHighEffBJetTags',
                                          'simpleSecondaryVertexHighPurBJetTags',
                                          'combinedSecondaryVertexBJetTags'],
                                              )

# Make a collection of muons with our final selection applied so that
# the muon-jet cleaning will use only muons passing those cuts. This
# muon collection is not saved in the output.
from SUSYBSMAnalysis.Zprime2muAnalysis.OurSelectionDec2012_cff import loose_cut
process.muonsForJetCleaning = process.selectedPatMuons.clone(cut = loose_cut.replace('pt > 45', 'pt > 30'))
process.patDefaultSequence.replace(process.selectedPatMuons, process.selectedPatMuons * process.muonsForJetCleaning)
process.cleanPatJets.checkOverlaps.muons.src = 'muonsForJetCleaning'
process.cleanPatJets.checkOverlaps.muons.deltaR = 0.2
process.cleanPatJets.checkOverlaps.muons.requireNoOverlaps = True
process.cleanPatJets.finalCut = 'pt > 30.0'


############## embedding of trigger info
process.load('SUSYBSMAnalysis.Zprime2muAnalysis.hltTriggerMatch_cfi')

from PhysicsTools.PatAlgos.tools.trigTools import *
switchOnTrigger( process )
switchOnTriggerMatchEmbedding( process,
                               triggerProducer = 'patTrigger',
                               triggerMatchers = [ 'muonTriggerMatchHLTMuons' ]
                               )


process.load('SUSYBSMAnalysis.Zprime2muAnalysis.goodData_cff')
process.goodDataHLTPhysicsDeclared = cms.Path(process.hltPhysicsDeclared)
process.goodDataPrimaryVertexFilter = cms.Path(process.primaryVertexFilter)
process.goodDataNoScraping = cms.Path(process.noscraping)
process.goodDataAll = cms.Sequence(process.hltPhysicsDeclared * process.primaryVertexFilter) # * process.noscraping)

#MET filter
#process.load("RecoMET.METFilters.metFilters_cff")
#has to be replaced in 7X because the import * inside refers to a c++ class that is not anymore defined 
process.load("PhysicsTools.PatAlgos.slimming.metFilterPaths_cff")
process.goodDataMETFilter =  cms.Path(process.metFilters)

# Let it run
#process.p = cms.Path(process.goodOfflinePrimaryVertices*process.GoodMuons *  process.GoodEvents * process.patTriggerMatching * process.goodDataAll)

#process.p = cms.Path(process.selectedPatMuons * process.patTriggerMatching *  process.countPatMuons)
process.p = cms.Path(goodDataMETFilter * process.selectedPatMuons *  process.countPatMuons)
process.outpath = cms.EndPath(process.out) 

#print process.dumpPython()
