//  Index  0  1  2    3   4   5  6    7   8   9
//        [0, 1, 21, 33, 45, 45, 61, 71, 72, 73] //looking for number 33
//         L              M                    R
     
            
// M = Middle number or middle pointer
           
// M = Sum of the index L + R / 2 = Average
// M = (0 + 9) / 2 = 4.5
// M = Round down = 4
    
    
// IS 45 Which is the middle number greater than 33? No so element all those numbers

//      [0, 1, 21, 33, 45, 45, 61, 71, 72, 73] //looking for number 33
//       L              M                   R
      

// //Code walkthrough 
// //Soliving in python 
// def binarySearch(array, target):
// return binarySearchHelper(array, target, 0, array - 1)


// def binarySearchHelper(array, target, left, right):



// Given a m x n matrix grid which is sorted in non - increasing order both row - wise and column - wise,
//  return the number of negative numbers in grid.


// Example 1:

// Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
// Output: 8
// Explanation: There are 8 negatives number in the matrix.
// Example 2:

// Input: grid = [[3,2],[1,0]]
// Output: 0
// Example 3:

// Input: grid = [[1,-1],[-1,-1]]
// Output: 3