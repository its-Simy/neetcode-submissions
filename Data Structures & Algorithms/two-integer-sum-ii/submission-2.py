class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #must sum up a specific number
        #must not create any extra space
        #returns list


        #constraints
        #movement, can easily be done in a O(n^2), using a nested for loop
        #both answers can't be the same( 3+3, woudlnt be allowed), also cannot use the same element twice.
        

        #since its in order, I would think to start  from the back,
        #one pointer making sure that its not bigger than the target

        ans1 = 0
        ans2 = 0
        for i in range(len(numbers)-1, -1,-1):
            pointer = 0
            if numbers[i] >= target:
                i -= 1
            while numbers[pointer] + numbers[i] < target:
                pointer += 1

            if numbers[pointer] + numbers[i] == target and numbers[pointer] != numbers[i]:
                ans1 = pointer + 1
                ans2 = i + 1
                if ans1 > ans2:
                    return[ans2,ans1]
                
                break

    
        return [ans1,ans2]