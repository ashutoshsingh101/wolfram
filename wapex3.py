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
import assumption_extraction
import prepare_and_perform_wolfram_query
import supervise_wolfram_extraction

def think_its_name(server,appid,input_string,type_of_calculator, medical_test_wolram_query_flag):
    get_assumptions = assumption_extraction.get_assumptions_and_formula_variables_from_basic_query(server,appid,input_string,type_of_calculator)
    assumption_list = get_assumptions.perform_basic_query_and_extract_assumptions()
    prepare_and_perform_query = prepare_and_perform_wolfram_query.prepare_and_perform_query_with_assumptions(input_string,assumption_list,appid,server,medical_test_wolram_query_flag,type_of_calculator)
    json_result = prepare_and_perform_query.perform_query()
    return json_result


        
def wolfram_query_for_calculators(count_of_re_querying,server,appid,input_string,type_of_calculator):
    medical_test_wolram_query_flag = False
    count_of_re_querying = count_of_re_querying + 1

    json_result = think_its_name(server,appid,input_string,type_of_calculator, medical_test_wolram_query_flag)
    supervise_data_extraction= supervise_wolfram_extraction.supervise_extraction_of_data(json_result,medical_test_wolram_query_flag,type_of_calculator)
    if count_of_re_querying < 3:
        if int(type_of_calculator) == 1:
            regimen_duration_info, maintain_bodyweight_table_dict = supervise_data_extraction.retrieving_all_pods_from_data()
            if type(regimen_duration_info) is bool or type(maintain_bodyweight_table_dict) is bool:
                wolfram_query_for_medical_calculators(count_of_re_querying,server,appid,input_string,type_of_calculator)
            if type(regimen_duration_info) is str and type(maintain_bodyweight_table_dict) is dict:
                print(regimen_duration_info)
                print(maintain_bodyweight_table_dict)

        if int(type_of_calculator) == 2:
            info_about_risk_probability = supervise_data_extraction.retrieving_all_pods_from_data()
            if type(info_about_risk_probability) is bool:
                wolfram_query_for_calculators(count_of_re_querying,server,appid,input_string,type_of_calculator)
            
            if type(info_about_risk_probability) is str:
                print(info_about_risk_probability)

        if int(type_of_calculator) == 3 or int(type_of_calculator) == 4 or int(type_of_calculator) == 5:
            result_dict = supervise_data_extraction.retrieving_all_pods_from_data()
            if type(result_dict) is bool:
                wolfram_query_for_calculators(count_of_re_querying,server,appid,input_string,type_of_calculator)
            if type(result_dict) is dict:
                print(result_dict)
    else:
        print('Sorry')


def for_calculator_operations():
    medical_test_wolram_query_flag = False
    count_of_re_querying = 0
    input_test_name = ''
    server = 'http://api.wolframalpha.com/v2/query.jsp'
    appid = 'EEKVX9-HGPX4GPUWY'
    input_string = ''
    type_of_calculator = raw_input('enter 1 to use weight loss, 2 to use heart disease risk, 3 to use physical exercise calculator, 4 to calculate BMI, 5 to measure your blood alcohol content: ')
    if int(type_of_calculator) == 1:
        input_string = 'weight loss'
    if int(type_of_calculator) == 2:
        input_string = 'heart disease risk'
    if  int(type_of_calculator) == 3:
        input_string = 'running'
    if int(type_of_calculator) == 4:
        input_string = 'BMI'
    if int(type_of_calculator) == 5:
        input_string = 'Am I too drunk to drive?'
    wolfram_query_for_calculators(count_of_re_querying,server,appid,input_string,type_of_calculator)




for_calculator_operations()