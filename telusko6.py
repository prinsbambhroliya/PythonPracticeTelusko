
# 68.Linear search
# pos = -1
# def search(list,n):
#     i=0
#     for i in list:
#         if list[i] == n:
#             globals()['pos'] = i
#             pos = i
#             return True
#     return False

    # while i< len(list):
    #     if list[i] == n:
    #         globals()['pos'] = i
    #         pos = i
    #         return True
    #     i = i+1
    # return False

# 69.Binary Search
# pos = -1
# def search(list,n):
#     l = 0
#     u = len(list)-1 

#     while l <= u:
#         mid = (l+u)//2

#         if list[mid] == n:
#             globals()['pos'] = mid
#             return True
#         else:
#             if list[mid] < n:
#                 l = mid
#             else:
#                 u = mid
# list = [3,5,2,6,4,8,7,9]
# n = 9

# if search(list ,n):
#     print("Found at position ",pos+1)
# else:
#     print("Not Found")

# 70.Bubble Sort

# def sort(nums):
#     for i in range(len(nums)-1, 0 , -1):
#         for j in range(i):
#             if nums[j]>nums[j+1]:
#                 temp = nums[j]
#                 nums[j] = nums[j+1]
#                 nums[j+1] = temp

# nums = [5, 3, 8, 6, 7, 2]
# sort(nums)
# print(nums)

# 71.Selection sort 

def sort(nums):
    for i in range(5):
        minpos = i
        for j in range(i,6):
            if nums[j] < nums[minpos]:
                minpos = j

        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

nums = [5, 3, 8, 6, 4, 2, 9]
sort(nums)
print(nums)



