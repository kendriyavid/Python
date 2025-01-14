// #include <bits/stdc++.h>
// using namespace std;

// int main() {
//     long long n, k;
//     cin >> n >> k;
    
//     vector<long long> front; // Use long long for divisors
//     vector<long long> back;
//     for (long long i = 1; i * i <= n; i++) {
//         if (n % i == 0) {
//             front.emplace_back(i); // Add the smaller divisor
//             if (i != n / i) {
//                 back.emplace_back(n / i); // Add the larger paired divisor
//             }
//         }
//     }
//     // Total number of unique divisors
//     int totalDivisors = front.size() + back.size();
//     if (k > totalDivisors) {
//         cout << -1 << endl; // Not enough divisors
//     } else if (k <= front.size()) {
//         cout << front[k - 1] << endl; // k-th divisor is in `front`
//     } else {
//         cout << back[back.size() - (k - front.size())] << endl; // Adjust index in `back`
//     }

//     return 0;
// }

// counting divisors
// #include <bits/stdc++.h>
// using namespace std;

// int main(){
//     int x;
//     cin>>x;
//     int product=1;
//     for(int i=2;i*i<=x;i++){
//         if(x%i==0){
//             int count=0;
//             while(x%i==0){
//                 x = x/i;
//                 count++;
//             }
//             product*=count+1;
//         }
//     }
//     cout<<product<<endl;
// }

// #include <bits/stdc++.h>
// using namespace std;

// int counting(int x){
//     int product = 1;

//     // Factorize x
//     for (int i = 2; i * i <= x; i++) {
//         if (x % i == 0) {
//             int count = 0;
//             while (x % i == 0) {
//                 x = x / i;
//                 count++;
//             }
//             product *= (count + 1);
//         }
//     }

//     if (x > 1) {
//         product *= 2; 
//     }

//     return product;
// }

// int main() {
//     int cases;
//     cin>>cases;
//     while(cases--){
//         int x;
//         cin >> x;
//         cout<<counting(x)<<endl;
//     }
//     return 0;
// }


// Common divisors
// #include <bits/stdc++.h>
// using namespace std;

// void factorize(map<int,int> &mp1,int n){
//     for(int i=2;i*i<=n;i++){
//         int count=0;
//         if(n%i==0){
//             while(n%i==0){
//                 count++;
//                 n/=i;
//             }
//         }
//         mp1[i]=count;
//     }
//     if(n>1){
//         mp1[n]++;
//     }
// }

// void compare(map<int,int> &mp1, map<int,int> &mp2){
//     auto mp2p = mp2.begin();
//     for(auto &mp1p:mp1){
//         mp1p.second = min(mp1p.second, mp2[mp1p.first]);
//     }
// }

// int main(){
//     int size;
//     cin>>size;
//     int n=0;
//     vector<int> numbers(size,0);
//     for(int i=0;i<size;i++){
//         cin>>numbers[i];
//         if(numbers[i]>n){
//             n=numbers[i];
//         }
//     }
//     // prime factorization
//     map<int,int> mp1;
//     factorize(mp1,n);
//     for(auto &i:numbers){
//         if(i!=n){
//             map<int,int> mp2;
//             factorize(mp2,i);
//             compare(mp1,mp2);
//         }
//     }
//     int count=1;
//     for(auto &it:mp1){
//         if(it.second!=0){
//             count*=(it.second+1);
//         }
//     }
//     cout<<count;
//     return 0;
// }


// #include <bits/stdc++.h>
// using namespace std;

// // iterative
// int gcd(int a, int b){
//     while(b!=0){
//         int temp =b;
//         b = a%b;
//         a = temp;
//     }
//     return a;
// }

// int factorize(int n){
//     int result=1;
//     for(int i=2;i*i<=n;i++){
//         if(n%i==0){
//             int count=0;
//             while(n%i==0){
//                 count++;
//                 n/=i;
//             }
//             result*=(count+1);
//         }
//     }
//     if(n>1){
//         result*=2;
//     }
//     return result;
// }


// int main(){
//     int size;
//     cin>>size;
//     vector<int> dataArr(size,0);
//     for(int i=0;i<size;i++){
//         cin>>dataArr[i];
//     }
//     int GCD=0;
//     for(auto &it:dataArr){
//         GCD = gcd(it,GCD);
//     }
//     cout<< factorize(GCD);

//     return 0;
// }


// lcm problem


// #include <bits/stdc++.h>
// using namespace std;

// int main(){
//     int cases;
//     cin>>cases;
//     while(cases--){
//         int x,y;
//         cin>>x>>y;
//         int product = 2*x;
//         if(x<=product && product<=y){
//             cout<<x<<" "<<product<<endl;
//         }
//         else{
//             cout<<-1<<endl;
//         }
//     }
//     return 0;
// }