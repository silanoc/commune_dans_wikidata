#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from SPARQLWrapper import SPARQLWrapper, JSON
import pandas as pd
import sys

class Extraction_wikidata():
    def __init__(self, endpoint_url:str, query:str):
        self.endpoint_url:str = endpoint_url
        self.query:str = query
        
    def get_results(self, endpoint_url:str, query:str):
        user_agent = "WDQS-example Python/%s.%s" % (sys.version_info[0], sys.version_info[1])
        # TODO adjust user agent; see https://w.wiki/CX6
        sparql = SPARQLWrapper(endpoint_url, agent = user_agent)
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        return sparql.query().convert()
    
    def json_to_df(self, entree):
        #results = sparql.query().convert()
        df_results = pd.json_normalize(entree["results"]["bindings"])
        return df_results
    
    def extraire_et_df(self):
        extract_json = self.get_results(self.endpoint_url, self.query)
        extract_df = self.json_to_df(extract_json)
        return extract_df

 


if __name__ == '__main__':
    pass

    