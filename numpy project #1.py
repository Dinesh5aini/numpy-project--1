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

print()

'''
3. Print the daily temperatures for the first week of each month.
'''
daily_temp_1st_week=temprature[:,0,:,:]
print("Daily temprature of 1st week:",daily_temp_1st_week)

print()

'''
4. Print the temperatures for Tuesday of each month.
'''
tuesday_temp=temprature[:,:,1,:]
print("Tempratures for tuesday:",tuesday_temp)

print()

'''
5. Print only the maximum temperature for all the weekdays of Dec and Feb.
'''

max_temp_allDays_dec_feb=temprature[1::2,:,:,1]
print("Only max. temp. of all days of dec and feb:",max_temp_allDays_dec_feb)

print()

'''
6. Print all the days along with the week number in November when the
minimum temperature was less than 8 degrees.
'''

nov_min=temprature[0,:,:,0]
nov_min_lt8=np.where(nov_min<8)
print("The days along with the week number in November \nwhen the minimum temperature was less than 8 degrees:")
for day,week in np.nditer([nov_min_lt8[1],nov_min_lt8[0]]):
    if day==0:
        print(f"Monday of week ",week+1)
    elif day==1:
        print(f"Tuesday of week ",week+1)
    elif day==2:
        print(f"Wednesday of week ",week+1)
    elif day==3:
        print(f"Thursday of week ",week+1)
    elif day==4:
        print(f"Friday of week ",week+1)
    elif day==5:
        print(f"Saturday of week ",week+1)
    else :
        print(f"Sunday of week ",week+1)
    
print()

'''
7. Print all the weeks in Dec and Jan where the maximum temperature has
crossed a threshold of 20 degrees.
'''

dec_jan_max=temprature[1:3,:,:,1]
max_temp_gt20=np.where(dec_jan_max>20)
print("The weeks in Dec and Jan where the maximum\n temperature has crossed a threshold of 20 degrees:")

for month,week in np.nditer([max_temp_gt20[0],max_temp_gt20[1]]):
    if month==0:
        print(f"week {week+1} of December")
    else:
        print(f"week {week+1} of December ")

print()

'''
8. Check if there are any absurd values present in the dataset(like some temp
which should not be present in the data)
'''

absurd_values = np.where((temprature< -5) | (temprature > 50))
print("Here are indices of absurd values:",absurd_values)

print()

'''
9. What strategy would you use to handle such data points?
'''


print()

'''
10. Find and print the indexes of all the outlier(unusual) values present in
the above dataset.
'''
print("Here are indices of all outliers in array:",absurd_values)

print()

'''
11.Replace the outliers with an appropriate value.
'''

print()

'''
12. Find the average max temperature for the winter months in Jaipur.
'''
print(np.mean(temprature[:,:,:,1], axis=(1,2)))