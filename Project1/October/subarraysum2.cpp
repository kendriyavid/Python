#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int length;
    cin >> length;
    vector<int> vec(length);
    
    for (int i = 0; i < length; i++) {
        cin >> vec[i];
    }
    
    vector<long long> pref(length);
    // Compute prefix sums using long long to prevent overflow
    pref[0] = vec[0];
    for (int i = 1; i < length; i++) {
        pref[i] = pref[i - 1] + vec[i];
    }
    
    unordered_map<int, int> mp;
    long long count = 0;
    mp[0] = 1; // Initialize for subarrays that are directly divisible by length
    
    for (int i = 0; i < length; i++) {
        // Calculate remainder, ensuring it's non-negative
        int remainder = ((pref[i] % length) + length) % length;
        
        // Add the count of previous occurrences of this remainder
        count += mp[remainder];
        
        // Increment the count of this remainder
        mp[remainder]++;
    }
    
    cout << count << endl;
    return 0;
}