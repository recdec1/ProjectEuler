#include <iostream>
#include <string>
using namespace std;

string reverseStr(string str)
{
	int len = str.length();
	string strRev;
	for (int i = len - 1; i >= 0; i--)
	{
		strRev.push_back(str[i]);
	}
	return strRev;
}

int main()
{
	int total = 0;
	int largest = 0;
	for (int i = 100; i < 1000; i++)
	{
		for (int j = 100; j < 1000; j++)
		{
			total = i * j;
			string str = to_string(total);
			string strRev = reverseStr(str);
			if (str == strRev)
			{
				if (largest < stoi(str)) {
					largest = stoi(str);
				}
				
			}
		}
	}
	cout << largest;
}
