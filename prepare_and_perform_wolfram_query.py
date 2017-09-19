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






class prepare_and_perform_query_with_assumptions:
    def __init__(self,input_string,assumption,appid,server,medical_test_wolram_query_flag,type_of_calculator):
        self.medical_test_wolram_query_flag = medical_test_wolram_query_flag
        self.assumption = assumption
        self.input_string = input_string
        self.create_and_perform_wolfram_query = wap.WolframAlphaEngine(appid, server)
        self.query_str = self.create_and_perform_wolfram_query.CreateQuery(self.input_string)
        self.wolframalpha_query = wap.WolframAlphaQuery(self.query_str, appid)
        self.type_of_calculator = int(type_of_calculator)
        
    def classify_formula_variables_into_subjective_or_objective(self):
        variable_list_subjective = []
        variable_list_objective = []
        for value_type_dict in self.assumption:
            if value_type_dict['type'][0] == 'FormulaVariable':
                if len(value_type_dict['value']) == 1:
                    variable_list_subjective.append(str(value_type_dict['value'][0].split('-_')[0])+'-_')
                else:
                    variable_list_objective.append(value_type_dict)
        return variable_list_subjective,variable_list_objective

    def grab_value_from_user_input_and_add_unit(self,user_input,unit):
        grabbed_value_list = re.findall(r'(\d+\.?\d*)',user_input)
        if len(grabbed_value_list) > 0:
            user_input = str(grabbed_value_list[0])+''+str(unit)
        return user_input

    def add_subjective_variables_for_blood_alcohol_content_calc(self,query_str,variable_list_subjective):
        names_of_variables_needed = ['number of drinks','time','body weight']
        for variable_number in range(len(variable_list_subjective)):
            user_input = raw_input('enter your '+str(names_of_variables_needed[variable_number])+' : ')
            if re.search(r'\d+\.?\d*',user_input):
                if names_of_variables_needed[variable_number] == 'time':
                   user_input = self.grab_value_from_user_input_and_add_unit(user_input,'min')
                elif names_of_variables_needed[variable_number] == 'body weight':
                   user_input = self.grab_value_from_user_input_and_add_unit(user_input,'kg')
                else:
                    user_input = re.findall(r'(\d+\.?\d*)',user_input)[0]
                query_str = query_str+"&assumption="+str(variable_list_subjective[variable_number])+str(user_input)
        return query_str

    def add_subjective_variables_for_physical_exercises_calc(self,query_str,variable_list_subjective):
        names_of_variables_needed = ['speed(in kmph)','distance(in kms)','inclination(enter 0 if flat surface)','age','height(in cms)','weight(kg)','resting heart rate']
        for variable_number in range(len(variable_list_subjective)):
            user_input = raw_input('enter your '+str(names_of_variables_needed[variable_number])+' : ')
            if re.search(r'\d+\.?\d*',user_input):
                if names_of_variables_needed[variable_number] == 'speed(in kmph)':
                   user_input = self.grab_value_from_user_input_and_add_unit(user_input,'kmph')
                elif names_of_variables_needed[variable_number] == 'distance(in kms)':
                   user_input = self.grab_value_from_user_input_and_add_unit(user_input,'km')
                elif names_of_variables_needed[variable_number] == 'inclination(enter 0 if flat surface)':
                    user_input = self.grab_value_from_user_input_and_add_unit(user_input,'%')
                else:
                    user_input = re.findall(r'(\d+\.?\d*)',user_input)[0]
                query_str = query_str+"&assumption="+str(variable_list_subjective[variable_number])+str(user_input)
        return query_str
    
    def add_subjective_formula_variables_to_query(self,variable_list_subjective):
        query_str = self.query_str
        names_of_variables_needed = []

        if self.type_of_calculator == 1:
            names_of_variables_needed = ['age','height(in cms.)','current body weight(in kg)','target body weight(in kg)','daily_calorie intake(optional)']
        if self.type_of_calculator == 2:
            names_of_variables_needed = ['age', 'LDL cholesterol', 'HDL cholesterol', 'systolic blood pressure','diastolic blood pressure']
        if self.type_of_calculator == 3:
            query_str = self.add_subjective_variables_for_physical_exercises_calc(query_str,variable_list_subjective)
            return query_str
        if self.type_of_calculator == 4:
            names_of_variables_needed = ['weight(in kg)','height(in cms)']
        if self.type_of_calculator == 5:
            query_str = self.add_subjective_variables_for_blood_alcohol_content_calc(query_str,variable_list_subjective)
            return query_str

        for variable_number in range(len(variable_list_subjective)):
            user_input = raw_input('enter your '+str(names_of_variables_needed[variable_number])+' : ')
            if re.search(r'\d+\.?\d*',user_input):
                user_input = re.findall(r'(\d+\.?\d*)',user_input)[0]
                query_str = query_str+"&assumption="+str(variable_list_subjective[variable_number])+str(user_input)
        return query_str
         
    def add_objective_formula_variables_to_query(self,variable_list_objective,query_str):
        for value_type_dict in variable_list_objective:
            choice_list = []
            
            for choice in value_type_dict["value"]:
                choice_list.append((str(choice).split('%3A'))[1])

            user_input_string = 'for '+str(re.findall(r'-_(\w+)%3A',str(choice))[0])+' enter'
            for index in range(len(choice_list)):
                user_input_string = str(user_input_string)+' '+str(index+1)+' if '+str(choice_list[index])+','
            user_input_objective = raw_input(user_input_string+": ")
            query_str = query_str+"&assumption="+str(value_type_dict["value"][int(user_input_objective)-1])
        return query_str

    def prepare_query_with_formula_variables(self):
        subjective_formula_variables,objective_formula_variables = self.classify_formula_variables_into_subjective_or_objective()
        query_str = self.add_subjective_formula_variables_to_query(subjective_formula_variables)
        query_str = self.add_objective_formula_variables_to_query(objective_formula_variables,query_str)
        return query_str
    
    def prepare_query_for_medical_tests(self):
        is_medical_test = False
        query_str = self.query_str
        for value_type_dict in self.assumption:
            for value in value_type_dict['value']:
                if 'MedicalTest' in value:
                    is_medical_test = True
                    query_str = query_str+"&assumption="+str(value)

        return query_str

    def perform_query(self):
        if self.medical_test_wolram_query_flag is False:
            query_str = self.prepare_query_with_formula_variables()
        else:
            query_str = self.prepare_query_for_medical_tests()
        
        result = self.create_and_perform_wolfram_query.PerformQuery(query_str)
        results = wap.WolframAlphaQueryResult(result)
        json_result= json.loads(results.JsonResult())
        return json_result