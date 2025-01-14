// #include <iostream>
// #include <unordered_map>
// #include <vector>

// using namespace std;

// int main() {
//     int n, k;
//     cin >> n >> k;
//     vector<int> arr(n);

//     for (int i = 0; i < n; ++i) {
//         cin >> arr[i];
//     }

//     unordered_map<int, int> freq;  // To store the frequency of elements in the current window
//     int left = 0;                  // Left pointer of the window
//     long long result = 0;          // To store the number of valid subarrays
//     int distinct_count = 0;        // Count of distinct elements in the window

//     // Iterate over the array using the right pointer
//     for (int right = 0; right < n; ++right) {
//         int current = arr[right];
        
//         // Add the current element to the window
//         if (freq[current] == 0) {
//             distinct_count++;  // We have a new distinct element
//         }
//         freq[current]++;

//         // Shrink the window from the left if the number of distinct elements exceeds k
//         while (distinct_count > k) {
//             int left_elem = arr[left];
//             freq[left_elem]--;
//             if (freq[left_elem] == 0) {
//                 distinct_count--;  // One distinct element is removed from the window
//             }
//             left++;  // Move the left pointer to shrink the window
//         }

//         // The number of valid subarrays ending at 'right' is (right - left + 1)
//         result += (right - left + 1);
//     }

//     cout << result << endl;

//     return 0;
// }
// #include <bits/stdc++.h>
// using namespace std;

// int main() {
//     int tests;
//     cin >> tests;
//     while (tests--) {  // moved tests-- to while condition
//         int n, k;
//         cin >> n >> k;
//         vector<int> arr(n);
//         int minimum = INT_MAX;
        
//         for (int i = 0; i < n; i++) {
//             cin >> arr[i];
//             int remainder = arr[i] % k;
//             if (remainder > 0) {
//                 minimum = min(minimum, k - remainder);  // calculate steps needed to reach next multiple
//             } else {
//                 minimum = 0;  // if already divisible by k
//             }
//         }
        
//         cout << (minimum == INT_MAX ? 0 : minimum) << endl;
//     }
//     return 0;
// }


// #include <bits/stdc++.h>
// using namespace std;

// int main(){
//     int cases;
//     cin>>cases;
//     while(cases--){
//         int n,p;
//         cin>>n>>p;
//         vector<int> tn(n,0);
//         vector<int> cost(n,0);
//         for(int i=0;i<n;i++){
//             cin>>tn[i];
//         }
//         for(int i=0;i<n;i++){
//             cin>>cost[i];
//         }
//         vector<pair<int,int>> combined(n,{0,0});
//         for(int i=0;i<n;i++){
//             combined[i].first = cost[i];
//             combined[i].second = tn[i];
//         }
//         sort(combined.begin(),combined.end());
//         int i=0;
//         int j=0;
//         int cost = combined[1].first;
//         while(j<n){
//             if(combined[i].first<p){
//                 while(combined[i].second--){
//                     cost=cost+combined[j].first;
//                     j++;
//                 }
//                 i++;
//             }
//             else{
//                 cost+=combined[i].first;
//                 j++
//             }
//         }
//         cout<<cost;
//     }


//     return 0;
// }


// #include <bits/stdc++.h>
// using namespace std;

// int main(){
//     int cases;
//     cin >> cases;
//     while (cases--) {
//         int n, p;
//         cin >> n >> p;

//         vector<int> tn(n, 0);   
//         vector<int> cost(n, 0); 

//         for (int i = 0; i < n; i++) {
//             cin >> tn[i];
//         }

//         for (int i = 0; i < n; i++) {
//             cin >> cost[i];
//         }

//         vector<pair<int, int>> combined(n, {0, 0});
//         for (int i = 0; i < n; i++) {
//             combined[i].first = cost[i];
//             combined[i].second = tn[i];  
//         }
//         sort(combined.begin(), combined.end());
//         int total_cost = 0; 
//         int i = 0;
//         int j = 0;

//         while (j < n) {
//             if (combined[i].first < p) {
//                 while (combined[i].second-- && j < n) {
//                     total_cost += combined[j].first;
//                     j++;
//                 }
//                 i++;
//             } else {
//                 total_cost += combined[i].first;
//                 j++;
//             }
//         }

//         cout << total_cost << endl;
//     }

//     return 0;
// }


// #include <bits/stdc++.h>
// using namespace std;
// int main(){

//     int cases;
//     cin>>cases;
//     while(cases--){
//         int n;
//         cin>>n;
//         vector<int> vec(n,0);
//         for(int i=0;i<n;i++){
//             cin>>vec[i];
//         }
//         if(n%2==0){
//             cout<<2<<endl;
//             cout<<1<<" "<<n<<endl;
//             cout<<1<<" "<<n<<endl;
//         }
//         else{
//             cout<<4<<endl;
//             cout<<1<<" "<<n-1<<endl;
//             cout<<n-1<<" "<<n<<endl;
//         }
//     }
//     return 0;
// }


// #include <bits/stdc++.h>
// using namespace std;

// bool func(int mid, unordered_map<int, int> mp){
//     if(mp.size()<mid){
//         return false;
//         }
//     for(auto &it:mp){
//         if (it.second>mid){
//             return true;
//         }
//     }
//     return false;
// }

// int main(){
//     int cases;
//     cin>>cases;
//     while(cases--){
//         int n;
//         cin>>n;
//         vector<int> vec(n,0);
//         for(int i=0; i<n;i++){
//             cin>>vec[i];
//         }
//         unordered_map<int, int> mp;
//         for(int i=0;i<n;i++){
//             if (mp.find(vec[i])!=mp.end()){
//                 mp[vec[i]]++;
//             }
//             else{
//                 mp[vec[i]]=1;
//             }
//         }
//         // binary searching
//         int result=0;
//         int i = 1;
//         int j = n/2;
//         while(i<=j){
//             int mid = (i+j)/2;
//             if(func(mid,mp)){
//                 result = mid;
//                 i++;
//             }
//             else{
//                 j--;
//             }
//         }
//         cout<<result;
//     }
//     return 0;
// }



// #include <bits/stdc++.h>
// using namespace std;

// int main(){
//     int x;
//     cin>>x;

//     bool flag = ;
//     for(int i=2;i<x;i++){
//         if(x%i==0){
//             flag = false;
//         }
//     }
//     cout<<flag;
//     return 0;
// }


//seive of erethnoses

// #include <bits/stdc++.h>
// using namespace std;

// int main(){
//     int cases;
//     cin>>cases;
//     while(cases--){
//         int n,l,r;
//         cin>>n,l,r;
//         vector<int> arr(n,0);
//         for(int i=0;i<n;i++){
//             cin>>arr[i];
//         }
//         int count=0;
//         for(int i=0;i<n;i++){
//             int num = arr[i];
//             for(int j = arr[i];i<=r;i++){
//                 if(j%arr[i]==0){
//                     count++;
//                 }
//             }
//         }
//         cout<<count;
//     }
//     return 0;
// }


// #include <bits/stdc++.h>
// using namespace std;

// int main() {
//     int cases;
//     cin >> cases;
//     while (cases--) {
//         int n, l, r;
//         cin >> n >> l >> r;
//         vector<int> arr(n);
//         for (int i = 0; i < n; i++) {
//             cin >> arr[i];
//         }

//         unordered_set<int> seti;
//         for (int i = 0; i < n; i++) {
//             int num = arr[i];

//             // Start at the smallest multiple of `num` >= `l`
//             int start = (l + num - 1) / num * num;

//             // Insert multiples of `num` between `l` and `r` into the set
//             for (int j = start; j <= r; j += num) {
//                 seti.insert(j);
//             }
//         }

//         // Output the size of the set, which represents the unique count
//         cout << seti.size() << endl;
//     }
//     return 0;
// }



// binary exponentiation
// #include <bits/stdc++.h>
// using namespace std;
// int main(){
//     int num;
//     cin>>num;
//     int pow;
//     cin>>pow;
//     int result=1;
//     while(pow!=0){
//         if(pow%2!=0){
//             result = result*num;
//             pow--;
//         }else{
//             pow = pow/2;
//             num = num*num;
//         }
//     }
//     cout<<result;
//     return 0;
// }

// #include <bits/stdc++.h>
// using namespace std;

// bool primeChecker(int num){
//     for(int i=2;i*i<=num;i++){
//         if(num%i==0){
//             return false;
//         }
//         return true;
//     }
// }

// int main(){
//     int num;
//     cin>>num;
//     int c1,c2;
//     if(num%2==0){
//         c1 = num/2;
//         c2 =num/2;
//         if(primeChecker(c1)){
//             c1++;
//             c2--;
//         }
//     }else{
//         num--;
//         c1 = num/2;
//         c2 = num/2;
//          if(primeChecker(c1)){
//             c1++;
//             c2--;
//         }
//         c1++;
//     }
//     return 0;
// }



#include <bits/stdc++.h>
using namespace std;

void rec(vector<string>& result, string mid, int pointer, const string& in) {
    if (pointer == in.size()) {
        result.emplace_back(mid);
        return;
    }
    // Taking the current character
    mid += in[pointer];
    rec(result, mid, pointer + 1, in);  // Move to the next character

    // Removing the last character to backtrack
    mid.pop_back();
    rec(result, mid, pointer + 1, in);  // Move to the next character
}

int main() {
    vector<string> result;
    string input;
    getline(cin, input);
    rec(result, "", 0, input);

    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << endl;  // Print each result on a new line
    }
    return 0;
}
