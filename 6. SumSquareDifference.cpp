#include <iostream>
#include <math.h>

using namespace std;

int main() 
{
	int limit = 100;
	int totalSumSquare = 0;
	int totalSquareSum = 0;

	for (int i = 1; i <= limit; i++)
	{
		totalSquareSum += pow(i, 2);
		totalSumSquare += i;
	}
	totalSumSquare = pow(totalSumSquare, 2);
	cout << totalSumSquare - totalSquareSum;
}