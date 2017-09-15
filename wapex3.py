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

#--------------------------------------------------------------------------------------------------------------------------------
total_tests_of_labtests_online = [u'5-HIAA', u'17-Hydroxyprogesterone', u'A/G Ratio', u'A1c', u'Absolute neutrophils', u'ACE', u'Acetaminophen', u'Acetylcholinesterase', u'AChR Antibody', u'ACR', u'ACT', u'ACTH', u'Adenosine Deaminase', u'ADH', u'AFB Testing', u'AFP Maternal', u'AFP Tumor Markers', u'Albumin', u'Aldolase', u'Aldosterone', u'ALK Mutation (Gene Rearrangement)', u'Allergy Blood Testing', u'ALP', u'Alpha-1 Antitrypsin', u'ALT', u'AMA', u'Amikacin',
u'Aminoglycoside Antibiotics', u'Ammonia', u'Amniocentesis', u'Amylase', u'ANA', u'ANCA', u'Androstenedione', u'Anion Gap', u'Anti-CCP', u'Anti-DNase B', u'Anti-dsDNA', u'Anti-LKM-1', u'Anti-Mullerian Hormone', u'Antibody ID, RBC', u'Anticentromere Antibody', 
u'Antiphospholipids', u'Antithrombin', u'APC Resistance', u'Apo A-I', u'Apo B', u'APOE Genotyping, Alzheimer Disease',
u'APOE Genotyping, CVD', u'aPTT', u'Arbovirus Testing', u'Arterial Blood Gases', u'ASCA', u'ASO', u'AST', u'Autoantibodies', u'B Vitamins', u'B-cell Ig Gene Rearrangement', u'BCR-ABL1', u'Beta-2 Glycoprotein 1 Antibodies', u'Beta-2 Microglobulin Kidney Disease', u'Beta-2 Microglobulin Tumor Marker', u'Bicarbonate', u'Bilirubin', u'Blood Culture', u'Blood Donation', u'Blood Gases', u'Blood Ketones', u'Blood Smear',
u'Blood Transfusion', u'Blood Typing', u'BMP', u'BNP', u'Body Fluid Analysis', u'Bone Markers', u'Bone Marrow', u'BRCA', u'Breast Cancer, Gene Expression', u'BUN', u'c-ANCA', u'C-peptide', u'C-telopeptide', u'C. difficile', u'CA 15-3', u'CA 19-9', u'CA 27.29', u'CA-125', u'Caffeine', u'Calcitonin', u'Calcium', u'Calprotectin', u'CALR Mutation', u'Carbamazepine', u'Cardiac Biomarkers',
u'Cardiac Risk', u'Cardiolipin Antibodies', u'Catecholamines', u'CBC', u'CCP Antibody', u'CD4 Count', u'CEA', u'Celiac Disease Tests', u'Cell-Free Fetal DNA', u'Ceruloplasmin', u'CF Gene Mutations', u'Chem 7', u'Chemistry Panels', u'Chickenpox', u'Chlamydia', u'Chloride', u'Cholesterol', u'Cholinesterase', u'Chromogranin A', u'Chromosome Analysis', u'Chymotrypsin', u'CK', u'CK-MB', u'Clopidogrel',
u'Clostridium difficile', u'CMP', u'CMV Tests', u'CO2, Total',
u'Coagulation Cascade', u'Coagulation Factors', u'Cold Agglutinins', u'Complement', u'Coombs, Direct', u'Coombs, Indirect', u'Copper', u'Cortisol', u'Creatinine', u'Creatinine Clearance', u'CRP', u'CRP, high-sensitivity', u'Cryoglobulins', u'CSF Analysis', u'Cyclosporine', u'Cystatin C', u'D-dimer', u'DCP', u'Dengue Fever', u'DHEAS', u'Diabetes Autoantibodies', u'Differential', u'Digoxin', u'Dilute Russell Viper Venom Test',
u'Direct Antiglobulin Test', u'Direct LDL-C', u'Drug Abuse Testing', u'E. coli (Shiga toxin-producing)', u'EBV Antibodies', u'eGFR', u'EGFR [Her-1]', u'Elastase', u'Electrolytes', u'Electrophoresis', u'Emergency/Overdose Drug Testing', u'ENA Panel', u'Erythropoietin',
u'ESR', u'Estradiol', u'Estrogen/Progesterone Receptors', u'Estrogens', u'Ethanol', u'Factor V Leiden', u'Fecal Fat', u'Fecal Occult Blood Test', u'Ferritin', u'fFN', u'Fibrinogen', u'FIP1L1-PDGFRA', u'First Trimester Screening', u'Flu Tests', u'Folate', u'Free Light Chains', u'Free T3', u'Free T4', u'Fructosamine', u'FSH', u'Fungal Tests', u'G6PD', u'Gastrin', u'Genetic Tests for Targeted Cancer Therapy', u'Gentamicin', u'GFR', u'GGT', u'GI Pathogens Panel', u'Glucose',
u'Gonorrhea', u'Gram Stain', u'Group B Strep Screen', u'Growth Hormone', u'H. pylori', u'Haptoglobin', u'hCG Pregnancy', u'hCG Tumor Marker', u'HDL', u'HE4', u'Heavy Metals', u'Hematocrit', u'Hemoglobin', u'Hemoglobin A1c', u'Hemoglobinopathy Eval', u'Heparin Anti-Xa', u'Hepatitis A', u'Hepatitis B', u'Hepatitis C', u'Hepatitis Panel', u'HER2/neu', u'Herpes', u'Histamine', u'Histone Antibody', 
u'HIT Antibody', u'HIV Antiretroviral Drug Resistance', u'HIV Screening', u'HIV Viral Load', u'HLA Testing', u'HLA-B27', u'Homocysteine', u'HPV', u'hs-CRP', u'HTLV', u'IgE, Total', u'IGF-1', u'IMA', u'Immunoelectrophoresis', u'Immunoglobulins', u'Immunophenotyping', u'Influenza Tests', 
u'Inhibin A', u'INR', u'Insulin', u'Interleukin-6', u'Intrinsic Factor Antibody', u'Ionized Calcium', u'Iron Tests', u'Iron, serum', u'IRT', u'JAK2 Mutation', u'Kappa/Lambda Ratio', u'Karyotyping', u'Ketones, blood', u'Kidney Stone Analysis', u'Kidney Stone Risk Panel', u'KRAS Mutation', u'Lactate', u'Lactoferrin', u'Lactose Tolerance Tests', u'LD', u'LDL', u'LDL-P', u'Lead', u'Legionella', u'Leptin', u'Levetiracetam', u'LH', u'Lipase', u'Lipid Profile', u'Lithium', u'Liver Panel', u'Lp(a)', u'Lp-PLA2',
u'Lupus Anticoagulant Testing', u'Lyme Disease', u'Magnesium', u'MCH', u'MCHC', u'MCV', u'Measles', u'Mercury', u'Metanephrines', u'Methotrexate', u'Microalbumin', u'MMA', u'Mononucleosis Test', u'MPA', u'MRSA Screening', u'MTHFR Mutation', u'Mumps', u'Mycoplasma', u'Myoglobin', u'Nicotine / Cotinine', u'NIPT', u'Non-HDL Cholesterol', u'NT-proBNP', u'Osmolality', u'Ova and Parasite Exam', u'p-ANCA', u'P1NP', u'Pap Test', u'PAPP-A', u'Parietal Cell Antibody', u'Parvovirus B19', u'Pericardial Fluid Analysis', u'Peritoneal Fluid Analysis',
u'Pertussis', u'Pharmacogenetic Tests', u'Phenobarbital', u'Phenytoin', u'Phosphorus', u'Plasma Metanephrines', u'Platelet Count', u'Platelet Function Tests', u'Pleural Fluid Analysis', u'PML-RARA', u'Porphyrins', u'Potassium', u'Prealbumin', u'Pregnancy Test', u'Pregnenolone', u'Procalcitonin', u'Progesterone', u'Progesterone Receptors', u'Prolactin',
u'Protein C', u'Protein Electrophoresis', u'Protein S', u'Prothrombin Time', u'PSA', u'PSEN1', u'Pseudocholinesterase', u'PT 20210', u'PTH', u'PTT', u'Quad Screen', u'RBC', u'RBC Antibody ID', u'RBC Antibody Screen', u'RDW', u'Renal Panel', u'Renin', u'Reticulocytes', u'Rheumatoid Factor', u'RSV', u'Rubella', u'Salicylates', u'Second Trimester Screening', u'Semen Analysis', u'Sensitivity Testing', u'Serotonin', u'Serum Iron', u'SHBG', u'Shingles', u'Sickle Cell Tests', u'Sirolimus', u'Smooth Muscle Antibody', u'SMRP', u'Sodium',
u'Soluble Transferrin Receptor', u'Sputum Culture', u'Stool Culture', u'Strep Throat Test', u'Susceptibility Testing', u'Sweat Chloride', u'Synovial Fluid Analysis', u'Syphilis', u'T-Cell Receptor Gene Rearrangement', u'T3', u'T4', u'Tacrolimus', u'Tau/A\xdf42', u'TB Screening Tests', u'Testosterone', u'Theophylline', u'Therapeutic Drug Monitoring', u'Throat Culture', 
u'Thrombin Time', u'Thyroglobulin', u'Thyroid Antibodies', u'Thyroid Panel', u'TIBC', u'Tobramycin', u'TORCH', u'Total Protein', u'Toxoplasmosis', u'TPMT', u'Trace Minerals', u'Transferrin', u'Trichomonas', u'Triglycerides', u'Triple Screen', u'Troponin', u'Tryptase', u'TSH', u'tTG Antibody', u'Tumor Markers', u'UIBC', u'UP/CR', u'Uric Acid', u'Urinalysis', u'Urine Albumin', u'Urine Culture', u'Urine Metanephrines', u'Urine Protein', u'Valproic Acid', u'Vancomycin', u'Vitamin A', u'Vitamin B12', u'Vitamin D', u'Vitamin K', u'VLDL',
u'VMA', u'von Willebrand Factor', u'Warfarin Sensitivity Testing', u'WBC', u'WBC Differential', u'West Nile Virus', u'Whooping Cough', u'Widal Test', u'Wound Culture', u'Xylose Absorption', u'Zika Virus Testing', u'ZPP']

#-----------------------------------------------------------------------------------------------------------------------------------------------

total_tests_available = ['AMYLASE ', 'CHLORIDE', 'HOMOCYSTEINE', 'IRON TOTAL IRON BINDING CAPACITY (TIBC) ', 
'% TRANSFERRIN SATURATION BLOOD UREA NITROGEN (BUN)', 'CREATININE - SERUM', 'URIC ACID', 'CALCIUM', 
'BUN / SR.CREATININE RATIO', 'SODIUM', 'LIPASE', 'FOLLICLE STIMULATING HORMONE (FSH)', 'LUTEINISING HORMONE (LH)', 
'PROLACTIN (PRL)', 'TOTAL CHOLESTEROL', 'HDL CHOLESTEROL - DIRECT', 'TRIGLYCERIDES', 'LDL CHOLESTEROL - DIRECT', 
'TC/ HDL CHOLESTEROL RATIO', 'LDL / HDL RATIO', 'VLDL CHOLESTEROL', 'NON-HDL CHOLESTEROL', 'ALKALINE PHOSPHATASE', 
'BILIRUBIN -DIRECT', 'BILIRUBIN - TOTAL', 'BILIRUBIN (INDIRECT)', 'GAMMA GLUTAMYL TRANSFERASE (GGT)', 
'ASPARTATE AMINOTRANSFERASE (SGOT )', 'ALANINE TRANSAMINASE (SGPT)', 'PROTEIN - TOTAL', 'ALBUMIN - SERUM', 'SERUM GLOBULIN', 
'SERUM ALBUMIN/GLOBULIN RATIO', 'TESTOSTERONE', 'TOTAL TRIIODOTHYRONINE (T3)', 'TOTAL THYROXINE (T4) ', 'THYROID STIMULATING HORMONE (TSH)', '25-OH VITAMIN D (TOTAL)', 'VITAMIN B-12', 
'AVERAGE BLOOD GLUCOSE (ABG)', 'HbA1c', 'TOTAL LEUCOCYTES COUNT', 'NEUTROPHILS', 'LYMPHOCYTE PERCENTAGE', 'MONOCYTES', 'EOSINOPHILS', 'BASOPHILS', 'IMMATURE GRANULOCYTE PERCENTAGE(IG%)', 
'NEUTROPHILS - ABSOLUTE COUNT', 'LYMPHOCYTES - ABSOLUTE COUNT', 'MONOCYTES - ABSOLUTE COUNT', 'BASOPHILS - ABSOLUTE COUNT', 'EOSINOPHILS - ABSOLUTE COUNT', 'IMMATURE GRANULOCYTES(IG)', 'TOTAL RBC', 
'NUCLEATED RED BLOOD CELLS', 'NUCLEATED RED BLOOD CELLS %', 'HEMOGLOBIN', 'HEMATOCRIT(PCV)', 'MEAN CORPUSCULAR VOLUME(MCV)', 'MEAN CORPUSCULAR HEMOGLOBIN(MCH)', 'MEAN CORP.HEMO.CONC(MCHC)', 'RED CELL DISTRIBUTION WIDTH - SD(RDW-SD)', 
'RED CELL DISTRIBUTION WIDTH (RDW-CV)', 'PLATELET DISTRIBUTION WIDTH(PDW)', 'MEAN PLATELET VOLUME(MPV)', 'PLATELET COUNT', 'PLATELET TO LARGE CELL RATIO(PLCR)', 'PLATELETCRIT(PCT)']


#---------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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

#----------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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

    def add_subjective_formula_variables_to_query(self,variable_list_subjective):
        query_str = self.query_str
        names_of_variables_needed = []

        if self.type_of_calculator == 1:
            names_of_variables_needed = ['age','height(in cms.)','current body weight(in kg)','target body weight(in kg)','daily_calorie intake(optional)']
        if self.type_of_calculator == 2:
            names_of_variables_needed = ['age', 'LDL cholesterol', 'HDL cholesterol', 'systolic blood pressure','diastolic blood pressure']
        if self.type_of_calculator == 3:
            names_of_variables_needed = ['speed(in kmph)','distance(in kms)','inclination(enter 0 if flat surface)','age','height(in cms)','weight(kg)','resting heart rate']
        for variable_number in range(len(variable_list_subjective)):
            user_input = raw_input('enter your '+str(names_of_variables_needed[variable_number])+' : ')
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

#--------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class extract_medical_test_data:
    def __init__(self,pods_list):
        self.pods_list = pods_list

    def extract_data_out_of_pod_reference_distribution(self,pod_item):
        reference_distribution_table_dict = {}
        for inner_pod_list in pod_item:
            if type(inner_pod_list) is list and inner_pod_list[0] == 'subpod':
                for subpod_item in inner_pod_list:
                    if type(subpod_item) is list and subpod_item[0] == 'plaintext':
                        reference_distribution_table_rows = subpod_item[1].split('\n')
                        for row_index in range(len(reference_distribution_table_rows)):

                            columns = reference_distribution_table_rows[row_index].split('|')
                            if len(columns) >=2:
                                reference_distribution_table_dict.update({''+(columns[0].encode('utf-8')).strip()+'':''+(columns[1].encode('utf-8')).strip()+''})
        return reference_distribution_table_dict

    def extract_data_from_required_pods(self):
        medical_information_obtained = False
        for pod_item in self.pods_list:
            if type(pod_item) is list:
                for inner_pod_list in pod_item:
                    if inner_pod_list[0] == 'title':
                        if 'Reference distribution' in inner_pod_list[1]:
                            medical_information_obtained = True
                            print('required pods working')
                            reference_distribution_table_dict = self.extract_data_out_of_pod_reference_distribution(pod_item)
                            print(reference_distribution_table_dict)
        if medical_information_obtained is True:
            return reference_distribution_table_dict
        if medical_information_obtained is False:
            return f

#--------------------------------------------------------------------------------------------------------------------------------- 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


class extract_weight_loss_data:
    def __init__(self,pods_list):
        self.pods_list = pods_list
    
    def extract_data_out_of_pod_regimen_duration(self,pod_item):
        data = ''
        for inner_pod_list in pod_item:
            if type(inner_pod_list) is list and inner_pod_list[0] == 'subpod':
                for subpod_item in inner_pod_list:
                    if type(subpod_item) is list and subpod_item[0] == 'plaintext':
                        data = str(subpod_item[1])
        return data                

    def extract_data_out_of_pod_maintain_bodyweight(self,pod_item):
        maintain_bodyweight_table_dict = {}
        for inner_pod_list in pod_item:
            if type(inner_pod_list) is list and inner_pod_list[0] == 'subpod':
                for subpod_item in inner_pod_list:
                    if type(subpod_item) is list and subpod_item[0] == 'plaintext':
                        maintain_bodyweight_table_rows = subpod_item[1].split('\n')
                        for row_index in range(1,len(maintain_bodyweight_table_rows)):
                            row_data_list = str(maintain_bodyweight_table_rows[row_index]).split(' | ')
                            if len(row_data_list) == 3:
                                maintain_bodyweight_table_dict.update({''+str(row_data_list[0])+'':{'weight':''+str(row_data_list[1])+'','calorie intake':''+str(row_data_list[2])+''}})
        return maintain_bodyweight_table_dict   


    def extract_data_from_required_pods(self):
        for pod_item in self.pods_list:
            if type(pod_item) is list:
                for inner_pod_list in pod_item:
                    if inner_pod_list[0] == 'title':
                        if 'Weight loss regimen duration' in inner_pod_list[1]:
                            regimen_duration_info = self.extract_data_out_of_pod_regimen_duration(pod_item)
                        if 'Caloric intake to maintain body weight' in inner_pod_list[1]:
                            maintain_bodyweight_table_dict = self.extract_data_out_of_pod_maintain_bodyweight(pod_item)
        return regimen_duration_info, maintain_bodyweight_table_dict 

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class extract_heart_risk_data:
    
    def __init__(self,pods_list):
        self.pods_list = pods_list

    def extract_data_out_of_pod_10year_risk(self,pod_item):
        for inner_pod_list in pod_item:
            if type(inner_pod_list) is list and inner_pod_list[0] == 'subpod':
                for subpod_item in inner_pod_list:
                    if type(subpod_item) is list and subpod_item[0] == 'plaintext':
                        data = str(subpod_item[1].split('\n')[0])
        return data                


    def extract_data_from_required_pods(self):
        for pod_item in self.pods_list:
            if type(pod_item) is list:
                for inner_pod_list in pod_item:
                    if inner_pod_list[0] == 'title':
                        if '10-year risk of developing coronary heart disease' in inner_pod_list[1]:
                            data = self.extract_data_out_of_pod_10year_risk(pod_item)
        return data


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class extract_physical_excercises_data:
    def __init__(self,pods_list):
        self.pods_list = pods_list

    def extract_data_out_of_pod_metabolic_activities(self,pod_item):
        
        metabolic_activities_table_dict = {}
        for inner_pod_list in pod_item:
            if type(inner_pod_list) is list and inner_pod_list[0] == 'subpod':
                for subpod_item in inner_pod_list:
                    if type(subpod_item) is list and subpod_item[0] == 'plaintext':
                        metabolic_activities_table_rows =  subpod_item[1].split('\n')
                        for row in metabolic_activities_table_rows:
                            columns = row.split('|')
                            if len(columns) >= 2 :
                                metabolic_activities_table_dict.update({''+(columns[0].encode('utf-8')).strip()+'':''+(columns[1].encode('utf-8')).strip()+''})
        return metabolic_activities_table_dict
    

    def extract_data_from_required_pods(self):
        
        for pod_item in self.pods_list:
            if type(pod_item) is list:
                for inner_pod_list in pod_item:
                    if inner_pod_list[0] == 'title':
                        if 'Metabolic properties' in inner_pod_list[1]:
                            metabolic_activities_table_dict = self.extract_data_out_of_pod_metabolic_activities(pod_item)
        return metabolic_activities_table_dict




#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class supervise_extraction_of_data():
    def __init__(self,json_result,medical_test_wolram_query_flag,type_of_calculator):
        self.json_result = json_result
        self.medical_test_wolram_query_flag = medical_test_wolram_query_flag
        self.type_of_calculator = int(type_of_calculator)
            
    def retrieving_all_pods_from_data(self):
        pods_list = []
        for result in self.json_result:
            if type(result) is list:
                if result[0] == 'pod':
                    pods_list.append(result)
        if self.medical_test_wolram_query_flag is False:
            if self.type_of_calculator == 1:
                extracting_weight_loss_data = extract_weight_loss_data(pods_list)
                regimen_duration_info, maintain_bodyweight_table_dict = extracting_weight_loss_data.extract_data_from_required_pods()
                return regimen_duration_info, maintain_bodyweight_table_dict
            if self.type_of_calculator == 2:
                extracting_heart_risk_data = extract_heart_risk_data(pods_list)
                info_about_risk_probability = extracting_heart_risk_data.extract_data_from_required_pods()
                return info_about_risk_probability
            if self.type_of_calculator == 3:
                extracting_physical_excercises_data = extract_physical_excercises_data(pods_list)
                metabolic_activities_table_dict = extracting_physical_excercises_data.extract_data_from_required_pods()
                return metabolic_activities_table_dict
        if self.medical_test_wolram_query_flag is True:
            extracting_medical_test_data = extract_medical_test_data(pods_list)
            print('supervise working')
            reference_distribution_table_dict = extracting_medical_test_data.extract_data_from_required_pods()
            return reference_distribution_table_dict

                   
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


class calculate_percentile:
    def __init__(self,total_tests_available):
        self.total_tests_available = total_tests_available


    def take_user_input_and_find_nearest_match(self):
        input_test_name = raw_input('Enter test name: ')
        input_value = raw_input('Enter your value: ')
        highest_similarity = 0
        for test_name in self.total_tests_available:
            similarity = difflib.SequenceMatcher(None,test_name.lower(),input_test_name.lower()).ratio()
            if similarity > highest_similarity:
                highest_similarity = similarity
                name_to_use_for_calculation = test_name

        return highest_similarity,name_to_use_for_calculation,input_value,input_test_name



    def connect_to_database_to_form_result_dictionary (self,name_to_use_for_calculation,input_value):
        db = MySQLdb.connect(host = 'localhost',
            user = 'root',
            password = 'jubi',
            db = 'parsed')

        query = 'select test.value from test where test.name like '+ '\"%'+name_to_use_for_calculation+'%\"'+''
        
        all_values_of_given_test = pd.read_sql(query, db)
        length = len(all_values_of_given_test)
        if length > 3000:
            count = 0
            for value in all_values_of_given_test['value'].values:
                try:
                    if type(value) is float or type(value) is str or type(value) is int:
                        if float(value) < float(input_value):
                            count = count + 1
                    else:
                        length = length - 1
                        continue
                except ValueError:
                    length = length - 1
                    continue

        percentage_below_you = float(count)/float(length) *100
        percentage_above_you = 100 - percentage_below_you

        data_dictionary = {'percentage of people below your value':percentage_below_you,'percentage of people above your value':percentage_above_you}

        return data_dictionary

    def validate_and_perform_operation(self,count,flag_for_wolfram):
        count = count + 1 
        highest_similarity,name_to_use_for_calculation,input_value,input_test_name= self.take_user_input_and_find_nearest_match()
        validate_test_name = raw_input("Is "+name_to_use_for_calculation+" the test you are looking for?Enter Yes or No: ")
        if validate_test_name.lower() == 'yes':
            data_dictionary = self.connect_to_database_to_form_result_dictionary (name_to_use_for_calculation,input_value)
            return data_dictionary,input_value,input_test_name
        
        else:
            if highest_similarity > .7 and count < 3:
                print('Check the spelling and try again')
                self.validate_and_perform_operation(count,flag_for_wolfram)
            else:
                print('trying to find your answer on internet')
                flag_for_wolfram = True
                return flag_for_wolfram,input_value,input_test_name

#----------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------

def check_validity_of_test_name_for_wolfram_query_try(input_test_name):
    highest_similarity = 0
    for test_name in total_tests_of_labtests_online:
        similarity = difflib.SequenceMatcher(None,str(test_name.encode('utf-8')).lower(),input_test_name.lower()).ratio()
        if similarity > highest_similarity:
            highest_similarity = similarity
            name_to_use_for_calculation = test_name
    re_query_flag = True
    if highest_similarity > .7:
        validate_test_name = raw_input("Is "+name_to_use_for_calculation+" the test you are looking for?Enter Yes or No: ")
        
        if validate_test_name.lower() == 'yes':
            re_query_flag = True
            return re_query_flag
        else:
            return re_query_flag
    else:
        return re_query_flag



def wolfram_query_for_medical_test(medical_test_wolram_query_flag,input_test_name,count_of_re_querying,server,appid,input_string,type_of_calculator): 
    count_of_re_querying = count_of_re_querying + 1
    print('c : '+str(count_of_re_querying))
    
    get_assumptions = get_assumptions_and_formula_variables_from_basic_query(server,appid,input_string,type_of_calculator)
    assumption_list = get_assumptions.perform_basic_query_and_extract_assumptions()
 
    prepare_and_perform_query = prepare_and_perform_query_with_assumptions(input_string,assumption_list,appid,server,medical_test_wolram_query_flag,type_of_calculator)
    json_result = prepare_and_perform_query.perform_query()

    supervise_data_extraction= supervise_extraction_of_data(json_result,medical_test_wolram_query_flag,type_of_calculator)
    
    if medical_test_wolram_query_flag is True:
        reference_distribution_table_dict = supervise_data_extraction.retrieving_all_pods_from_data()
        print('dict : '+str(reference_distribution_table_dict))
        if type(reference_distribution_table_dict) is bool and count_of_re_querying < 5:
            if count_of_re_querying == 1:
                re_query_flag = check_validity_of_test_name_for_wolfram_query_try(input_test_name)
            if count_of_re_querying > 1:
                re_query_flag = True
            if re_query_flag is False:
                print('Sorry, Name Not Found')
            else: 
                wolfram_query_for_medical_test(medical_test_wolram_query_flag,input_test_name,count_of_re_querying,server,appid,input_string,type_of_calculator)
        
    else:
        if int(type_of_calculator) == 1:
            regimen_duration_info, maintain_bodyweight_table_dict = supervise_data_extraction.retrieving_all_pods_from_data()
            print('\n')
            print('\n')
            print(regimen_duration_info)
            print('\n')
            print('\n')
            print(maintain_bodyweight_table_dict)

        if int(type_of_calculator) == 2:
            info_about_risk_probability = supervise_data_extraction.retrieving_all_pods_from_data()
            print('\n')
            print('\n')
            print(info_about_risk_probability)

        if int(type_of_calculator) == 3:
            metabolic_activities_table_dict =  supervise_data_extraction.retrieving_all_pods_from_data()
            print('\n')
            print('\n')
            print(metabolic_activities_table_dict)







def for_medical_test_operations():
    medical_test_wolram_query_flag = True
    calculate_percentile_for_test = calculate_percentile(total_tests_available)
    count_of_spelling_mistake_try = 0
    flag_for_calling_wolfram = False
    result_of_percentile_class,input_value,input_test_name= calculate_percentile_for_test.validate_and_perform_operation(count_of_spelling_mistake_try,flag_for_calling_wolfram)


    server = 'http://api.wolframalpha.com/v2/query.jsp'
    appid = 'EEKVX9-HGPX4GPUWY'
    input_string = ""+str(input_test_name)+" "+str(input_value)

    if type(result_of_percentile_class) is dict:
        percentile_inforamtion = result_of_percentile_class
        print(percentile_inforamtion)
    if type(result_of_percentile_class) is bool:
        flag_for_calling_wolfram = result_of_percentile_class
        if flag_for_calling_wolfram is True:
            count_of_re_querying = 0
            type_of_calculator = 0
            wolfram_query_for_medical_test(medical_test_wolram_query_flag,input_test_name,count_of_re_querying,server,appid,input_string,type_of_calculator)



def for_calculator_operations():
    medical_test_wolram_query_flag = False
    count_of_re_querying = 0
    input_test_name = ''
    server = 'http://api.wolframalpha.com/v2/query.jsp'
    appid = 'EEKVX9-HGPX4GPUWY'
    input_string = ''
    type_of_calculator = raw_input('enter 1 to use weight loss, 2 to use heart disease risk, 3 to use physical exercise calculator: ')
    if int(type_of_calculator) == 1:
        input_string = 'weight loss'

    if int(type_of_calculator) == 2:
        input_string = 'heart disease risk'

    if  int(type_of_calculator) == 3:
        input_string = 'running'
    
    wolfram_query_for_medical_test(medical_test_wolram_query_flag,input_test_name,count_of_re_querying,server,appid,input_string,type_of_calculator)





what_to_do = raw_input('enter 1 to use calculators and 2 to find about medical test value: ')

if int(what_to_do) == 1:
    for_calculator_operations()
if int(what_to_do) == 2:
    for_medical_test_operations()
