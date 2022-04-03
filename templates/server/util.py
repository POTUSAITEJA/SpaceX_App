import json
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

__orbit = None
__Gridfins = None
__reused = None
__legs = None
__landingpad = None
__launchsite = None
__data_columns = None
__model = None


def get_launch_prediction(payloadmass,flights,Block,ReusedCount,orbit,gridfins,reused,legs,landingpad,launchsite):
    try:
        loc_index1 = __data_columns.index(orbit.lower())
        loc_index6 = __data_columns.index(launchsite.lower())
        loc_index5 = __data_columns.index(landingpad.lower())
        #loc_index4 = np.where(X.columns==serial)
        loc_index2 = __data_columns.index(gridfins.lower())
        loc_index3 = __data_columns.index(reused.lower())
        loc_index4 = __data_columns.index(legs.lower())
    except:
        loc_index1 = -1
        loc_index6 = -1
        loc_index5 = -1
        #loc_
        loc_index2 = -1
        loc_index3 = -1
        loc_index4 = -1

    d = np.zeros(len(__data_columns))
    
    d[0]=payloadmass
    d[1]=flights
    d[2]=Block
    d[3]=ReusedCount
    if loc_index1>=0:
        d[loc_index1]=1
    if loc_index2>=0:
        d[loc_index2]=1
    if loc_index3>=0:
        d[loc_index3]=1
    if loc_index4>=0:
        d[loc_index4]=1
    if loc_index5>=0:
        d[loc_index5]=1
    if loc_index6>=0:
        d[loc_index6]=1
    f = scaler.fit_transform([d])
    k = __model.predict(f)[0]

    if k ==1:
        return "Yes, the first stage will land sucessfully"
    else:
        return "Better luck  next time, the first stage crashed"

def get_orbit_names():
    return __orbit

def get_Gridfins():
    return __Gridfins

def get__reused():
    return __reused

def get_legs():
    return __legs
def get_landingpad():
    return __landingpad
def get_launchsite_names():
    return __launchsite


def load_saved_artificates():
    print("loading saved artifacts...start")
    global __data_columns
    global __orbit
    global __Gridfins
    global __reused
    global __legs
    global __landingpad
    global __launchsite

    with open("server/artificates/columns.json","r") as f:
        __data_columns = json.load(f)["data_columns"]
        __orbit = __data_columns[4:15]
        __Gridfins = __data_columns[15:17]
        __reused = __data_columns[17:19]
        __legs = __data_columns[19:21]
        __landingpad = __data_columns[21:26]
        __launchsite = __data_columns[26:]
    
    global __model
    if __model is None:
        with open("server/artificates/launch_prediction_model.pickle","rb") as  f:
            __model = pickle.load(f)
    print("loading saved artificates....done")
        
if __name__=="__main__":
    load_saved_artificates()
    print(get_orbit_names())
    print(get_Gridfins())
    print(get__reused())
    print(get_legs())
    print(get_landingpad())
    print(get_launchsite_names())
    print(get_launch_prediction(458754,3.0,5.0,1.0,'PO','GridFins_True', 'Reused_True', 'Legs_True',
       '5e9e3032383ecb554034e7c9','KSC LC 39A'))