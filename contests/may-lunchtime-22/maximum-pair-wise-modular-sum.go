// Maximum Pairwise Modular Sum Problem Code: MXMODSUM
// Add problem to Todo list
// You are given an array A containing N integers, and a positive integer M. Find the maximum value of
// Ai+Aj+((Ai−Aj)modM)
// across all pairs 1≤i,j≤N.

// Note that xmodM refers to the smallest non-negative integer obtained as the remainder upon dividing x by M. For example, 4mod3=1 and (−10)mod3=2.

// Input Format
// The first line of input will contain a single integer T, the number of test cases. The description of test cases follows.
// Each test case consists of two lines of input.
// The first line of each test case contains two space-separated integers N and M.
// The second line of each test case contains N space-separated integers A1,A2,…,AN.
// Output Format
// For each test case, output on a new line the maximum value of Ai+Aj+((Ai−Aj)modM).
// Constraints
// 1≤T≤100
// 2≤N≤2⋅105
// 2≤M≤5⋅108
// 0≤Ai≤5⋅108
// The sum of N across all test cases won't exceed 2⋅105.
// Subtasks
// Subtask 1 (10 points):
// The sum of N across all test cases won't exceed 1000
// Subtask 2 (20 points):
// 2≤M≤1000
// Subtask 3 (70 points):
// Original constraints
// Sample Input 1 
// 4
// 2 18
// 12 1
// 3 5
// 4 5 6
// 5 4
// 79 29 80 58 80
// 3 20
// 33 46 56
// Sample Output 1 
// 24
// 15
// 162
// 112
// Explanation
// Test case 1: There are 4 possible pairs of indices to choose from. Their respective values are:

// i=1,j=1, giving 12+12+((12−12)mod18)=24+0=24
// i=1,j=2, giving 12+1+((12−1)mod18)=13+11=24
// i=2,j=1, giving 1+12+((1−12)mod18)=13+7=20
// i=2,j=2, giving 1+1+((1−1)mod18)=2+0=2
// Of these, the largest value is 24.

// Test case 2: There are 3×3=9 choices for pairs (i,j). Of these, one way to achieve the maximum is by choosing i=2,j=3, giving 5+6+((5−6)mod5)=11+4=15.

// Test case 3: Picking i=1,j=3 gives a value of 79+80+((79−80)mod4)=159+3=162, which is the largest possible.

// Test case 4: Picking i=3,j=2 gives a value of 56+46+((56−46)mod20)=102+10=112, which is the largest possible.





// --------------------------------------------------------------------------------------------------------------------------

package main

import (
	"fmt"
	"bufio"
	"strings"
	"strconv"
	"os"
)

func myans(a int, b int, m int) int {
	ta := a
	tb := b
	if tb < ta {
		tmp := ta
		ta = tb
		tb = tmp		
	}

	ans := ta + tb + ( ( ta - tb ) % m + m ) % m

	ans1 := tb + ta + ( ( tb - ta ) % m + m ) % m
	
	if ans > ans1 {
		return ans
	}

	return ans1 		
}

func max(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	var (
		t int
	)	

	reader := bufio.NewReader(os.Stdin)
	fmt.Scanf("%d\n", &t)
	
	for t > 0 {
		t--
                
		text, _ := reader.ReadString('\n')
		ninps := strings.Fields(text)
		n, _ := strconv.Atoi(ninps[0])
		m, _ := strconv.Atoi(ninps[1])

		x := make([]int, n)

		a := -1
		text, _ = reader.ReadString('\n')
		ninps = strings.Fields(text)	
		for i, val := range ninps {
			x[i], _ = strconv.Atoi(val)
			if x[i] > a {
				a = x[i]
			}
		}
		/*
		b := -1
		for _, val := range x {
			if val < a && val > b {
				b = val
			}
		}

		if b < a {
			tmp := a
			a = b
			b = tmp		
		}

		if a * b < 0 {
			a = b
		}*/

		ans := -1
		for i := 0; i < n; i++ {
			tmp := myans( a, x[i], m )
			ans = max(ans, tmp)
		}
		
		fmt.Println(ans)
	}	
}