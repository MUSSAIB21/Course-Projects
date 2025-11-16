from itertools import count

nums1=[1,1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]

nums2=[2,2,4,5,5,6,9,10]

nums3=sorted(nums1+nums2)
print(nums3)

freq=1
highest=[0,0]

for n in range(len(nums3)-1):


    if nums3[n]==nums3[n+1]:
        freq+=1
        if freq>highest[1]:
            highest[1]=freq
            highest[0]=nums3[n]
    else:
        freq=1
print(highest)



