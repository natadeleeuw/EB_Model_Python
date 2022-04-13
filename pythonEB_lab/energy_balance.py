from vapPressure import *

url = 'https://github.com/samsamsam34/EB_Models_mat/blob/758d9443d7aff14df6aa5a1db57387078188b135/matlabEB_lab/CENMET_INPUT_data.csv?raw=true'
input = pd.read_csv(url,index_col=0)
vp = vapPressure(input)
print(vp)
