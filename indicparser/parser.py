#-*- coding: utf-8 -*-
"""
@author:Bengali.ai
"""
#------------------------------------------------------------
from __future__ import print_function
#------------------------------------------------------------
class GraphemeParser(object):
    def __init__(self,language):
        '''
            initializes a grapheme parser for a given language
            args:
                language  :   a class that contains list of:
                                1. vowel_diacritics 
                                2. consonant_diacritics
                                3. modifiers
                                and 
                                4. connector 
        '''
        # assignment
        self.vds=language.vowel_diacritics 
        self.cds=language.consonant_diacritics
        self.mds=language.modifiers
        self.connector=language.connector
        # error check -- type
        assert type(self.vds)==list,"Vowel Diacritics Is not a list"
        assert type(self.cds)==list,"Consonant Diacritics Is not a list"
        assert type(self.mds)==list,"Modifiers Is not a list"
        assert type(self.connector)==str,"Connector Is not a string"
    
    def get_root_from_decomp(self,decomp):
        '''
            creates grapheme root based list 
        '''
        if self.connector in decomp:   
            c_idxs = [i for i, x in enumerate(decomp) if x == self.connector]
            # component wise index map    
            comps=[[cid-1,cid,cid+1] for cid in c_idxs ]
            # merge multi root
            r_decomp = []
            while len(comps)>0:
                first, *rest = comps
                first = set(first)

                lf = -1
                while len(first)>lf:
                    lf = len(first)

                    rest2 = []
                    for r in rest:
                        if len(first.intersection(set(r)))>0:
                            first |= set(r)
                        else:
                            rest2.append(r)     
                    rest = rest2

                r_decomp.append(sorted(list(first)))
                comps = rest
            
            # add    
            combs=[]
            for ridx in r_decomp:
                comb=''
                for i in ridx:
                    comb+=decomp[i]
                combs.append(comb)
                for i in ridx:
                    if i==ridx[-1]:
                        decomp[i]=comb
                    else:
                        decomp[i]=None
            decomp=[d for d in decomp if d is not None]
            
            return decomp
        else:
            return decomp

    def get_graphemes_from_decomp(self,decomp):
        '''
        create graphemes from decomp
        '''
        graphemes=[]
        idxs=[]
        for idx,d in enumerate(decomp):
            if d not in self.vds+self.mds:
                idxs.append(idx)
        idxs.append(len(decomp))
        for i in range(len(idxs)-1):
            sub=decomp[idxs[i]:idxs[i+1]]
            grapheme=''
            for s in sub:
                grapheme+=s
            graphemes.append(grapheme)
        return graphemes

    def process(self,word,return_graphemes=True,debug=False):
        '''
            processes a word for creating:
            if return_graphemes=True (default):
                * components
            else:                 
                * grapheme 
        '''
        try:
            decomp=[ch for ch in word]
            decomp=self.get_root_from_decomp(decomp)
            if debug:
                print(decomp)        
            if return_graphemes:
                return self.get_graphemes_from_decomp(decomp)
            else:
                components=[]
                for comp in decomp:
                    if comp in self.vds+self.mds:
                        components.append(comp)
                    else:
                        cd_val=None
                        for cd in self.cds:
                            if cd in comp:
                                comp=comp.replace(cd,"")
                                cd_val=cd
                        components.append(comp)
                        if cd_val is not None:
                            components.append(cd_val)
                return components
        except Exception as e:
            if debug:
                print(e)
                print(word)                        
