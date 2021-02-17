#include <iostream>
#include <math.h>

using namespace std;

void pythagoreanTriplet(int n)
{
	for (int a = 1; a < n; a++)
	{
		for (int b = 1; b < a; b++)
		{
			float c = sqrt(pow(a, 2) + pow(b, 2));
			if (fmod(c, 1) == 0 && a + b + c == 1000)
			{
				int answer = a * b * c; // the answer was given as a * e expression so it is converted into an integer
				cout << answer << endl;
			}
		}
	}
}

int main()
{
	pythagoreanTriplet(500);
}