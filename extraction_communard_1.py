#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 12:07:55 2024

@author: silanoc
"""
from extraction_wd import *


def les_communards():
    """permet de tester """
    endpoint_url:str = "https://query.wikidata.org/sparql"
    query:str = """SELECT ?communard_ou_communarde ?communard_ou_communardeLabel WHERE {
      SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],fr". }
      ?communard_ou_communarde wdt:P106 wd:Q1780490.
    }"""
    extraction_communard = Extraction_wikidata(endpoint_url, query)
    df_communard = extraction_communard.extraire_et_df()
    print("--------- df--------------")
    print(df_communard)
    print("--------- describe--------------")
    print(df_communard.describe())

def tous_sur_tous_les_communard():
    ### les variables
    endpoint_url:str = "https://query.wikidata.org/sparql"
    query = """SELECT ?communard_ou_communarde ?communard_ou_communardeLabel ?p ?pLabel ?q ?qLabel WHERE {
      SERVICE wikibase:label { bd:serviceParam wikibase:language "fr,en".
                             ?communard_ou_communarde rdfs:label ?communard_ou_communardeLabel.
                             ?p rdfs:label ?pLabel.
                             ?q rdfs:label ?qLabel.}
      
      ?communard_ou_communarde wdt:P106 wd:Q1780490;
                               ?p ?q. 
    }
    """
    ### premiere extraction
    extraction_communard_tous_p_q = Extraction_wikidata(endpoint_url, query)
    df_communard_tous_p_q = extraction_communard_tous_p_q.extraire_et_df()
    ### apperçu
    #print(df_communard_tous_p_q)
    ##print(df_communard_tous_p_q.describe())
    ##print(df_communard_tous_p_q.columns)
    ### Nettoyer
    # retirer les colonnes "inutiles"
    df_nettoyage_colonne = df_communard_tous_p_q.loc[:,['communard_ou_communarde.value','p.value','q.value','communard_ou_communardeLabel.xml:lang','communard_ou_communardeLabel.value', 'pLabel.value','qLabel.value', 'q.xml:lang']]
    # garder le français
    df_nettoyage_langue = df_nettoyage_colonne[df_nettoyage_colonne['q.xml:lang'] == ("fr" or "NaN")]
    #print(df_nettoyage_langue.describe())
    return df_nettoyage_langue
    
df_tout_sur_tous_communard = (tous_sur_tous_les_communard())
print(df_tout_sur_tous_communard)