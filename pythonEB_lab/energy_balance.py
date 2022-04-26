from vapPressure import *
from advectedheat import *
from longwave import *
from shortwave import *
from latentheat import *
from sensibleheat import *
from melt import *

#Define constants

RHOw  = 1000 # kg/m^3, Standard density of water
Cw = 4.1876e3 #J/ kg*K, Specific heat of water at Tr


# Latent heat of vaporization
L_v = 2.499e6 # J/kg
# Latent heat of sublimation
L_sub = 2.835e6 # J/kg
# Standard density of air
rho = 1.29 # kg/m^3
# Total atmospheric pressure assumed
Pa = 100000 # Pa
# Vapor pressure difference
# Note that this value will be calculated in a different script and will need to be called beforehand for this to work.
#vp_diff = ea - esat

# VonKarmon's constant
k = 0.4
# The height of the measured windspeed above the snowpack. 
z = 2
# Aerodynamic roughness in m
z0 = 0.003

# Calculate bulk transfer coefficient for vapor exchange
Ce = k**2 *log(z/z0)**-2


url = 'https://github.com/samsamsam34/EB_Models_mat/blob/758d9443d7aff14df6aa5a1db57387078188b135/matlabEB_lab/CENMET_INPUT_data.csv?raw=true'
input = pd.read_csv(url,index_col=0)


vp = vapPressure(input)

adv = advectedheat(vp, RHOw, Cw)


long = longwave(adv)

short = shortwave(long)

lh = latentheat(short, rho, L_v, L_sub, Pa, Ce)

sh = sensibleheat(lh)

melt = melt(sh)


print(list(melt.columns))

final = melt

final['sum'] = melt['Qsw'] + melt['Qlw'] + melt['Qh'] + melt['Qe'] + melt['Qr'] + melt['Qmelt']

#final = final.reset_index()

print(final)
