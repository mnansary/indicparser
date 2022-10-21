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
                                3. connector 
        '''
        # assignment
        self.lang=language.iden
        self.vds=language.vowel_diacritics 
        self.cds=language.consonant_diacritics
        self.connector=language.connector
        
        # error check -- type
        assert type(self.vds)==list,"Vowel Diacritics Is not a list"
        assert type(self.cds)==list,"Consonant Diacritics Is not a list"
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
            if d not in self.vds:
                idxs.append(idx)
        idxs.append(len(decomp))
        for i in range(len(idxs)-1):
            sub=decomp[idxs[i]:idxs[i+1]]
            grapheme=''
            for s in sub:
                grapheme+=s
            graphemes.append(grapheme)
        
        # correct consonant diacs
        graphemes=[g for g in graphemes if g is not None]
        for idx,d in enumerate(graphemes):
            if d in self.cds:
                graphemes[idx]=graphemes[idx-1]+d
                graphemes[idx-1]=None
        graphemes=[g for g in graphemes if g is not None]
        
        return graphemes

    def space_correction(self,comps):
        for idx in range(len(comps)-1):
            if comps[idx]==" " and comps[idx+1]==" ":
                    comps[idx]=None 
        comps=[g for g in comps if g is not None]
        if comps[0]==" ":comps=comps[1:]
        if comps[-1]==" ":comps=comps[:-1]
        return comps
    
        
    def no_space_char_addition(self,decomp):
        for idx,comp in enumerate(decomp):
            if idx<len(decomp)-1:
                if decomp[idx+1] in ["\u200d","\u200c"] and decomp[idx]!=self.connector:
                    decomp[idx]+=decomp[idx+1]
                    decomp[idx+1]=None
        decomp=[i for i in decomp if i is not None]
        return decomp

    def process(self,text,merge_spaces=False):
        '''
            useage:
                text                :   the text to process
                merge_spaces        :   default:False
                                        if space merging is used
                                            *  multiple consecutive spaces will combine into one space 
                                            *  begining and ending spaces will be stripped
                                        

        '''
        assert type(text)==str,"input data is not type text"
        #try:
        decomp=[ch for ch in text]
        # handle no - space
        decomp=self.no_space_char_addition(decomp)
        # root
        decomp=self.get_root_from_decomp(decomp)
        result=self.get_graphemes_from_decomp(decomp)
        # spacing
        if merge_spaces:
            result=self.space_correction(result)
        return result
        # except Exception as e:
        #     print("given text:",text,"extracted components:",decomp)
        #     print("error:",e)
            
        
            