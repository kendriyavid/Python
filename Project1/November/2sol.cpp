// #include <bits/stdc++.h>
// using namespace std;

// int main() {
//     int size;
//     cin >> size;
//     vector<int> dataArr(size, 0);
//     for (int i = 0; i < size; i++) {
//         cin >> dataArr[i];
//     }

//     int xoring = 0;
//     for (int i = 0; i < size; i++) {
//         xoring ^= dataArr[i];
//     }

//     int nth = 0;
//     while ((xoring & 1) == 0) {
//         nth++;
//         xoring >>= 1; // Correct way to right-shift the variable
//     }

//     int mask = 1;
//     mask = mask << nth; // Correctly create the mask

//     vector<int> t1;
//     vector<int> t2;
//     for (int i = 0; i < size; i++) {
//         if ((dataArr[i] & mask) != 0) { // Check if nth bit is set
//             t1.emplace_back(dataArr[i]);
//         } else {
//             t2.emplace_back(dataArr[i]);
//         }
//     }

//     int number1 = 0;
//     int number2 = 0;
//     for (auto &i : t1) {
//         number1 ^= i;
//     }
//     for (auto &i : t2) {
//         number2 ^= i;
//     }

//     cout << number1 << " " << number2;
//     return 0;
// }



// #include <bits/stdc++.h>
// using namespace std;

// int main(){
//     int number;
//     cin>>number;
//     int position=0;
//     int power=1;
//     while(number!=0){
//         if(number&1!=1){
//             position+= 1<<(power-1);
//         }    
//         else{
//             position+= 1<<(power);
//         }
//         power++;
//         number>>=1;
//     }
//     cout<<position;
//     return 0;
// }

// #include <bits/stdc++.h>
// using namespace std;

// int main(){
//     int size;
//     cin>>size;
//     vector<int> dataArr(size,0);
//     for(int i=0;i<size;i++){
//         cin>>dataArr[i];
//     }
//     // creating dicti
//     unordered_map<int,int> ump;
//     for(auto &it:dataArr){
//         if(ump.find(it)==ump.end()){
//             ump[it]=1;
//         }
//         else{
//             ump[it]++;
//         }
//     }
//     //creating vector of 32 bits
//     vector<int> binRep(32,0);
//     int count=31;
//     for(auto it:ump){
//         if(it.second==0){
//             continue;
//         }
//         int i=31;
//         int number = it.first;
//         while(number!=0){
//             if((number&1)==1){
//             binRep[i]+=it.second;
//             }
//             number>>=1;
//             i--;
//         }
//     }
//     int number=0;
//     // parsing the binRep and turning the bit of 3n+1 on
//     for(int i=31;i>=0;i--){
//         if(binRep[i]%3==1){
//             number+=(1<<i);
//         }
//     }
//     cout<<number;
//     return 0;
// }


// #include <bits/stdc++.h>
// using namespace std;

// int main() {
//     int size;
//     cin >> size;
//     vector<int> dataArr(size, 0);
//     for (int i = 0; i < size; i++) {
//         cin >> dataArr[i];
//     }

//     // Creating a vector to store the count of bits at each position (32-bit integer)
//     vector<int> binRep(32, 0);

//     // Counting the bit occurrences for each number in dataArr
//     for (auto num : dataArr) {
//         for (int i = 31; i >= 0; i--) {
//             if (num & (1 << i)) { // Check if the ith bit is set
//                 binRep[i]++;
//             }
//         }
//     }

//     int number = 0;
//     // Constructing the unique number from the bit representation
//     for (int i = 31; i >= 0; i--) {
//         // If the bit count modulo 3 is 1, it means this bit is part of the unique number
//         if (binRep[i] % 3 == 1) {
//             number += (1 << i);
//         }
//     }

//     cout << number;
//     return 0;
// }

// power set using bitmanipulation
// #include <bits/stdc++.h>
// using namespace std;

// int main() {
//     string s;
//     getline(cin, s);
//     vector<string> result;

//     int n = s.size();
//     int totalSubsequences = (1 << n); // Total number of subsequences (2^n)

//     // Generate all subsequences
//     for (int i = 1; i < totalSubsequences; i++) {
//         string temp = "";
//         for (int j = 0; j < n; j++) {
//             // Check if the j-th bit in i is set
//             if (i & (1 << j)) {
//                 temp += s[j];
//             }
//         }
//         result.emplace_back(temp);
//     }

//     // Print all non-empty subsequences
//     for (const auto &subsequence : result) {
//         cout << subsequence << endl;
//     }

//     return 0;
// }


// #include <bits/stdc++.h>
// using namespace std;

// int main(){
//     int cases;
//     cin>>cases;
//     while(cases--){
//         int size;
//         cin>>size;
//         vector<int> dataArr(size);
//         for(int i=0;i<size;i++){
//             cin>>dataArr[i];
//         }
//         int result=dataArr[0];
//         for(int i=0;i<size;i++){
//             result&=dataArr[i];
//         }
//         cout<<result;
//     }
//     return 0;
// }



// #include <bits/stdc++.h>
// using namespace std;
// // 1 for prime and 0 for not prime
// int main(){
//     int number;
//     cin>>number;
//     vector<int> sieve(number+1,1);
//     sieve[0]=sieve[1]=0;
//     for(int i=2;i<=number;i++){
//         if(sieve[i]==1){
//         for(int j=i*i;j<=number;j+=i){
//             sieve[j]=0;
//         }}
//     }
//     return 0;
// }


// #include <bits/stdc++.h>
// using namespace std;

// int main(){
//     long long base = 8;
//     int power;
//     long long result=1;
//     cin>>power;
//     while(power>0){
//         if((power&1)==1){
//             power--;
//             result = (result*base)%10;
//         }
//         else{
//             base = (base*base)%10;
//             power/=2;
//         }
//     }
//     cout<<result;
//     return 0;
// }

// #include <bits/stdc++.h>
// using namespace std;
// const int MOD = 1e9 + 7;

// int power(int a,int n){
//     int result=1;
//     while(n!=0){
//         if(n&1==1){
//             n--;
//             result = (result%MOD * a%MOD)%MOD;
//         }
//         else{
//             n/=2;
//             a = (a%MOD * a%MOD)%MOD ;
//         }
//     }
//     return result;
// }

// int main(){
//     int cases;
//     cin>>cases;
//     while(cases--){
//         int a,b,n;
//         cin>>a>>b>>n;
//         int number =abs(a-b);
//         vector<int> divisors;
//         for(int i=1;i*i<number;i++){
//             if(number%i==0){
//                 divisors.emplace_back(i);
//                 divisors.emplace_back(number/i);
//             }
//         }
//         int n1 = (power(a,n)%MOD+power(b,n)%MOD)%MOD;
//         int maximum = INT_MIN;
//         for(int i=0;i<divisors.size();i++){
//             if(n1%divisors[i]==0){
//                 maximum = max(divisors[i],maximum);
//             }
//         }
//         cout<<maximum<<endl;
        
//     }
//     return 0;
// }
