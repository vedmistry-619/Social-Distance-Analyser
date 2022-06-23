import operator
Faults = ['Temperature engine hot','There is water seepage on the bottom of the car','Car suddenly dead','Less water reservoir',
            'Water reservoir exceed the limit','Swing wheel','Engine temperature cold','Light off','Brake not grip','There is brake fluid seepage',
            'Horn not sound','Hard to stomp the clutch','Gear difficulty to enter','Difficult to starter','Engine sometime turn off',
            'Difficult to starter','Engine difficult to turn on','Vehicle difficult to turn','Wasteful fuel consumption','Black smoke',
            'Car engine dies','Sound of metal clashing','Oil indicator lights up','There is oil seepage under the vehicle','Tickling sound while running car',
            'Whoosh sound','Unusual sound like a buzzing sound','Screeching sound','Heavy steering wheel','Steering wheel is not normal,sometimes shake or weight',
            'Rumbling sound','Sounds like brake squeal','Brakes do not grip']
print("Select the problems you are facing right now")
for i in range(0,len(Faults)):
    print("{} : {}".format(i,Faults[i]))
input_string = input('Enter ids of problems separated by space\n')
errlst = input_string.split()
for i in range(len(errlst)):
    errlst[i] = int(errlst[i])

errs = {}
errs["Radiator"] = [0,1,2]
errs["Radiator Tube"] = [0,1,2]
errs["Radiator lid"] = [1,3]
errs["Radiator fan"] = [1,4]
errs["Tie rod"] = [1,5]
errs["Thermostat"] = [6,18]
errs["Light"] = [7]
errs["Break Master"] = [8,9]
errs["Horn"] = [10]
errs["Brake Booster"] = [8]
errs["Clutch"] = [11]
errs["Clutch Master"] = [8,12]
errs["Battery (ACCU)"] = [14,15]
errs["Fuel Pump"] = [13,14]
errs["Depeleted Gas"] = [13,20]
errs["Magneto-Ignition Broken"] = [16]
errs["Damaged Coil"] = [17,18,28]
errs["Injector or Carburator"] = [17,18,19,28]
errs["Throtle Body"] = [17,18,19,20,28]
errs["Oil Leaks"] = [21,22,23]
errs["Engine Knocking"] = [24]
errs["Broken Car Axle"] = [25]
errs["Clutch Bearings"] = [12]
errs["Car Tansmission Problem"] = [12,21,26]
errs["Fan Belt"] = [17,27,28]
errs["Bearing"] = [29,30]
errs["Burshing Stabilizer"] = [27,29]
errs["Shock Breaker"] = [29,30]
errs["Plug"] = [18,19,20]
errs["Power Steering"] = [27,29]
errs["Velg"] = [29]
errs["Damaged Brake Shoes"] = [31,32]
def sort_dict_by_value(d, reverse = False):
  return dict(sorted(d.items(), key = lambda x: x[1], reverse = reverse))
threshold = 0.4
Valcal = {}
#tr = [1,2,5]
import numpy as np
def getMatches(a, b):
    matches = []
    unique_a = np.unique(a)
    unique_b = np.unique(b)
    for a in unique_a:
        for b in unique_b:
            if a == b:
                matches.append(a)
    return matches
#print(getMatches(tr,[1,2,4]))
for key in errs:
    #print(getMatches(tr,errs[key]))
    #print(len(errs[key]))
    #print(len(getMatches(tr,errs[key]))/len(errs[key]))
    temp=0
    if ((len(getMatches(errlst,errs[key]))/len(errs[key]))>=threshold):
            temp = len(getMatches(errlst,errs[key]))/len(errs[key])
            print(temp)
            Valcal[key] = temp
nd = sort_dict_by_value(Valcal, True)
print(list(nd.keys()))