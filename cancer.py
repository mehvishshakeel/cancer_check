from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


df = pd.read_csv(r'data.csv')

print (df)

df.hist(bins=50, figsize=(15, 15))
plt.tight_layout()
plt.show()

print ('please enter in the details of ypur tumor \n')


radius = input ('radius mean:')
while True:
    if (float(radius) <28.1) and (float(radius) > 6.98 ):
        break
    else:
        radius = input ('Enter correct radius mean :')    


texture = input('\n texture mean: ')
while True:
    if (float(texture) <39.3) and (float(texture) > 9.71 ) :
        break
    else:
        texture = input ('Enter correct texture mean :')


perimeter = input('perimeter mean: ')
while True:
    if (float(perimeter) <189) and (float(perimeter) > 43.8 ) :
        break       
    else:
        perimeter = input ('Enter correct perimeter mean :')   

            
area = input('area mean: \n')
while True:
    if (float(area) <2501) and (float(area) > 144 ) :
        break
    else:
        area = input ('Enter correct area mean :')
                
                
smoothness = input('smoothness mean: \n')
while True:
    if (float(smoothness) <0.16) and (float(smoothness) > 0.05 ) :
        break
    else:
        smoothness = input ('Enter correct smoothness mean :')


compactness = input('compactness mean: \n')
while True:
    if (float(compactness) <0.35) and (float(compactness) > 0.02 ) :
        break
    else:
        compactness = input ('Enter correct compactness mean :')

                        
concavity = input('concavity mean: \n')
while True:
    if (float(concavity) <0.43) and (float(concavity) > 0 ) :
        break
    else:
        concavity = input ('Enter correct concavity mean :')


concave_points = input('concave points mean: \n')
while True:
    if (float(concave_points) <0.2) and (float(concave_points) > 0 ) :   
        break
    else:
        concave_points = input ('Enter correct concave points mean :')



    

        
                
                    
                        

                            






