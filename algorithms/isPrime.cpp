#include <algorithm>
#include <chrono>
#include <iostream>
#include<vector>
using namespace std;
using namespace std::chrono;

bool checkPrimeNumber(int n) {
    int i;
    bool isPrime = true;

    // 0 and 1 are not prime numbers

        for (i = 2; i <= n / 2; ++i) {
            if (n % i == 0) {
                isPrime = false;
                break;
            }
        }
        return isPrime;
    }

int main() {
    int n;

    cout << "Enter a positive  integer: ";
    cin >> n;

    auto start = high_resolution_clock::now();
    bool result = checkPrimeNumber(n);
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<nanoseconds>(stop - start);

    if (result)
        cout << "true";
    else
        cout << "false";


    cout << "\n"
         << duration.count() << " nanoseconds" << endl;

    return 0;
}
