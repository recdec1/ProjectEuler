#include <iostream>
using namespace std;

int main()
{
	int number = 2520;
	int i = 1;
	while (i < 21)
	{
		if (i == 20 && (number % i == 0))
		{
			cout << number;
			return 0;
		}
		else if (number % i == 0)
		{
			i++;
		}
		else
		{
			number += 2520;
			i = 1;
		}
	}
}