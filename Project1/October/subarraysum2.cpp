
// #include <bits/stdc++.h>
// using namespace std;

// int main(){
//     //input
//     int number;
//     cin >> number;
//     vector<char> arr(number);
//     for (int i = 0; i < number; i++) {
//         cin >> arr[i];
//     }

//     // prefix array initialization
//     vector<int> ph(number, 0); // counts for Hoof
//     vector<int> pp(number, 0); // counts for Paper
//     vector<int> ps(number, 0); // counts for Scissors

//     if (arr[0] == 'P') {
//         pp[0] = 1;
//     } else if (arr[0] == 'S') {
//         ps[0] = 1;
//     } else if (arr[0] == 'H') {
//         ph[0] = 1;
//     }

//     for (int i = 1; i < number; i++) {
//         ph[i] = ph[i-1];
//         pp[i] = pp[i-1];
//         ps[i] = ps[i-1];
//         if (arr[i] == 'P') {
//             pp[i]++;
//         } else if (arr[i] == 'S') {
//             ps[i]++;
//         } else if (arr[i] == 'H') {
//             ph[i]++;
//         }
//     }

//     // suffix array initialization
//     vector<int> phs(number, 0); // suffix Hoof
//     vector<int> pps(number, 0); // suffix Paper
//     vector<int> pss(number, 0); // suffix Scissors

//     if (arr[number-1] == 'P') {
//         pps[number-1] = 1;
//     } else if (arr[number-1] == 'S') {
//         pss[number-1] = 1;
//     } else if (arr[number-1] == 'H') {
//         phs[number-1] = 1;
//     }

//     for (int i = number - 2; i >= 0; i--) {
//         phs[i] = phs[i+1];
//         pps[i] = pps[i+1];
//         pss[i] = pss[i+1];
//         if (arr[i] == 'P') {
//             pps[i]++;
//         } else if (arr[i] == 'S') {
//             pss[i]++;
//         } else if (arr[i] == 'H') {
//             phs[i]++;
//         }
//     }

//     // Find maximum
//     int maximum = 0;
//     for (int i = 0; i < number - 1; i++) {
//         // hoof then paper
//         maximum = max(maximum, ph[i] + pps[i+1]);
//         // hoof then scissor
//         maximum = max(maximum, ph[i] + pss[i+1]);
//         // paper then hoof
//         maximum = max(maximum, pp[i] + phs[i+1]);
//         // paper then scissor
//         maximum = max(maximum, pp[i] + pss[i+1]);
//         // scissor then hoof
//         maximum = max(maximum, ps[i] + phs[i+1]);
//         // scissor then paper
//         maximum = max(maximum, ps[i] + pps[i+1]);
//     }

//     cout << maximum << endl;
//     return 0;
// }



// #include <bits/stdc++.h>
// using namespace std;

// int main(){

//     int n;
//     int k;
//     cin>>n>>k;
//     vector<int> arr(n,0);
//     vector<int> dif(n+1,0);

//     //initializing the diff array
//     dif[0] = arr[0];
//     for (int i=1;i<n;i++){
//         dif[i] = arr[i]-arr[i-1];
//     }

//     for(int i=0; i<k; i++){
//         int l;
//         int r;
//         cin>>l>>r;
//         l--;r--;
//         dif[l]++;
//         dif[r+1]--;
//     }

//     // prefix summing
//     int total = dif[0];
//     for (int i=1; i<n;i++){
//         total+=dif[i];
//         dif[i] = total;
//     }
    
//     return 0;
// }


// #include <bits/stdc++.h>
// using namespace std;


// int goodsubarray(int length, vector<int> arr){
//     unordered_map<int,int> mp;
//     vector<int> vec(length,0);
//     vec[0] = arr[0];
//     int total = arr[0];
//     int count = 0;
//     for(int i=1; i<length; i++){
//         int diff = total- ();
//         if (diff==0){
//             count++;
//         };
//         if(mp.find(diff)!=mp.end()){
//             count+=mp[diff];
//         }
//         total+=arr[i];
//         vec[i] = total;
//         mp[vec[i]]++;
//     }    
//     return count;

// }

// int main(){

//     int cases;
//     cin>>cases;

//     for (int i=0; i<cases; i++){

//         int length;
//         cin>>length;
//         vector<int> arr(length,0);
//         string array;
//         cin>>array;
//         for (int i = 0; i < length; i++) {
//             arr[i]=(array[i] - '0'); // '0' is used to convert char to int
//         }
//         cout<<goodsubarray(length,arr)<<endl;

//     }

//     return 0;
// }


// // #include <bits/stdc++.h>
// // using namespace std;

// // int goodsubarray(int length, vector<int> &arr) {
// //     unordered_map<int, int> mp;
// //     int prefixSum = 0;
// //     int count = 0;

// //     // Initialize the map for handling subarrays starting from the 0th index
// //     mp[0] = 1;

// //     for (int i = 0; i < length; i++) {
// //         // Modify the element by subtracting 1 from each value
// //         prefixSum += arr[i] - 1;

// //         // Check if prefixSum is already present in the map
// //         if (mp.find(prefixSum) != mp.end()) {
// //             count += mp[prefixSum]; // If yes, add its frequency to the count
// //         }

// //         // Increment the frequency of the current prefixSum in the map
// //         mp[prefixSum]++;
// //     }

// //     return count;
// // }

// // int main() {
// //     int cases;
// //     cin >> cases;

// //     while (cases--) {
// //         int length;
// //         cin >> length;
// //         vector<int> arr(length, 0);
// //         string array;
// //         cin >> array;

// //         // Convert string to vector of integers
// //         for (int i = 0; i < length; i++) {
// //             arr[i] = array[i] - '0'; // '0' is used to convert char to int
// //         }

// //         // Output the result for this case
// //         cout << goodsubarray(length, arr) << endl;
// //     }

// //     return 0;
// // }



// haybale stacking


// #include <bits/stdc++.h>
// using namespace std;



// int main(){

//     int length;
//     int queries;
//     cin>>length>>queries;
//     vector<int> arr(length+1,0);
//     //query processing
//     for(int i=0; i<queries; i++){
//         int l;
//         int r;
//         cin>>l>>r;
//         arr[l]++;
//         arr[r+1]--;
//     }
//     vector<int> result(length,0);
//     result[0] = arr[0];
//     int total = result[0];
//     for(int i = 1; i<length;i++){
//         total+=arr[i-1];
//         result[i] = total;
//     }
//     sort(result);
//     cout<<result[int(length/2)];

//     return 0;
// }

// #include <bits/stdc++.h>
// using namespace std;

// int main() {
//     int length, queries;
//     cin >> length >> queries;

//     vector<int> arr(length + 2, 0);  // Length + 2 to avoid out-of-bounds for arr[r + 1]

//     // Query processing
//     for (int i = 0; i < queries; i++) {
//         int l, r;
//         cin >> l >> r;
//         arr[l]++;
//         if (r + 1 <= length) {
//             arr[r + 1]--; // Ensure we don't go out of bounds
//         }
//     }

//     vector<int> result(length, 0);
//     int total = 0;

//     // Calculate the result array using prefix sums
//     for (int i = 1; i <= length; i++) {
//         total += arr[i];
//         result[i - 1] = total; // Fill the result array
//     }

//     // Sort the result array
//     sort(result.begin(), result.end());

//     // Find the median
//     int median;
//     if (length % 2 == 1) {
//         median = result[length / 2];  // Odd case
//     } else {
//         median = (result[length / 2 - 1] + result[length / 2]) / 2; // Even case
//     }

//     cout << median << endl;

//     return 0;
// }


// // Good subarrays
// #include <bits/stdc++.h>
// using namespace std;
// int goodsubarray(vector<int> arr,int length){

//     //reducing 1
//     for(int i=0;i<length;i++){
//         arr[i]--;
//     }

//     unordered_map<int, int> mp;
//     mp[0] = arr[0];
//     //prefix
//     int count=0;
//     int total = arr[0];
//     for (int i=1;i<length;i++){
//         total+=arr[i];
//         arr[i] = total;
//         if (mp.find(total)!=mp.end()){
//             count+=mp[total];
//         }

//         mp[total]++;
//     }
//     return count;
// }   

// int main(){

//     int cases;
//     cin>>cases;
//     for (int i=0;i<cases;i++){
//         int length;
//         cin>>length;
//         vector<int> arr(length,0);
//         string number;
//         cin>>number;
//         for(int i=0;i<length;i++){
//             int num = int(number[i]-'a');
//         }
//         cout<<goodsubarray(arr,length);
//     }
    
//     return 0;
// }


// #include <bits/stdc++.h>
// using namespace std;
// int goodsubarray(vector<int>& arr, int length) {
//     // Reducing 1
//     for (int i = 0; i < length; i++) {
//         arr[i]--; 
//     }
//     unordered_map<int, int> mp;
//     mp[0] = 1; // Initialize with the prefix sum of 0
//     int count = 0;
//     int total = 0;

//     // Prefix sum calculation
//     for (int i = 0; i < length; i++) {
//         total += arr[i];

//         // Count the number of good subarrays that end at index i
//         if (mp.find(total) != mp.end()) {
//             count += mp[total]; // Add the number of times this prefix sum has been seen
//         }

//         // Update the count of the current prefix sum
//         mp[total]++;
//     }

//     return count;
// }   

// int main() {
//     int cases;
//     cin >> cases;
//     while (cases--) {
//         int length;
//         cin >> length;
//         vector<int> arr(length);

//         string number;
//         cin >> number;

//         // Populate the arr vector with the numeric values corresponding to characters
//         for (int i = 0; i < length; i++) {
//             arr[i] = int(number[i]);
//         }

//         cout << goodsubarray(arr, length) << endl;
//     }
    
//     return 0;
// }



// #include <bits/stdc++.h>
// using namespace std;

// int goodsubarray(vector<int>& arr, int length) {
//     for(int i=0;i<length;i++){
//         arr[i]--;
//     }
//     unordered_map<int, long long> mp;
//     mp[0] = 1; 
//     long long count = 0;
//     long long total = 0;
//     for (int i = 0; i < length; i++) {
//         total += arr[i];
//         count += mp[total]; 
//         mp[total]++;
//     }
//     return count;
// }   
// int main() {
//     int cases;
//     cin >> cases; 
//     while (cases--) {
//         int length;
//         cin >> length; 
//         vector<int> arr(length);
//         string number;
//         cin >> number; 
//         for (int i = 0; i < length; i++) {
//             arr[i] = number[i] - '0'; 
//         }
//         cout << goodsubarray(arr, length) << endl;
//     }
//     return 0;
// }


// #include <bits/stdc++.h>
// using namespace std;
// int main(){
//     int length;
//     cin >>length;
//     vector<int> arr;
//     for (int i=0;i<length;i++){
//         int number;
//         cin>>number;
//         arr.emplace_back(number);
//     }
//     int total = arr[0];

//     for (int i=1;i<length;i++){
//         total+=arr[i];
//         arr[i] = total;
//     }
//     int maximum=arr[1];
//     int minimum =arr[0];
//     for(int i=1;i<length;i++){
//         maximum = max(maximum,arr[i]-minimum);
//         minimum = min(minimum,arr[i]);
//     }
//     cout<<maximum;
//     return 0;
// }



#include <bits/stdc++.h>
using namespace std;

int main() {
    int length;
    cin >> length;
    vector<int> arr(length);
    for (int i = 0; i < length; i++) {
        cin >> arr[i]; 
    }
    int total = arr[0]; 
    int maximum = arr[0]; 
    int minimum = arr[0]; 
    for (int i = 1; i < length; i++) {
        total += arr[i]; 
        arr[i] = total;
        maximum = max(maximum, total - minimum);
        minimum = min(minimum, total);
    }

    cout << maximum << endl; // Output the result
    return 0;
}
