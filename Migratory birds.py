"""
Given an array of bird sightings where every element represents a bird type id, determine the id of the most frequently sighted type.
If more than 1 type has been spotted that maximum amount, return the smallest of their ids.
"""

def migratoryBirds(arr):
    # Write your code here
    my_dict={}
    for i in arr:
        if i not in my_dict:
            my_dict[i]=1
        else:
            my_dict[i]+=1
    my_list=list(sorted(my_dict.items(), key=lambda x:x[1]))
    max_list=[]
    max_val=my_list[len(my_list)-1][1]
    for i in my_list:
        if i[1]==max_val:
            max_list.append(i)
    max_list=sorted(max_list)
    return max_list[0][0]