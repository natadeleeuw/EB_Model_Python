import pandas as pd
import numpy as np
import math


def vapPressure(df): #Takes pandas dataframe as argument
  inMet = df #Rename dataframe

  esat = np.empty(len(inMet.index)) #Create empty numpy array

  for i in range(len(inMet.index): #Calculate vapor pressure in mb
    esat[i] = round(6.11*(math.exp((17.3*inMet.iloc[i]['T_C'])/(inMet.iloc[i]['T_C']+237.3))),2)
    #this formula is from Dingman, Appendix D, formula D-7. The output is in mb
  
  inMet['esat'] = esat.tolist() #Add to array
  
  #Convert the saturation vapor pressure to vapor pressure using relative humidity
  
  inMet['ea'] = inMet['esat']*inMet[' RH']
  
  #Take the difference between the ea and esat for use in the latent heat calculations 
  inMet['vpdiff'] = inMet['ea']-inMet['esat'] #Save to newcolum in df

  return inMet #Return updated dataframe






