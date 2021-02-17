#include <iostream>
using namespace std;

bool isPrime(int num)
{
	if (num < 2)
		return false;
	if (num == 2)   //only let one even number pass
		return true;
	if (!(num % 2))  //other even numbers: return false
		return false;
	//You just check for a few numbers, until i > sqrt of num
	//Ex: for 100 use just need to check ODD NUMBER less than sqrt(100) = 10
	//that is 3,5,7,9  not 100 numbers
	for (int i = 3; i <= sqrt((double)num); i += 2)
		if (!(num % i))
			return false;
	return true;

int main() {
	uint64_t number = 0;
	cout << "Find the Largest Prime Factor of What Number?"; cin >> number;
	for (int i = 1; i < number; i++)
	{
		if (number % i == 0)
		{
			number /= i;
			if (i > 1)
			{
				if (isPrime(i)) {
					cout << i << endl;
				}
			}
		}
	}
	cout << number;
}