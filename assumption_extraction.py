#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wap
import json
import re
import pandas as pd
import numpy as np
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
np.set_printoptions(threshold=np.inf)
import difflib
import time

class get_assumptions_and_formula_variables_from_basic_query():
    def __init__(self,server,appid,input_string,type_of_calculator):
        self.type_of_calculator = int(type_of_calculator)
        self.server = server
        self.appid = appid
        self.input_string = input_string
        self.create_and_perform_wolfram_query = wap.WolframAlphaEngine(self.appid, self.server)
        self.wolframalpha_query = wap.WolframAlphaQuery(self.input_string, self.appid)
    
    def give_value_for_assumption(self,value,assumption_dict):
        for in_list in value:
            for tuples in in_list:
                if str(tuples[0]) == 'input':
                    assumption_dict['value'].append(tuples[1])
        return assumption_dict


    def create_basic_query(self):
        query = self.create_and_perform_wolfram_query.CreateQuery(self.input_string) 
        
        scantimeout = '3.0'
        podtimeout = '4.0'
        formattimeout = '8.0'
        async = 'False'

        self.create_and_perform_wolfram_query.ScanTimeout = scantimeout
        self.create_and_perform_wolfram_query.PodTimeout = podtimeout
        self.create_and_perform_wolfram_query.FormatTimeout = formattimeout
        self.create_and_perform_wolfram_query.Async = async
        self.wolframalpha_query.ScanTimeout = scantimeout
        self.wolframalpha_query.PodTimeout = podtimeout
        self.wolframalpha_query.FormatTimeout = formattimeout
        self.wolframalpha_query.Async = async
        self.wolframalpha_query.ToURL()
        self.wolframalpha_query.AddPodTitle('')
        self.wolframalpha_query.AddPodIndex('')
        self.wolframalpha_query.AddPodScanner('')
        self.wolframalpha_query.AddPodState('')
        self.wolframalpha_query.AddAssumption('')

        query = self.wolframalpha_query.Query
        return query


    def perform_basic_query_and_extract_assumptions(self):
        query = self.create_basic_query()
        if self.type_of_calculator == 3:
            result = self.create_and_perform_wolfram_query.PerformQuery(query+'&assumption=*FS-_**Running.t--&assumption=*FVarOpt-_**Running.v-.*Running.age-.*Running.H--&assumption=*FVarOpt-_**Running.incline-.*Running.v-.*Running.age-.*Running.H-.*Running.HRResting--')
        elif self.type_of_calculator == 4:
             result = self.create_and_perform_wolfram_query.PerformQuery(query+'&assumption=*FVarOpt-_**BodyMassIndex.S--')
        else:
            result = self.create_and_perform_wolfram_query.PerformQuery(query)
        
        basic_query_result = wap.WolframAlphaQueryResult(result)
        assumptions = basic_query_result.Assumptions()

        outer_assumption_list = []
        for assumption in assumptions:
            assumption_dict = {'type':'',"value":[]}
            wap_assumptions = wap.Assumption(assumption)

            assumption_type = wap_assumptions.Type()

            assumption_dict['type'] = assumption_type
            word = wap_assumptions.Word()

            count = wap_assumptions.Count()

            value = wap_assumptions.Value()

            assumption_dict = self.give_value_for_assumption(value,assumption_dict)
            outer_assumption_list.append(assumption_dict)
        return outer_assumption_list