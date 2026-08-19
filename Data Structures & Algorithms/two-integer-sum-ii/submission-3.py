class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        Because of O(1) space, I have to work with the very own list
        keep track of the indexs. this could be used as a two pointer approach


        can iterate using a for loop

        the right track first makes sure that it is not bigger than the target
        left pointer will be all the way to the left.

            while left + right != target or right != target

            if left + right == target
                return left,right

            if left + right < target
                increase left by one
            
            else:
                break
    
        decrease right pointer
        left = 0
        

        return [0,1]
        '''

        #right pointer will be i
        
        for right in range(len(numbers)-1,-1,-1):
            left = 0
            while left < right:
                print("Left: ", left, "Right: ", right)
                if numbers[left] + numbers[right] == target:
                    return [left + 1,right +1]
                elif numbers[left] + numbers[right] < target:
                    left += 1
                else:
                    print("break")
                    break



        