#!/usr/bin/env python

import sys, os, FWCore.ParameterSet.Config as cms
from SUSYBSMAnalysis.Zprime2muAnalysis.Zprime2muAnalysis_cff import switch_hlt_process_name
from SUSYBSMAnalysis.Zprime2muAnalysis.Zprime2muAnalysis_cfg import process, flag
#process.source.fileNames=['root://cms-xrd-global.cern.ch//store/mc/Phys14DR/DYJetsToEEMuMu_M-120To200_13TeV-madgraph/MINIAODSIM/PU20bx25_PHYS14_25_V1-v2/10000/0626BCFB-C27C-E411-BFCF-002590747DDC.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/DYJetsToEEMuMu_M-120To200_13TeV-madgraph/MINIAODSIM/PU20bx25_PHYS14_25_V1-v2/10000/C645CDFB-C27C-E411-A3B0-002590747DDC.root']
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/DYJetsToEEMuMu_M-1400To2300_13TeV-madgraph/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/12B916AF-CE73-E411-8419-002590747DE2.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/DYJetsToEEMuMu_M-200To400_13TeV-madgraph/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/10000/88C136C9-C073-E411-B945-E0CB4E5536BE.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/DYJetsToEEMuMu_M-2300To3500_13TeV-madgraph/MINIAODSIM/PU20bx25_PHYS14_25_V1-v2/00000/0AAFEA47-FD76-E411-AC79-20CF30561726.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/DYJetsToEEMuMu_M-3500To4500_13TeV-madgraph/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/AA40FD5D-CE73-E411-8344-20CF3019DF11.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/DYJetsToEEMuMu_M-400To800_13TeV-madgraph/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/6C63A3C9-2972-E411-9997-00266CFFBCD0.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/DYJetsToEEMuMu_M-4500To6000_13TeV-madgraph/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/B62B0696-2670-E411-A7DA-003048FFCB6A.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/DYJetsToEEMuMu_M-4500To6000_13TeV-madgraph/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/D20E3F90-2670-E411-B1EC-0025905A60AA.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/DYJetsToEEMuMu_M-6000To7500_13TeV-madgraph/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/10000/08B2ECF8-C275-E411-919A-001E673972E7.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/DYJetsToEEMuMu_M-7500To8500_13TeV-madgraph/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/48E742E6-CF73-E411-B2D7-002590D0B072.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/DYJetsToEEMuMu_M-7500To8500_13TeV-madgraph/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/10000/0E143E69-BE73-E411-99FC-E0CB4EA0A8E0.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/DYJetsToEEMuMu_M-800To1400_13TeV-madgraph/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/10000/3AEB9038-A66B-E411-9DD0-00A0D1EEF328.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/DYJetsToEEMuMu_M-8500To9500_13TeV-madgraph/MINIAODSIM/PU20bx25_PHYS14_25_V1-v2/00000/B0441204-FF78-E411-A4CB-002618FDA216.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/DYJetsToEEMuMu_M-9500_13TeV-madgraph/MINIAODSIM/PU20bx25_PHYS14_25_V1-v2/00000/66767358-FA76-E411-956B-00259073E42E.root']

#process.source.fileNames=['root://cms-xrd-global.cern.ch//store/mc/Phys14DR/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_tsg_PHYS14_25_V1-v1/00000/007B37D4-8B70-E411-BC2D-0025905A6066.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_tsg_PHYS14_25_V1-v1/00000/06843FC5-8370-E411-9B8C-0025905A60AA.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_tsg_PHYS14_25_V1-v1/00000/0A867F71-8C70-E411-9CC9-0025905A48D6.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_tsg_PHYS14_25_V1-v1/00000/0C1D0A70-8870-E411-BAB1-0025905A612C.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_tsg_PHYS14_25_V1-v1/00000/0EB35257-8470-E411-A458-0025905B85B2.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_tsg_PHYS14_25_V1-v1/00000/10D92E71-8470-E411-8DE2-0025905A60B8.root']

#process.source.fileNames=['root://cms-xrd-global.cern.ch//store/mc/Phys14DR/ZZTo4L_Tune4C_13TeV-powheg-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/04CD96C9-E269-E411-9D64-00266CF9ADA0.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/ZZTo4L_Tune4C_13TeV-powheg-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/10A409C9-E269-E411-8E48-00266CFAE8D0.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/ZZTo4L_Tune4C_13TeV-powheg-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/1C0E56C5-E269-E411-BCDD-00266CF9BE6C.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/ZZTo4L_Tune4C_13TeV-powheg-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/22C728CF-E269-E411-8850-00A0D1EE8EE0.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/ZZTo4L_Tune4C_13TeV-powheg-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/241933C6-E269-E411-B532-7845C4FC3A19.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/ZZTo4L_Tune4C_13TeV-powheg-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/7EEFB973-E269-E411-9407-848F69FD2949.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/ZZTo4L_Tune4C_13TeV-powheg-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/829AAAC9-E269-E411-9EAE-00266CFAEA68.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/ZZTo4L_Tune4C_13TeV-powheg-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/845BC5C8-E269-E411-B72C-00266CF9BBE4.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/ZZTo4L_Tune4C_13TeV-powheg-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/8606AA22-E869-E411-A156-848F69FD4ED1.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/ZZTo4L_Tune4C_13TeV-powheg-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/86B65CCA-E269-E411-A4BA-848F69FD2955.root'
#]

#process.source.fileNames=['root://cms-xrd-global.cern.ch//store/mc/Phys14DR/WZJetsTo3LNu_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/484D51C6-2673-E411-8AB0-001E67398412.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/WZJetsTo3LNu_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/5075EDC3-2573-E411-A168-002590A80E08.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/WZJetsTo3LNu_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/745E51CD-6473-E411-B67C-002590A80DF0.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/WZJetsTo3LNu_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/8033DEC0-2673-E411-AD03-001E67398052.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/WZJetsTo3LNu_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/9C944BF0-2573-E411-9940-002590200840.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/WZJetsTo3LNu_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/ECED17B7-2573-E411-A237-001E67398011.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/WZJetsTo3LNu_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/F2BACD92-2573-E411-9720-002590A83192.root'
#]
#process.source.fileNames=['root://cms-xrd-global.cern.ch//store/mc/Phys14DR/T_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/1E9DD9C1-8E7A-E411-87DD-1CC1DE04FF50.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/T_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/3C999DBB-8E7A-E411-A218-1CC1DE1D1E3C.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/T_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/3E092BBC-8E7A-E411-BD6A-1CC1DE1D03FC.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/T_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/563D4EBB-8E7A-E411-A87A-1CC1DE1CDF30.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/T_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/5E152ABE-8E7A-E411-A649-1CC1DE051038.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/T_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/687E24C9-8E7A-E411-96BB-78E7D1E4B772.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/T_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/AA10E6C4-8E7A-E411-B73C-1CC1DE0570A0.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/T_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/AA26E5B9-8E7A-E411-91F2-1CC1DE1CEFC8.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/T_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/D45C47C0-8E7A-E411-A890-1CC1DE0503C0.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/T_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/10000/0A182E14-8B7A-E411-BA19-00266CFFC598.root'
#]


#process.source.fileNames=['root://cms-xrd-global.cern.ch//store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/0432E62A-7A6C-E411-87BB-002590DB92A8.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/06C61714-7E6C-E411-9205-002590DB92A8.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/0EAD09A8-7C6C-E411-B903-0025901D493E.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/1E4D0DAE-7C6C-E411-B488-002590DB923C.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/2286DCDB-796C-E411-AAB4-002481E14D72.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/2683B2C5-7C6C-E411-BE0B-002590DB9214.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/28EF4E6A-7D6C-E411-A54F-0025907DCA38.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/2A733A85-7D6C-E411-8D2B-002481E14D72.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/3008BB28-7D6C-E411-AAC2-002590DB91F0.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/34167B14-7E6C-E411-A113-002590DB92A8.root'
#
#]

#process.source.fileNames=['root://cms-xrd-global.cern.ch//store/mc/Phys14DR/WJetsToLNu_13TeV-madgraph-pythia8-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/02215B44-2D70-E411-90A3-0025905A60B8.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/WJetsToLNu_13TeV-madgraph-pythia8-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/0603D444-2D70-E411-AF03-002618943922.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/WJetsToLNu_13TeV-madgraph-pythia8-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/08947C88-3570-E411-974E-002618FDA26D.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/WJetsToLNu_13TeV-madgraph-pythia8-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/0E8B81D9-2D70-E411-94AB-0025905A4964.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/WJetsToLNu_13TeV-madgraph-pythia8-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/1225D443-2D70-E411-9D85-0025905B85F6.root'
#]

#process.source.fileNames=['root://cms-xrd-global.cern.ch//store/mc/Phys14DR/QCD_Pt-20toInf_MuEnrichedPt15_PionKaonDecay_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v3/00000/F263724C-3FA7-E411-A3BE-002590A371AE.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/QCD_Pt-20toInf_MuEnrichedPt15_PionKaonDecay_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v3/10000/325BE5B9-AAA6-E411-8371-001E673972E2.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/QCD_Pt-20toInf_MuEnrichedPt15_PionKaonDecay_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v3/10000/381E5CF2-8BA7-E411-B4ED-0025B3E05C2C.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/QCD_Pt-20toInf_MuEnrichedPt15_PionKaonDecay_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v3/10000/42E3F46B-ABA6-E411-AD64-002590A887AC.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/QCD_Pt-20toInf_MuEnrichedPt15_PionKaonDecay_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v3/10000/50474FE6-8BA7-E411-AE1C-001E67397021.root',
#'root://cms-xrd-global.cern.ch//store/mc/Phys14DR/QCD_Pt-20toInf_MuEnrichedPt15_PionKaonDecay_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v3/10000/585CB6CF-ABA6-E411-96B9-001E673972E2.root'
#]

#working
process.source.fileNames=['root://cms-xrd-global.cern.ch//store/user/federica/MINIAOD/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/ZprimeToMuMu_M-5000_PU20BX25/150326_104035/0000/miniaod_1.root',
                           'root://cms-xrd-global.cern.ch//store/user/federica/MINIAOD/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/ZprimeToMuMu_M-5000_PU20BX25/150326_104035/0000/miniaod_10.root',
                          'root://cms-xrd-global.cern.ch//store/user/federica/MINIAOD/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/ZprimeToMuMu_M-5000_PU20BX25/150326_104035/0000/miniaod_2.root',
                          'root://cms-xrd-global.cern.ch//store/user/federica/MINIAOD/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/ZprimeToMuMu_M-5000_PU20BX25/150326_104035/0000/miniaod_3.root',
                           'root://cms-xrd-global.cern.ch//store/user/federica/MINIAOD/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/ZprimeToMuMu_M-5000_PU20BX25/150326_104035/0000/miniaod_4.root',
                           'root://cms-xrd-global.cern.ch//store/user/federica/MINIAOD/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/ZprimeToMuMu_M-5000_PU20BX25/150326_104035/0000/miniaod_5.root',
                           'root://cms-xrd-global.cern.ch//store/user/federica/MINIAOD/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/ZprimeToMuMu_M-5000_PU20BX25/150326_104035/0000/miniaod_6.root',
                           'root://cms-xrd-global.cern.ch//store/user/federica/MINIAOD/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/ZprimeToMuMu_M-5000_PU20BX25/150326_104035/0000/miniaod_7.root',
                           'root://cms-xrd-global.cern.ch//store/user/federica/MINIAOD/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/ZprimeToMuMu_M-5000_PU20BX25/150326_104035/0000/miniaod_8.root',
                          'root://cms-xrd-global.cern.ch//store/user/federica/MINIAOD/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/ZprimeToMuMu_M-5000_PU20BX25/150326_104035/0000/miniaod_9.root']

#AOD
#process.source.fileNames =['root://cms-xrd-global.cern.ch//store/user/federica/PATTuple/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/ZprimeToMuMu_M-5000_PU20BX25/150223_144430/0000/pat_1.root',
#'root://cms-xrd-global.cern.ch//store/user/federica/PATTuple/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/ZprimeToMuMu_M-5000_PU20BX25/150223_144430/0000/pat_10.root',
#'root://cms-xrd-global.cern.ch//store/user/federica/PATTuple/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/ZprimeToMuMu_M-5000_PU20BX25/150223_144430/0000/pat_2.root',
#'root://cms-xrd-global.cern.ch//store/user/federica/PATTuple/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/ZprimeToMuMu_M-5000_PU20BX25/150223_144430/0000/pat_3.root',
#'root://cms-xrd-global.cern.ch//store/user/federica/PATTuple/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/ZprimeToMuMu_M-5000_PU20BX25/150223_144430/0000/pat_4.root',
#'root://cms-xrd-global.cern.ch//store/user/federica/PATTuple/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/ZprimeToMuMu_M-5000_PU20BX25/150223_144430/0000/pat_5.root',
#'root://cms-xrd-global.cern.ch//store/user/federica/PATTuple/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/ZprimeToMuMu_M-5000_PU20BX25/150223_144430/0000/pat_6.root',
#'root://cms-xrd-global.cern.ch//store/user/federica/PATTuple/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/ZprimeToMuMu_M-5000_PU20BX25/150223_144430/0000/pat_7.root',
#'root://cms-xrd-global.cern.ch//store/user/federica/PATTuple/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/ZprimeToMuMu_M-5000_PU20BX25/150223_144430/0000/pat_8.root',
#'root://cms-xrd-global.cern.ch//store/user/federica/PATTuple/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/ZprimeToMuMu_M-5000_PU20BX25/150223_144430/0000/pat_9.root'
#]
#process.source.fileNames =['/store/mc/Phys14DR/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/MINIAODSIM/PU20bx25_tsg_PHYS14_25_V1-v1/00000/788396C0-9D6F-E411-97DF-002590494E34.root',
                    #       '/store/mc/Phys14DR/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/MINIAODSIM/PU20bx25_tsg_PHYS14_25_V1-v1/00000/3023C1A6-D56F-E411-B210-002590AC4C08.root',
                   #        '/store/mc/Phys14DR/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/MINIAODSIM/PU20bx25_tsg_PHYS14_25_V1-v1/00000/90575C8B-D56F-E411-A39B-0025904B1420.root',
                  #         '/store/mc/Phys14DR/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/MINIAODSIM/PU20bx25_tsg_PHYS14_25_V1-v1/00000/FCEF82CA-9D6F-E411-A2FC-002481E0D5CE.root',
                 #          '/store/mc/Phys14DR/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/MINIAODSIM/PU20bx25_tsg_PHYS14_25_V1-v1/10000/44B8EEE7-9A6F-E411-8858-002590DB0640.root',
                #           '/store/mc/Phys14DR/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/MINIAODSIM/PU20bx25_tsg_PHYS14_25_V1-v1/10000/F03F87D0-9A6F-E411-8BC4-00266CFFA5E0.root']

process.maxEvents.input = -1
from SUSYBSMAnalysis.Zprime2muAnalysis.hltTriggerMatch_cfi import trigger_match, prescaled_trigger_match, trigger_paths, prescaled_trigger_paths, overall_prescale, offline_pt_threshold, prescaled_offline_pt_threshold

# Since the prescaled trigger comes with different prescales in
# different runs/lumis, this filter prescales it to a common factor to
# make things simpler.
process.load('SUSYBSMAnalysis.Zprime2muAnalysis.PrescaleToCommon_cff')
process.PrescaleToCommon.trigger_paths = prescaled_trigger_paths
process.PrescaleToCommon.overall_prescale = overall_prescale

#process.load('SUSYBSMAnalysis.Zprime2muAnalysis.goodData_cff')
#process.load('HLTrigger.special.hltPhysicsDeclared_cfi')
#process.hltPhysicsDeclared.L1GtReadoutRecordTag = 'gtDigis'
#process.goodDataPrimaryVertexFilter = cms.path(process.primaryVertexFilter)
# The histogramming module that will be cloned multiple times below
# for making histograms with different cut/dilepton combinations.

if flag == "miniAOD":
	from SUSYBSMAnalysis.Zprime2muAnalysis.HistosFromPAT_cfi import HistosFromPAT
	HistosFromPAT.leptonsFromDileptons = False;
if flag == "AOD":
	from SUSYBSMAnalysis.Zprime2muAnalysis.HistosFromPAT_cfi import HistosFromPAT_AOD
	HistosFromPAT_AOD.leptonsFromDileptons = False ## True

# These modules define the basic selection cuts. For the monitoring
# sets below, we don't need to define a whole new module, since they
# just change one or two cuts -- see below.
#import SUSYBSMAnalysis.Zprime2muAnalysis.VBTFSelection_cff as VBTFSelection
#import SUSYBSMAnalysis.Zprime2muAnalysis.OurSelectionOld_cff as OurSelectionOld
#import SUSYBSMAnalysis.Zprime2muAnalysis.OurSelection2011EPS_cff as OurSelection2011EPS
import SUSYBSMAnalysis.Zprime2muAnalysis.OurSelectionNew_cff as OurSelectionNew
import SUSYBSMAnalysis.Zprime2muAnalysis.OurSelectionDec2012_cff as OurSelectionDec2012

# CandCombiner includes charge-conjugate decays with no way to turn it
# off. To get e.g. mu+mu+ separate from mu-mu-, cut on the sum of the
# pdgIds (= -26 for mu+mu+).
dils = [
    ('MuonsPlusMuonsMinus',          '%(leptons_name)s:muons@+ %(leptons_name)s:muons@-',         'daughter(0).pdgId() + daughter(1).pdgId() == 0'),
    ('MuonsPlusMuonsPlus',           '%(leptons_name)s:muons@+ %(leptons_name)s:muons@+',         'daughter(0).pdgId() + daughter(1).pdgId() == -26'),
    ('MuonsMinusMuonsMinus',         '%(leptons_name)s:muons@- %(leptons_name)s:muons@-',         'daughter(0).pdgId() + daughter(1).pdgId() == 26'),
    ('MuonsSameSign',                '%(leptons_name)s:muons@- %(leptons_name)s:muons@-',         ''),
    ('MuonsAllSigns',                '%(leptons_name)s:muons@- %(leptons_name)s:muons@-',         ''),
    ('MuonsPlusElectronsMinus',      '%(leptons_name)s:muons@+ %(leptons_name)s:electrons@-',     'daughter(0).pdgId() + daughter(1).pdgId() == -2'),
    ('MuonsMinusElectronsPlus',      '%(leptons_name)s:muons@- %(leptons_name)s:electrons@+',     'daughter(0).pdgId() + daughter(1).pdgId() == 2'),
    ('MuonsPlusElectronsPlus',       '%(leptons_name)s:muons@+ %(leptons_name)s:electrons@+',     'daughter(0).pdgId() + daughter(1).pdgId() == -24'),
    ('MuonsMinusElectronsMinus',     '%(leptons_name)s:muons@- %(leptons_name)s:electrons@-',     'daughter(0).pdgId() + daughter(1).pdgId() == 24'),
    ('MuonsElectronsOppSign',        '%(leptons_name)s:muons@+ %(leptons_name)s:electrons@-',     ''),
    ('MuonsElectronsSameSign',       '%(leptons_name)s:muons@+ %(leptons_name)s:electrons@+',     ''),
    ('MuonsElectronsAllSigns',       '%(leptons_name)s:muons@+ %(leptons_name)s:electrons@+',     ''),
    ]

# Define sets of cuts for which to make plots. If using a selection
# that doesn't have a trigger match, need to re-add a hltHighLevel
# filter somewhere below.
cuts = {
    #    'VBTF'     : VBTFSelection,
    #    'OurOld'   : OurSelectionOld,
    #    'OurEPS'   : OurSelection2011EPS,
    #'OurNew'   : OurSelectionNew,
    'Our2012'  : OurSelectionDec2012,
    #'OurNoIso' : OurSelectionDec2012,
    #'EmuVeto'  : OurSelectionDec2012,
    'Simple'   : OurSelectionDec2012, # The selection cuts in the module listed here are ignored below.
    #    'VBTFMuPrescaled' : VBTFSelection,
    #'OurMuPrescaledNew'  : OurSelectionNew,
    #'OurMuPrescaled2012' : OurSelectionDec2012 #doesn't work :( #to be checked 
    }

# Loop over all the cut sets defined and make the lepton, allDilepton
# (combinatorics only), and dilepton (apply cuts) modules for them.
for cut_name, Selection in cuts.iteritems():
    # Keep track of modules to put in the path for this set of cuts.
    path_list = []
    
    # Clone the LeptonProducer to make leptons with the set of cuts
    # we're doing here flagged.  I.e., muon_cuts in LeptonProducer
    # just marks each muon with a userInt "cutFor" that is 0 if it
    # passes the cuts, and non-0 otherwise; it does not actually drop
    # any of the muons. The cutFor flag actually gets ignored by the
    # LooseTightPairSelector in use for all the cuts above, at
    # present.
    leptons_name = cut_name + 'Leptons'
    if cut_name == 'Simple':
       ### muon_cuts = 'isGlobalMuon && pt > 20.'
        muon_cuts = '' ## this is a cut but it's applyed only at trigger level
    elif 'MuPrescaled' in cut_name:
        muon_cuts = Selection.loose_cut.replace('pt > %s' % offline_pt_threshold, 'pt > %s' % prescaled_offline_pt_threshold)
    else:
        muon_cuts = Selection.loose_cut
    leptons = process.leptons.clone(muon_cuts = muon_cuts)
    if cut_name == 'EmuVeto':
        leptons.electron_muon_veto_dR = 0.1
        # Keep using old TuneP for past selections
    if 'Dec2012' not in Selection.__file__:
        leptons.muon_track_for_momentum = cms.string('TunePNew')
    setattr(process, leptons_name, leptons)
    path_list.append(leptons)

    # Make all the combinations of dileptons we defined above.
    for dil_name, dil_decay, dil_cut in dils:
        # For the EmuVeto path, we only care about e-mu events.
        if cut_name == 'EmuVeto' and 'Electron' not in dil_name:
            continue

        # For the MuPrescaled paths, we don't care about e-mu events.
        if 'MuPrescaled' in cut_name and 'Electron' in dil_name:
            continue

        # Unique names for the modules: allname for the allDileptons,
        # and name for dileptons.
        name = cut_name + dil_name
        allname = 'all' + name

        alldil = Selection.allDimuons.clone(decay = dil_decay % locals(), cut = dil_cut)
        if 'AllSigns' in dil_name:
            alldil.checkCharge = cms.bool(False)
        dil = Selection.dimuons.clone(src = cms.InputTag(allname))

        # Implement the differences to the selections; currently, as
        # in Zprime2muCombiner, the cuts in loose_cut and
        # tight_cut are the ones actually used to drop leptons, and
        # not the ones passed into the LeptonProducer to set cutFor above.
        if cut_name == 'Simple':
            alldil.electron_cut_mask = cms.uint32(0)
            alldil.loose_cut = 'isGlobalMuon && pt > 20.'
            alldil.tight_cut = ''
            dil.max_candidates = 100
            dil.do_remove_overlap = False
            delattr(dil, 'back_to_back_cos_angle_min')
            delattr(dil, 'vertex_chi2_max')
            delattr(dil, 'dpt_over_pt_max')
        elif cut_name == 'OurNoIso':
            alldil.loose_cut = alldil.loose_cut.value().replace(' && isolationR03.sumPt / innerTrack.pt < 0.10', '')
        elif 'MuPrescaled' in cut_name:
            alldil.loose_cut = alldil.loose_cut.value().replace('pt > %s' % offline_pt_threshold, 'pt > %s' % prescaled_offline_pt_threshold)
            assert alldil.tight_cut == trigger_match
            alldil.tight_cut = prescaled_trigger_match

        # Histos now just needs to know which leptons and dileptons to use.
	if flag == 'miniAOD':
		histos = HistosFromPAT.clone(lepton_src = cms.InputTag(leptons_name, 'muons'), dilepton_src = cms.InputTag(name))
	
	if flag == 'AOD':
        	histos = HistosFromPAT_AOD.clone(lepton_src = cms.InputTag(leptons_name, 'muons'), dilepton_src = cms.InputTag(name))

        # Add all these modules to the process and the path list.
        setattr(process, allname, alldil)
        setattr(process, name, dil)
        setattr(process, name + 'Histos', histos)
        path_list.append(alldil * dil * histos)

    # Finally, make the path for this set of cuts.
    pathname = 'path' + cut_name
    pobj = process.muonPhotonMatch * reduce(lambda x,y: x*y, path_list)
    if 'VBTF' not in cut_name and cut_name != 'Simple':
        pobj = pobj#process.hltPhysicsDeclared * process.primaryVertexFilter * pobj
    if 'MuPrescaled' in cut_name:
        pobj = process.PrescaleToCommon * pobj
    if flag == 'miniAOD':
    	path = cms.Path(process.selectedPatMuons*pobj)
    if flag == 'AOD':	
    	path = cms.Path(pobj)#process.selectedPatMuons*pobj)
    setattr(process, pathname, path)

def ntuplify(process, fill_gen_info=False):
    process.SimpleNtupler = cms.EDAnalyzer('SimpleNtupler',
                                           dimu_src = cms.InputTag('SimpleMuonsAllSigns'),
                                           beamspot_src = cms.InputTag('offlineBeamSpot'),
                                           vertices_src = cms.InputTag('offlinePrimaryVertices'),
                                           )
    process.SimpleNtuplerEmu = process.SimpleNtupler.clone(dimu_src = cms.InputTag('SimpleMuonsElectronsAllSigns'))

    if fill_gen_info:
        from SUSYBSMAnalysis.Zprime2muAnalysis.HardInteraction_cff import hardInteraction
        process.SimpleNtupler.hardInteraction = hardInteraction

    ##process.pathSimple *= process.SimpleNtupler * process.SimpleNtuplerEmu

def printify(process):
    process.MessageLogger.categories.append('PrintEvent')

    process.load('HLTrigger.HLTcore.triggerSummaryAnalyzerAOD_cfi')
    process.triggerSummaryAnalyzerAOD.inputTag = cms.InputTag('hltTriggerSummaryAOD','','HLT')
    process.pathSimple *= process.triggerSummaryAnalyzerAOD

    process.PrintOriginalMuons = cms.EDAnalyzer('PrintEvent', muon_src = cms.InputTag('cleanPatMuonsTriggerMatch'), trigger_results_src = cms.InputTag('TriggerResults','','HLT'))
    #process.PrintOriginalMuons = cms.EDAnalyzer('PrintEvent', muon_src = cms.InputTag('selectedPatMuons'))
    #process.pathSimple *= process.PrintOriginalMuons

    pe = process.PrintEventSimple = cms.EDAnalyzer('PrintEvent', dilepton_src = cms.InputTag('SimpleMuonsPlusMuonsMinus'))
    process.pathSimple *= process.PrintEventSimple

    #- 2011-2012 selection (Nlayers > 8)
    #process.PrintEventOurNew = pe.clone(dilepton_src = cms.InputTag('OurNewMuonsPlusMuonsMinus'))
    #process.PrintEventOurNewSS = pe.clone(dilepton_src = cms.InputTag('OurNewMuonsSameSign'))
    #process.PrintEventOurNewEmu = pe.clone(dilepton_src = cms.InputTag('OurNewMuonsElectronsOppSign'))
    #process.pathOurNew *= process.PrintEventOurNew * process.PrintEventOurNewSS * process.PrintEventOurNewEmu

    #- December 2012 selection (Nlayers > 5, re-tuned TuneP, dpT/pT < 0.3)
    process.PrintEventOur2012    = pe.clone(dilepton_src = cms.InputTag('Our2012MuonsPlusMuonsMinus'))
    process.PrintEventOur2012SS  = pe.clone(dilepton_src = cms.InputTag('Our2012MuonsSameSign'))
    process.PrintEventOur2012Emu = pe.clone(dilepton_src = cms.InputTag('Our2012MuonsElectronsOppSign'))
    process.pathOur2012 *= process.PrintEventOur2012 * process.PrintEventOur2012SS * process.PrintEventOur2012Emu

def check_prescale(process, trigger_paths, hlt_process_name='HLT'):
    process.load('SUSYBSMAnalysis.Zprime2muAnalysis.CheckPrescale_cfi')
    process.CheckPrescale.trigger_paths = cms.vstring(*trigger_paths)
    process.pCheckPrescale = cms.Path(process.CheckPrescale)

def for_data(process):
    process.GlobalTag.globaltag = 'GR_P_V42_AN2::All'
    ntuplify(process)
    check_prescale(process, trigger_paths)

def for_mc(process, hlt_process_name, fill_gen_info):
    ntuplify(process, fill_gen_info)
    switch_hlt_process_name(process, hlt_process_name) # this must be done last (i.e. after anything that might have an InputTag for something HLT-related)

def get_dataset(run):
    #JMTBAD common with dataset_details in submit below, make a DataSamples.py?
    run = int(run)
    if 190450 <= run <= 191284:
        return '/SingleMu/tucker-datamc_SingleMuRun2012A_Prompt_190450_191284_20120418134612-57b19813ab8f2ab142c4566dc6738156/USER'
    else:
        raise ValueError('dunno how to do run %i' % run)

if 'int_data' in sys.argv:
    for_data(process)
    printify(process)
    
if 'int_mc' in sys.argv:
    for_mc(process, 'HLT', False)
    printify(process)
    
if 'gogo' in sys.argv:
    for_data(process)
    printify(process)
    
    n = sys.argv.index('gogo')
    run, lumi, event = sys.argv[n+1], sys.argv[n+2], sys.argv[n+3]
    print run, lumi, event
    run = int(run)
    lumi = int(lumi)
    event = int(event)
    filename = [x for x in sys.argv if x.endswith('.root')]
    if filename:
        filename = filename[0]
    else:
        dataset = get_dataset(run)
        print dataset
        output = os.popen('dbs search --url https://cmsdbsprod.cern.ch:8443/cms_dbs_ph_analysis_02_writer/servlet/DBSServlet --query="find file where dataset=%s and run=%s and lumi=%s"' % (dataset, run, lumi)).read()
        print repr(output)
        filename = [x for x in output.split('\n') if x.endswith('.root')][0]
    print filename
    process.source.fileNames = [filename]
    from SUSYBSMAnalysis.Zprime2muAnalysis.cmsswtools import set_events_to_process
    set_events_to_process(process, [(run, event)])

f = file('outfileMINIAOD_cut', 'w')
f.write(process.dumpPython())
f.close()

if __name__ == '__main__' and 'submit' in sys.argv:
    crab_cfg = '''
[CRAB]
jobtype = cmssw
scheduler = remoteGlidein
use_server = 0
[CMSSW]
datasetpath = %(ana_dataset)s
#dbs_url = https://cmsdbsprod.cern.ch:8443/cms_dbs_ph_analysis_02_writer/servlet/DBSServlet
dbs_url=phys03
pset = histos_crab.py
get_edm_output = 1
job_control
use_dbs3=1
[USER]
ui_working_dir = crab/crab_ana_datamc_%(name)s
return_data = 1
'''

    just_testing = 'testing' in sys.argv
        
    # Run on data.
    if 'no_data' not in sys.argv:
        from SUSYBSMAnalysis.Zprime2muAnalysis.goodlumis import *

        dataset_details = [
            ('SingleMuRun2012A_13Jul2012_190450_193751', '/SingleMu/slava-datamc_SingleMuRun2012A-13Jul2012_190450_193751_20121011073628-426a2d966f78bce6bde85f3ed41c07ba/USER'),
            ('SingleMuRun2012A_06Aug2012_190782_190949', '/SingleMu/slava-datamc_SingleMuRun2012A-recover-06Aug2012_190782_190949_20121011120430-426a2d966f78bce6bde85f3ed41c07ba/USER'),
            ('SingleMuRun2012B_13Jul2012_193752_196531', '/SingleMu/slava-datamc_SingleMuRun2012B-13Jul2012_193752_196531_20121012044921-426a2d966f78bce6bde85f3ed41c07ba/USER'),
            ('SingleMuRun2012C_24Aug2012_197556_198913', '/SingleMu/slava-datamc_SingleMuRun2012C-24Aug2012_197556_198913_20121012113325-426a2d966f78bce6bde85f3ed41c07ba/USER'),
            ('SingleMuRun2012C_Prompt_198934_203772',    '/SingleMu/slava-datamc_SingleMuRun2012C-Prompt_198934_203772_20121015023300-8627c6a48d2426dec4aa557620a039a0/USER'),
            ('SingleMuRun2012D_Prompt_203773_204563',    '/SingleMu/slava-datamc_SingleMuRun2012D-Prompt_203773_204563_20121016104501-8627c6a48d2426dec4aa557620a039a0/USER'),
            ('SingleMuRun2012D_Prompt_204564_206087',    '/SingleMu/slava-datamc_SingleMuRun2012D-Prompt_204564_206087_20121029121943-8627c6a48d2426dec4aa557620a039a0/USER'),
            ('SingleMuRun2012D_Prompt_206066_206066',    '/SingleMu/slava-datamc_SingleMuRun2012D-Prompt_206066_206066_20130115083834-5fce88899b8479b9df01fc5ef8a1e921/USER'),
            ('SingleMuRun2012D-Prompt_206088_206539',    '/SingleMu/slava-datamc_SingleMuRun2012D-Prompt_206088_206539_20121112085341-8627c6a48d2426dec4aa557620a039a0/USER'),
            ('SingleMuRun2012D-Prompt_206540_207900',    '/SingleMu/slava-datamc_SingleMuRun2012D-Prompt_206540_207900_20121203042806-8627c6a48d2426dec4aa557620a039a0/USER'),
            ('SingleMuRun2012D-Prompt_207901_208380',    '/SingleMu/slava-datamc_SingleMuRun2012D-Prompt_207901_208380_20121212090713-5fce88899b8479b9df01fc5ef8a1e921/USER'),
            ('SingleMuRun2012D-Prompt_208381_208700',    '/SingleMu/slava-datamc_SingleMuRun2012D-Prompt_208381_208700_20121217043712-5fce88899b8479b9df01fc5ef8a1e921/USER'),
#            ('SingleMuRun2012C-11Dec2012_201191_201191', '/SingleMu/slava-datamc_SingleMuRun2012C-EcalRecover_11Dec2012_201191_201191_20130115101201-5fce88899b8479b9df01fc5ef8a1e921/USER'),
            ]

        lumi_lists = [
#            'DCSOnly',
#            'Run2012PlusDCSOnlyMuonsOnly',
            'Run2012MuonsOnly',
            'Run2012',
            ]

        jobs = []
        for lumi_name in lumi_lists:
            ll = eval(lumi_name + '_ll') if lumi_name != 'NoLumiMask' else None
            for dd in dataset_details:
                jobs.append(dd + (lumi_name, ll))
                
        for dataset_name, ana_dataset, lumi_name, lumi_list in jobs:
            json_fn = 'tmp.json'
            lumi_list.writeJSON(json_fn)
            lumi_mask = 'lumi_mask = %s' % json_fn

            name = '%s_%s' % (lumi_name, dataset_name)
            print name

            new_py = open('histos.py').read()
            new_py += "\nfor_data(process)\n"
            open('histos_crab.py', 'wt').write(new_py)

            new_crab_cfg = crab_cfg % locals()

            job_control = '''
total_number_of_lumis = -1
lumis_per_job = 500
%(lumi_mask)s''' % locals()

            new_crab_cfg = new_crab_cfg.replace('job_control', job_control)
            open('crab.cfg', 'wt').write(new_crab_cfg)

            if not just_testing:
                os.system('crab -create -submit all')
            else:
                cmd = 'diff histos.py histos_crab.py | less'
                print cmd
                os.system(cmd)
                cmd = 'less crab.cfg'
                print cmd
                os.system(cmd)

        if not just_testing:
            os.system('rm crab.cfg histos_crab.py histos_crab.pyc tmp.json')

    if 'no_mc' not in sys.argv:
        # Set crab_cfg for MC.
        crab_cfg = crab_cfg.replace('job_control','''
total_number_of_events = -1
events_per_job = 50000
    ''')

        from SUSYBSMAnalysis.Zprime2muAnalysis.MCSamples import samples

        combine_dy_samples = len([x for x in samples if x.name in ['zmumu', 'dy120_c1', 'dy200_c1', 'dy500_c1', 'dy800_c1', 'dy1000_c1', 'dy1500_c1', 'dy2000_c1']]) > 0
        print 'combine_dy_samples:', combine_dy_samples

        for sample in reversed(samples):
            print sample.name

            new_py = open('histos.py').read()
            sample.fill_gen_info = sample.name in ['zmumu', 'dy120_c1', 'dy200_c1', 'dy500_c1', 'dy800_c1', 'dy1000_c1', 'dy1500_c1', 'dy2000_c1', 'zssm1000']
            new_py += "\nfor_mc(process, hlt_process_name='%(hlt_process_name)s', fill_gen_info=%(fill_gen_info)s)\n" % sample

            if combine_dy_samples and (sample.name == 'zmumu' or 'dy' in sample.name):
                mass_limits = {
                    'zmumu'    : (  20,    120),
                    'dy120_c1' : ( 120,    200),
                    'dy200_c1' : ( 200,    500),
                    'dy500_c1' : ( 500,    800),
                    'dy800_c1' : ( 800,   1000),
                    'dy1000_c1': (1000,   1500),
                    'dy1500_c1': (1500,   2000),
                    'dy2000_c1': (2000, 100000),
                    }
                lo,hi = mass_limits[sample.name]
                from SUSYBSMAnalysis.Zprime2muAnalysis.DYGenMassFilter_cfi import dy_gen_mass_cut
                new_cut = dy_gen_mass_cut % locals()

                new_py += '''
process.load('SUSYBSMAnalysis.Zprime2muAnalysis.DYGenMassFilter_cfi')

process.DYGenMassFilter.cut = "%(new_cut)s"
for pn,p in process.paths.items():
    setattr(process, pn, cms.Path(process.DYGenMassFilter*p._seq))
''' % locals()

            open('histos_crab.py', 'wt').write(new_py)

            open('crab.cfg', 'wt').write(crab_cfg % sample)
            if not just_testing:
                os.system('crab -create -submit all')
            else:
                cmd = 'diff histos.py histos_crab.py | less'
                print cmd
                os.system(cmd)
                cmd = 'less crab.cfg'
                print cmd
                os.system(cmd)

        if not just_testing:
            os.system('rm crab.cfg histos_crab.py histos_crab.pyc')
