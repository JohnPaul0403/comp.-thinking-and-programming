def bubble_sort(nums) :
    while True:
        n1 = 0
        n2 = 1
        n = 0
        for i in range(len(nums)):
            if (nums[n1] > nums[n2]):
                temp = nums[n1]
                nums[n1] = nums[n2]
                nums[n2] = temp
                n += 1
            
            n1 += 1
            n2 += 1

        if n == 0 : break

    return nums


