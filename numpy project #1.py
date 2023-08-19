import numpy as np 
'''excel sheet link-https://docs.google.com/spreadsheets/d/1Gamkq8pGS1VGir9t_SL8apd7aq93-AHnshZtjvrJPT0/edit?usp=sharing
'''
'''
1. Represent the data in the given sheet into an appropriate NumPy array so
that you can perform the following actions on it.
'''

temprature=np.array([[[[14,28],[13,24],[6,28],[11,22],[13,30],[6,27],[13,23]],
                      [[10,26],[7,25],[7,22],[-13,29],[12,28],[15,33],[6,26]],
                      [[13,23],[11,32],[12,22],[6,25],[14,22],[15,29],[7,23]],
                      [[7,24],[13,29],[9,21],[13,22],[11,23],[8,21],[12,30]]],

                     [[[6,20],[14,31],[12,25],[9,31],[13,26],[14,22],[13,20]],
                      [[13,30],[9,23],[9,29],[7,30],[9,23],[8,25],[10,31]],
                      [[6,20],[7,21],[6,23],[13,25],[11,23],[9,24],[7,21]],
                      [[12,26],[13,31],[13,30],[9,29],[13,23],[12,25],[15,32]]],

                     [[[4,22],[7,21],[8,21],[2,19],[5,19],[3,3],[22,6]],
                      [[5,19],[2,18],[4,22],[8,19],[2,21],[2,3],[22,4]],
                      [[8,18],[8,22],[7,21],[6,22],[4,20],[4,4],[19,2]],
                      [[2,19],[5,21],[5,18],[7,18],[4,22],[4,6],[21,4]]],
                      
                     [[[10,21],[9,22],[-10,18],[12,19],[11,20],[11,71],[18,8]],
                      [[8,18],[11,20],[7,18],[9,22],[8,18],[7,10],[18,7]],
                      [[8,19],[9,20],[11,18],[9,20],[12,19],[12,12],[18,9]],
                      [[11,19],[9,19],[12,21],[11,21],[12,21],[10,9],[22,12]]]])					

'''
2. Write the dimensions and shape of the NumPy array that you have
created.
'''
dim=np.ndim(temprature)
print("Dimension of array:",dim)

shape=np.shape(temprature)
print("Shape of array:",shape)

'''
3. Print the daily temperatures for the first week of each month.
'''
daily_temp_1st_week=temprature[:,::4,:,:]
print("Daily temprature of 1st week:",daily_temp_1st_week)

'''
4. Print the temperatures for Tuesday of each month.
'''
tuesday_temp=temprature[:,:,1:2,:]
print("Tempratures for tuesday:",tuesday_temp)

'''
5. Print only the maximum temperature for all the weekdays of Dec and Feb.
'''

max_temp_allDays_dec_feb=temprature[1::2,:,:,1]
print("Only max. temp. of all days of dec and feb:",max_temp_allDays_dec_feb)

'''
6. Print all the days along with the week number in November when the
minimum temperature was less than 8 degrees.
'''
