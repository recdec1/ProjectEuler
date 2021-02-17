#include <iostream>
using namespace std;

long int fib(long int n) {
	if (n == 1 || n == 0) {
		return n;
	}
	else{ 
		return (fib(n-1) + fib(n-2));
	}
}
int main() {
	int total = 0;
	for (int i = 0; total < 4000000; i++){
		if (fib(i) % 2 == 0) {
			total += fib(i);
		}
	}
	cout << total;
}