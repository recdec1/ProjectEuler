#include <iostream>
using namespace std;


int main() {
	int total = 0;
	int num = 0;
	cout << "Upper number limit?" << endl; cin >> num;
	for (int i = 0; i < num; i++)
	{
		if ((i % 5 == 0) || (i % 3 == 0))
		{
			total += i;
		}
	}
	cout << total;
}