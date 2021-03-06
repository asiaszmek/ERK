import glob
import os
from lxml import etree
from xml.etree import ElementTree as ET
import numpy as np

mol_change={'ERK':'ERK', 'MEK':'MEK','MKP1':'MKP1','PP2A':'PP2A','Raf':'Raf1','bRaf':'bRaf','dRaf1Ras':'dRaf1Ras','cAMP':'cAMP','PDE2':'PDE2','PDE4':'PDE4','PKA':'PKA','PKAc':'PKAc','Src':'Src','Cbl':'Cbl','CRKC3G':'CRKC3G','CamCa4':'CamCa4','CKpCamCa4':'CKpCamCa4','CKpCamCa4SynGap':'CKpCamCa4SynGap','PP1':'PP1','IP35':'Ip35','NgCam':'NgCam','Grb2':'Grb2','Sos':'Sos','Shc':'Shc','RasGRF':'RasGRF','Epac':'Epac','RasGDP':'RasGDP','Rap1GDP':'Rap1GDP','Ca':'Ca','Leak':'Leak','pmca':'pmca','ncx':'ncx','Calbin':'Calbin','CB':'CB','rasGap':'rasGap','rapGap':'rap1Gap','SynGap':'SynGap'}

#'bRaf':'154.514','Ca':'43.204','Calbin':'150702.742','CamCa4':'1.121',



PATH='./'
pattern_IC=PATH+'IC'+'*.xml'
IC_filename=sorted(glob.glob(pattern_IC)) 
list=[]				
#
for filename in IC_filename:
    find_name=os.path.split(filename)[-1]
    root=ET.parse(filename).getroot()
    for mol in mol_change.keys():
        for molecules in mol_change[mol]:
            for elem in root:
                for subelem in elem:
                    if molecules== subelem.attrib['specieID']:
                        val=float(subelem.attrib['value'])
                        list.append((molecules,val))
    outfname=find_name.split('-')[-1]+'-'+'molchange.txt'
    header='mol_change'+' '+'value'
    f=open(outfname, 'w')
    f.write(header+'\n')
    np.savetxt(f,list,fmt='%s', delimiter='   ')
    f.close()

    
for mol in mol_change.keys():
     for elem in root:
         for subelem in elem:
             if mol==subelem.attrib['specieID']:
                 list=[]
                 val=float(subelem.attrib['value'])
                 list.append((mol,val))
                 
        header='mol_change'+' '+'value'
        outfname='trialnad.txt'
        f=open(outfname, 'w')
        f.write(header+'\n')
        np.savetxt(f,list,fmt='%s', delimiter='   ')
