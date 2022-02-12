#-*- coding: utf-8 -*-
"""
@author:Bengali.ai
"""
#------------------------------------------------------------
from __future__ import print_function
#------------------------------------------------------------
from .langs import languages
from .parser import GraphemeParser

def graphemeParser(language):
    '''
        creates a grapheme parser object
        args:
            language    :   the specific language to use 
                available:
                    *   bangla  
                    *   malyalam    
                    *   tamil   
                    *   gujrati 
                    *   panjabi 
                    *   odiya   
                    *   hindi   
        returns:
            a Grapheme parser object

    '''
    return GraphemeParser(languages[language])