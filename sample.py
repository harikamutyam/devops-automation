def get_evendaysmilk(nums):
  sum=0
  for j in range(len(nums)):
    print(j)
    if j%2!=0:
      sum=sum+nums[j]
      
  return(sum)

def containsDuplicateNum(nums):
  for i in range(len(nums)):
    for j in range(len(nums)):
      if i!=j:
        if nums[i]==nums[j]:
          return True
  return False



#x=[44,55,6,33,60,7,23,75]
x=[5,6,7]
print(containsDuplicateNum(x))
