import re

# class heath_insurance_cover:
#   def __init__(self,asd):
#       self.asd = asd
    
# def details_of_customer():
#     customer_details_dict = {'age':'','pincode':''}

#     customer_details_dict['age'] = raw_input('Enter your income: ')
#     customer_details_dict['pincode'] = raw_input('Enter your pin code')

#     return customer_details_dict


# def add_other_parent(list_of_persons_to_be_insured,father_or_mother):
#     if int(father_or_mother) == 1:
#         decision = raw_input('enter yes to add details of your mother also else enter no')
#     if int(father_or_mother) == 2:
#         decision = raw_input('enter yes to add details of your father also else enter no')
#     if 'no' in decision:
#         return list_of_persons_to_be_insured
#     if 'yes' in decision:
#         if int(father_or_mother) == 1:
#             age = raw_input('enter age of your mother')
#             list_of_persons_to_be_insured.append({'age':age,'gender':'female'})
#             return list_of_persons_to_be_insured
#         if int(father_or_mother) == 2:
#             age = raw_input('enter age of your father')
#             list_of_persons_to_be_insured.append({'age':age,'gender':'male'})
#             return list_of_persons_to_be_insured



# def collect_info_of_other_family_members(list_of_persons_to_be_insured,customer_details_dict):
#     parent_count = 2
#     spouse_flag = False
#     finished_adding_members = False
#     while finished_adding_members is False:
#         if spouse_flag is False:
#             add_family_member_identifier = raw_input('press 1 to add spouse, 2 to add parent,3 to add children: ')
#         else:
#             add_family_member_identifier = raw_input('press 2 to add parent,3 to add children: ')
#         if int(add_family_member_identifier) == 1:
#             age_of_spouse = raw_input('enter age of your spouse: ')
#             if customer_details_dict['gender'] == 'male':
#                 list_of_persons_to_be_insured.append({'age':age_of_spouse,'gender':'female'})
#             else:
#                 list_of_persons_to_be_insured.append({'age':age_of_spouse,'gender':'male'})
#             spouse_flag = True 
#         if int(add_family_member_identifier) == 2:
#             while parent_count > 0:
#                 father_or_mother = raw_input('press 1 to add details of father, 2 to add details of mother:' )
#                 if int(father_or_mother) == 1:
#                     age = raw_input('enter age of your father')
#                     list_of_persons_to_be_insured.append({'age':age,'gender':'male'})
#                     list_of_persons_to_be_insured = add_other_parent(list_of_persons_to_be_insured,father_or_mother)
#                 if int(father_or_mother) ==2:
#                     age = raw_input('enter age of your mother')
#                     list_of_persons_to_be_insured.append({'age':age,'gender':'female'})
#                     list_of_persons_to_be_insured = add_other_parent(list_of_persons_to_be_insured,father_or_mother)
#                 parent_count = parent_count - 1
#         if int(add_family_member_identifier) == 3:
#             son_or_daughter = raw_input('press 1 to add details of son, 2 to add details of daughter:' )
#             if int(son_or_daughter) == 1:
#                 age_of_son = raw_input('enter age of your son: ')
#                 list_of_persons_to_be_insured.append({'age':age_of_son,'gender':'male'})
#             if int(son_or_daughter) == 2:
#                 age_of_daughter = raw_input('enter age of your daughter: ')
#                 list_of_persons_to_be_insured.append({'age':age_of_daughter,'gender':'female'})
#         exit_flag = raw_input('press 0 if finished adding else press 1: ')
#         if int(exit_flag) == 0:
#             finished_adding_members = True
#     return list_of_persons_to_be_insured



# def buy_for_self_or_family():
#     customer_details_dict = details_of_customer()
#     list_of_persons_to_be_insured = []
#     persons_to_be_insured_identifier = raw_input('enter 1 if you want insurance for youself,2 for the family,3 yourself plus family: ')

#     if int(persons_to_be_insured_identifier) == 1:
#         list_of_persons_to_be_insured.append(customer_details_dict)
#     elif int(persons_to_be_insured_identifier) == 2:
#         list_of_persons_to_be_insured.append(customer_details_dict)
#         list_of_persons_to_be_insured=collect_info_of_other_family_members(list_of_persons_to_be_insured,customer_details_dict)
#     else:
#         list_of_persons_to_be_insured=collect_info_of_other_family_members(list_of_persons_to_be_insured,customer_details_dict)

#     print(list_of_persons_to_be_insured)




# # a = heath_insurance_cover('ashutosh')
# buy_for_self_or_family()

class calculate_health_insurance_cover_range:

    def __init__(self):
        pass


    def enter_age_person_by_person(self,number_of_persons_to_be_insured,for_medical_condition_flag):
        list_of_age_of_people = []
        if for_medical_condition_flag is False:
            print('sorry did not get that,please enter age of one person at a time')
        else:
            print('enter age of persons with medical conditions one at a time')    
        for index in range(int(number_of_persons_to_be_insured)):
            age = raw_input('enter age of person '+str(index + 1)+': ')
            list_of_age_of_people.append(int(age))
        return list_of_age_of_people



    def ask_for_details_age_and_income(self,identifier_of_persons_to_be_insured):
        list_of_age_of_people = []
        income = ''
        number_of_persons_to_be_insured = '11'
        if int(identifier_of_persons_to_be_insured) == 1:
            age_of_customer = raw_input('enter your age(in yrs): ')
            list_of_age_of_people.append(age_of_customer)
            income = raw_input('enter your yearly income in lacs: ')

        if int(identifier_of_persons_to_be_insured) == 2 or int(identifier_of_persons_to_be_insured) == 3:
            while int(number_of_persons_to_be_insured) > 10:
                number_of_persons_to_be_insured = raw_input('enter no. of persons to buy insurance for: ')
                if int(number_of_persons_to_be_insured) > 10:
                    print('Please enter a number upto 10')
            age_string = raw_input('enter age(in yrs) of persons(eg. 06,32,45,22,56,etc: ')
            age_list = age_string.split(',')
            if len(age_list) == int(number_of_persons_to_be_insured):
                for age in age_list:
                    list_of_age_of_people.append(int(age))
            else:
                for_medical_condition_flag = False
                list_of_age_of_people = self.enter_age_person_by_person(number_of_persons_to_be_insured,for_medical_condition_flag)
            income = raw_input('enter your house hold yearly incoome in lacs: ')

        return income ,list_of_age_of_people 


    def deciding_cover_based_on_city(self,pin_code,income):
        tier_1_pin_dict = {'560001':'bangalore','400001':'mumbai','500001':'hyderabaad','600001':'chennai','110000':'delhi','700001':'kolkata'}
        cover_flag = False
        tier_1_pin_list = tier_1_pin_dict.keys()
        for pin in tier_1_pin_list:
            if pin_code[0:3] == pin[0:3]:
                cover = float(income)
                cover_flag = True
                break
        if cover_flag is False:
            cover = float(income) - 1.0

        return cover

    def deciding_cover_based_on_age_and_medical_condition(self,cover,list_of_age_of_people,ages_of_persons_with_medical_condition):
        total_cover = 0.00
        for age in list_of_age_of_people:
            if float(age) <= 25.00:
                if age in ages_of_persons_with_medical_condition:
                    total_cover = total_cover + 1.2*cover
                else:
                    total_cover = total_cover + cover
            elif float(age) <= 30.00:
                if age in ages_of_persons_with_medical_condition:
                    total_cover = total_cover + 1.33*cover + 1.0
                else:
                    total_cover = total_cover + cover + 1.0
            elif float(age) <= 35.00:
                if age in ages_of_persons_with_medical_condition:
                    total_cover = total_cover + 1.4*cover + 2.0
                else:
                    total_cover = total_cover + cover + 2.0
            elif float(age) <= 40.00:
                if age in ages_of_persons_with_medical_condition:
                    total_cover = total_cover + 1.5*cover + 3.0
                else:
                    total_cover = total_cover + cover + 3.0
            elif float(age) <= 90.00:
                if age in ages_of_persons_with_medical_condition:
                    total_cover = total_cover + 1.5*cover + 5.0
                else:
                    total_cover = total_cover + cover + 5.0
        return total_cover

    def get_information_about_medical_condition(self,number_of_persons_to_be_insured):
        disease_history_identifier = raw_input('Enter 1 if any medical condition, 2 if not: ')
        ages_of_persons_with_medical_condition = []
        if int(disease_history_identifier) == 1:
            if number_of_persons_to_be_insured == 1:
                number_of_people_with_medical_condition = '1'
                return '1'
            else:
                number_of_people_with_medical_condition = raw_input("enter the number of persons with medical conditions: ")
                for_medical_condition_flag = True
                ages_of_persons_with_medical_condition = self.enter_age_person_by_person(number_of_people_with_medical_condition,for_medical_condition_flag)
                return ages_of_persons_with_medical_condition
        else:
            return 'no disease history'

    def decide_final_range_of_cover(self,cover,income,total_cover):
        lower_limit_of_cover = cover
        if total_cover <= 2*float(income):
            upper_limit_of_cover = total_cover
        else:
            if 2*float(income) <= 25.00:
                upper_limit_of_cover = 2*float(income)
            else:
                upper_limit_of_cover = 25.00

        return lower_limit_of_cover,upper_limit_of_cover

    def who_to_buy_insurance_for(self):
        pin_validated = False
        no_of_trials_for_pin = 0
        while pin_validated is False:
            pin_code = raw_input('enter your pincode(india): ')
            if re.search(r'\d{6}',pin_code) and len(pin_code) == 6:
                pin_code = re.findall(r'(\d{6})',pin_code)[0]
                pin_validated = True
            else:
                print('Please enter a valid pin code')
        identifier_of_persons_to_be_insured = raw_input('enter 1 if you want insurance for youself,2 for the family,3 yourself plus family: ')
        income ,list_of_age_of_people = self.ask_for_details_age_and_income(identifier_of_persons_to_be_insured)
        cover = self.deciding_cover_based_on_city(pin_code,income)
        number_of_persons_to_be_insured = len(list_of_age_of_people)
        information_about_medical_condition = self.get_information_about_medical_condition(number_of_persons_to_be_insured)
        if information_about_medical_condition == '1':
            total_cover = self.deciding_cover_based_on_age_and_medical_condition(cover,list_of_age_of_people,list_of_age_of_people)
        if type(information_about_medical_condition) is list:
            total_cover = self.deciding_cover_based_on_age_and_medical_condition(cover,list_of_age_of_people,information_about_medical_condition)
        if information_about_medical_condition == 'no disease history':
             total_cover = self.deciding_cover_based_on_age_and_medical_condition(cover,list_of_age_of_people,[])
        lower_limit_of_cover,upper_limit_of_cover = self.decide_final_range_of_cover(cover,income,total_cover)
        print('your cover: '+str(lower_limit_of_cover)+' - '+str(upper_limit_of_cover))

    
calculate_health_insurance_cover = calculate_health_insurance_cover_range()
calculate_health_insurance_cover.who_to_buy_insurance_for()