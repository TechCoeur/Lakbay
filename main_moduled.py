#===============================================================================================REQUISITES=========================================================================================================
from Imports import Imports
from ML_models import ML_models
from Region_Check import Region_Check
from Travel_Plan_Proc import Travel_Plan_Proc
from Firebase_API import Firebase_API
from API_Mobile import API_Mobile
from Travel_Plan_Tours import Travel_Plan_Tours
from Travel_Plan_Restos import Travel_Plan_Restos
from Travel_Plan_Hotels import Travel_Plan_Hotels

#import dependencies
Imports()

#models
ML_Models()

#Firebase API
Firebase_API()

#LOCATIONS
	

#TOURS
Travel_Plan_Tours()

#RESTOS
Travel_Plan_Restos()

#HOTELS
Travel_Plan_Hotels()

#MACHINE
API_Mobile()

"""	
	cat_list_tours = ['Water & Seaside Sports & Activities','Architecture, Art, History, & Museums','Places in the City'] #override
	cat_list_hotels = [2,3,4,5] #override
"""

Travel_Plan_Proc()
#TRAVEL PLAN_1
