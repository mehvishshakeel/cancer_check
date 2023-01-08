from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


df = pd.read_csv(r'data.csv')

print (df)

df.hist(bins=50, figsize=(15, 15))
plt.tight_layout()

#plt.show()
print ('please enter in the following details\n')


radius = input ('radius mean:')
while True:
    if (float(radius) <28.1) and (float(radius) > 6.98 ):
        break
    else:
        print("The entered value falls beyond the acceptable limits\n")
        radius = input ('Enter correct radius mean :')    


texture = input('\n texture mean: ')
while True:
    if (float(texture) <39.3) and (float(texture) > 9.71 ) :
        break
    else:
        print("The entered value falls beyond the acceptable limits\n")
        texture = input ('Enter correct texture mean :')


perimeter = input('perimeter mean: ')
while True:
    if (float(perimeter) <189) and (float(perimeter) > 43.8 ) :
        break       
    else:
        print("The entered value falls beyond the acceptable limits\n")
        perimeter = input ('Enter correct perimeter mean :')   

            
area = input('area mean: \n')
while True:
    if (float(area) <2501) and (float(area) > 144 ) :
        break
    else:
        print("The entered value falls beyond the acceptable limits\n")
        area = input ('Enter correct area mean :')
                
                
smoothness = input('smoothness mean: \n')
while True:
    if (float(smoothness) <0.16) and (float(smoothness) > 0.05 ) :
        break
    else:
        print("The entered value falls beyond the acceptable limits\n")
        smoothness = input ('Enter correct smoothness mean :')


compactness = input('compactness mean: \n')
while True:
    if (float(compactness) <0.35) and (float(compactness) > 0.02 ) :
        break
    else:
        print("The entered value falls beyond the acceptable limits\n")
        compactness = input ('Enter correct compactness mean :')

                        
concavity = input('concavity mean: \n')
while True:
    if (float(concavity) <0.43) and (float(concavity) > 0 ) :
        break
    else:
        print("The entered value falls beyond the acceptable limits\n")
        concavity = input ('Enter correct concavity mean :')


concave_points = input('concave points mean: \n')
while True:
    if (float(concave_points) <0.2) and (float(concave_points) > 0 ) :   
        break
    else:
        print("The entered value falls beyond the acceptable limits\n")
        concave_points = input ('Enter correct concave points mean :')




avg_radius = df["radius_mean"].mean()
avg_texture = df["texture_mean"].mean()
avg_perimeter = df["perimeter_mean"].mean()
avg_area = df["area_mean"].mean()
avg_smoothness = df["smoothness_mean"].mean()
avg_compactness = df["compactness_mean"].mean()
avg_concavity = df["concavity_mean"].mean()
avg_concave_points = df["concave points_mean"].mean()


avg_radius_up_bound = avg_radius + (avg_radius*.4)
avg_texture_up_bound = avg_texture 
avg_perimeter_up_bound =
avg_area_up_bound =
avg_smoothness_up_bound =
avg_compactness_up_bound =
avg_concavity_up_bound =
avg_concave_points_up_bound =

avg_radius_low_bound = avg_radius + (avg_radius*.4)
avg_texture_low_bound = avg_texture
avg_perimeter_low_bound = 
avg_area_low_bound = 
avg_smoothness_low_bound = 
avg_compactness_low_bound = 
avg_concavity_low_bound = 
avg_concave_points_low_bound = 



'''
print("avg_radius\t",avg_radius)
print("avg_texture\t",avg_texture)
print("avg_perimeter\t",avg_perimeter)
print("avg_area\t",avg_area)
print("avg_smoothness\t",avg_smoothness)
print("avg_compactness\t",avg_compactness)
print("avg_concavity\t",avg_concavity)
print("avg_concave_points\t",avg_concave_points)
'''



percentage = 0

step = 100/8

if ((radius < avg_radius_up_bound) or (radius > avg_radius_low_bound)):
    percentage += step

if ((texture < avg_texture_up_bound) or (texture > avg_texture_low_bound)):
    percentage += step


print(" based on past data we are",percentage,"%", "sure that this cancer is Malignant")


    

        
                
                    
                        

                            






