from googleplaces import GooglePlaces, types, lang
import difflib

API_KEY = 'AIzaSyCPwpHit50Q4FNFnNfrvmrhRoh4GGV-qOo'
google_places = GooglePlaces(API_KEY)


class find_health_personnel:
    def __init__(self,city,location,user_request_for_more_data):
        self.city = city
        self.location = location
        self.user_request_for_more_data = user_request_for_more_data
    
    def perform_query(self,query_result,result_list):
        for place in query_result.places:
            place.get_details()
            if str(place.rating) != '':
                result_list.append({'rating':str(place.rating),'name': str(place.name),'phone nummber': str(place.local_phone_number),'address':str(place.formatted_address.encode('utf-8'))})
            else:
                continue
        return result_list

    def forming_query_for_type_health(self,radius_of_search,health_keyword,count_for_requerying):
        count_,count_for_requerying = count_for_requerying + 1
        result_list = []
        query_result = google_places.nearby_search(
            location=''+str(self.location)+' '+str(self.city)+'', keyword=''+health_keyword+'',
            radius=radius_of_search, types=[types.TYPE_HEALTH])
        result_list = self.perform_query(query_result,result_list)
        if count_for_requerying < 3:
            if len(result_list) < 5:
                radius_of_search = radius_of_search + 3000
                self.forming_query_for_type_health(radius_of_search,health_keyword)
            else:
                return result_list
        else:
            return reasult_list
    
    def forming_query_for_type_dentist(self,radius_of_search,count_for_requerying):
        result_list = []
        count_for_requerying = count_for_requerying + 1
        query_result = google_places.nearby_search(
            location=''+str(self.location)+' '+str(self.city)+'', keyword='dentist',
            radius=radius_of_search, types=[types.TYPE_DENTIST])
        result_list = self.perform_query(query_result,result_list)
        if count_for_requerying < 3:
            if len(result_list) < 5:
                radius_of_search = radius_of_search + 3000
                self.forming_query_for_type_dentist(radius_of_search)
            else:
                return result_list
        else:
            return reasult_list

    def forming_query_for_type_pharmacy(self,radius_of_search,count_for_requerying):
        result_list = []
        count_for_requerying = count_for_requerying + 1
        query_result = google_places.nearby_search(
            location=''+str(self.location)+' '+str(self.city)+'', keyword='pharmacy',
            radius=radius_of_search, types=[types.TYPE_PHARMACY])
        result_list = self.perform_query(query_result,result_list)
        if count_for_requerying < 3:
            if len(result_list) < 5:
                radius_of_search = radius_of_search + 3000
                self.forming_query_for_type_pharmacy(radius_of_search)
            else:
                return result_list
        else:
            return reasult_list

    def forming_query_for_type_gym(self,radius_of_search,count_for_requerying):
        result_list = []
        count_for_requerying = count_for_requerying + 1
        query_result = google_places.nearby_search(
            location=''+str(self.location)+' '+str(self.city)+'', keyword='gym',
            radius=radius_of_search, types=[types.TYPE_GYM])
        result_list = self.perform_query(query_result,result_list)
        if count_for_requerying < 3: 
            if len(result_list) < 5:
                radius_of_search = radius_of_search + 3000
                self.forming_query_for_type_gym(radius_of_search)
            else:
                return result_list
        else:
            return reasult_list

    def forming_query_for_type_physiotherapist(self,radius_of_search,count_for_requerying):
        result_list = []
        count_for_requerying = count_for_requerying + 1
        query_result = google_places.nearby_search(
            location=''+str(self.location)+' '+str(self.city)+'', keyword='physiotherapist',
            radius=radius_of_search, types=[types.TYPE_PHYSIOTHERAPIST])
        result_list = self.perform_query(query_result,result_list)
        if count_for_requerying < 3:
            if len(result_list) < 5:
                radius_of_search = radius_of_search + 3000
                self.forming_query_for_type_physiotherapist(radius_of_search)
            else:
                return result_list
        else:
            return reasult_list

#---------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------            


class find_doctors:
    def __init__(self,city,location,user_request_for_more_data):
        self.city = city
        self.location = location
        self.user_request_for_more_data = user_request_for_more_data

    
    def determine_speciality_of_doctor(self):
        doctor_specialist_list = ['Gynecologist','Orthopedist','Ophthalmologist','Dermatologist','Physiotherapist',
        'Pediatrician','Psychiatrist','Infertility Specialist','Urologist','Gastroenterologist','Pulmonologist',
        'Neurologist','Neurosurgeon','Bariatric Surgeon','Rheumatologist','Chiropractor']
        
        user_input = raw_input('Enter the type of doctor you are looking for: ')
        highest_similarity = 0
        for specialist in doctor_specialist_list:
            similarity = difflib.SequenceMatcher(None,specialist.lower(),user_input.lower()).ratio()
            if similarity > highest_similarity:
                highest_similarity = similarity
                doctor_search_keyword = specialist.lower()
        validate_doctor_type = raw_input('Are you looking for a '+str(doctor_search_keyword)+'? Enter yes or no: ')

        if 'yes' in validate_doctor_type.lower():
            return doctor_search_keyword
        else:
            print('please check the spelling and try again')
            self.determine_speciality_of_doctor()

    def forming_query_for_type_health(self,doctor_search_keyword,radius_of_search,count_for_requerying):
        count_for_requerying = count_for_requerying + 1

        result_list = []
        query_result = google_places.nearby_search(
            location=''+str(self.location)+' '+str(self.city)+'', keyword=''+doctor_search_keyword+'',
            radius=radius_of_search, types=[types.TYPE_DOCTOR])
        
        for place in query_result.places:
            place.get_details()
            if str(place.rating) != '':
                result_list.append({'rating':str(place.rating),'name': str(place.name),'phone nummber': str(place.local_phone_number),'address':str(place.formatted_address.encode('utf-8'))})
            else:
                continue
        return result_list,count_for_requerying

    def controlling_radius_of_search_area(self,count_for_requerying):
        radius_of_search = 4000
        doctor_search_keyword  =  self.determine_speciality_of_doctor()
        result_list = []
        while len(result_list) < 5:
            if count_for_requerying > 2:
                break
            result_list,count_for_requerying = self.forming_query_for_type_health(doctor_search_keyword,radius_of_search,count_for_requerying)
            radius_of_search = radius_of_search + 3000

        if self.user_request_for_more_data is True:
            a = ''

        return result_list



#---------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------


city = raw_input('Enter your city: ')
location = raw_input('Enter your location: ')
user_request_for_more_data = True
finding_health_personnel = find_health_personnel(city,location,user_request_for_more_data)

identifier = raw_input('Enter 1 for dietician,2 for yoga trainer,3 for physiotherapist,4 for pharmacy,5 for dentist,6 for gyms,7 for doctors: ')
radius_of_search = 4000
count_for_requerying = 0
if int(identifier) == 1:
    result_list=finding_health_personnel.forming_query_for_type_health(radius_of_search,'dietician',count_for_requerying)
if int(identifier) == 2:
    result_list=finding_health_personnel.forming_query_for_type_health(radius_of_search,'yoga trainer',count_for_requerying)
if int(identifier) == 3:
    result_list=finding_health_personnel.forming_query_for_type_physiotherapist(radius_of_search,count_for_requerying)
if int(identifier) == 4:
    result_list=finding_health_personnel.forming_query_for_type_pharmacy(radius_of_search,count_for_requerying)
if int(identifier) == 5:
    result_list=finding_health_personnel.forming_query_for_type_dentist(radius_of_search,count_for_requerying)
if int(identifier) == 6:
    result_list=finding_health_personnel.forming_query_for_type_gym(radius_of_search,count_for_requerying)
if int(identifier) == 7:
    finding_doctors = find_doctors(city,location,user_request_for_more_data)
    result_list = finding_doctors.controlling_radius_of_search_area(count_for_requerying)
    


if len(result_list) == 0:
    print('sorry no results in your area')
else:
    print(result_list)


# print(dir(types))
# print(query_result.places)
# if query_result.has_attributions:
#     print query_result.html_attributions



# # print str(place.rating)+" ;"+str(place.name)+""+str()+" ;"+str(place.international_phone_number)+" ;"+str(place.local_phone_number)+" ;"+str(place.formatted_address.encode('utf-8'))#+" ;"+str(place.details)
# query_result = google_places.nearby_search(
#     location='kherani road mumbai', keyword='dietitian',
#     radius=5000, types=[types.TYPE_HEALTH])

# # print(dir(types))
# # print(query_result.places)
# # if query_result.has_attributions:
# #     print query_result.html_attributions

# for place in query_result.places:
#     print(place.get_details())
#     