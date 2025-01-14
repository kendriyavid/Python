// // seive of erethnoses
// #include <bits/stdc++.h>
// using namespace std;
// bool checkPrime(int number,vector<int> sieve){
//     return sieve[number]==1;
// }
// int main(){
//     int number;
//     cin>>number;
//     vector<int> sieve(number);
//     for(int i=0;i<number;i++){
//         sieve[i]=1;
//     }
//     sieve[0]=sieve[1] = 0;
//     for(int i=2;i<number;i++){
//         if(sieve[i]==1){
//             for(int j=i+i;j<number;j+=i){
//                 sieve[j] = 0;
//             }
//         }
//     }
//     for(int i=0;i<number;i++){
//         cout<<sieve[i];
//     }
//     cout<<endl;
//     int cases;
//     cin>>cases;
//     while(cases--){
//         int testnumber;
//         cin>>testnumber;
//         cout<<checkPrime(testnumber,sieve)<<endl;
//     }
//     return 0;
// }


// #include <bits/stdc++.h>
// using namespace std;

// int main(){
//     int number;
//     cin>>number;
//     map<int,int> mp;
//     for(int i=2;i*i<number;i++){
//         if(number%i==0){
//         int count=0;
//         while(number%i==0){
//             count++;
//             number/=i;
//         }
//         mp[i] = count;
//     }}
//     return 0;
// }

// #include <bits/stdc++.h>
// using namespace std;
// int main(){
//     int base;
//     int power;
//     cin>>base;
//     cin>>power;
//     long long result=1;
//     while(power!=0){
//         if(power%2!=0){
//             result = result*base;
//             power--;
//         }
//         else{
//             power = power/2;
//             base= base*base;
//         }
//     }
//     cout<<result<<endl;
//     cout<<INT_MAX;
//     return 0;
// }


// #include <bits/stdc++.h>
// using namespace std;

// void multiply(vector<vector<int>> &mat,vector<vector<int>>&result,int size){
//     for(int i=0;i<size;i++){
//         for(int j=0;j<size;j++){
//             result[i][j] = result[i][j]*mat[j][i];
//         }
//     }
// }
// int main(){
//     int size;
//     int power;
//     cin>>size;
//     cin>>power;
//     vector<vector<int>> mat(size,vector<int>(size));
//     for(int i=0;i<size;i++){
//         for(int j=0;j<size;j++){
//             cin>>mat[i][j];
//         }
//     }
//     vector<vector<int>> result(size,vector<int>(size));
//     for(int i=0;i<size;i++){
//         for(int j=0;j<size;j++){
//             if(i==j){
//                 result[i][j] = 1;
//             }
//             else{
//                 result[i][j] = 0;
//             }
//         }
//     }

//     for(int i=0;i<power;i++){
//         //result = result*matrix
//         multiply(mat,result,size);
//     }
    
//     for(int i=0;i<size;i++){
//         for(int j=0;j<size;j++){
//             cout<<result[i][j];
//             cout<<" ";
//         }
//         cout<<endl;
//     }
//     return 0;
// }

// #include<bits/stdc++.h>
// using namespace std;

// vector<vector<int>> multiplication(vector<vector<int>> &a,vector<vector<int>>&b){
//     int size = a.size();
//     vector<vector<int>> temp(size,vector<int>(size));
//     for(int i=0;i<size;i++){
//         for(int j=0;j<size;j++){
//             temp[i][j] += a[i][j]*b[j][i];
//         }
//     }
//     return temp;
// }

// void powxn(vector<vector<int>> &result,int power){
//     // transition matrix
//     int size = result.size();
//     vector<vector<int>> transition(size,vector<int>(size));
//     for(int i=0;i<size;i++){
//         for(int j=0;j<size;j++){
//             transition[i][j] = 1;
//         }
//     }
//     transition[0][0] = 0;
//     power--;
//     while(power!=0){
//         if(power%2!=0){
//             power--;
//             result = multiplication(result,transition);
//         }
//         else{
//             power = power/2;
//             transition = multiplication(transition,transition);
//         }
//     }
// }
// int main(){
//     int k;
//     cin>>k;
//     vector<int> fnel(k);
//     for(int i=0;i<k;i++){
//         cin>>fnel[i];
//     }
//     // matrix exponentiation part
//     int power;
//     cin>> power;
//     vector<vector<int>> result(k,vector<int>(k));
//     for(int i=0;i<k;i++){
//         for(int j=0;j<k;j++){
//             if(i==j){
//                 result[i][j]=1;
//             }
//             else{
//                 result[i][j] = 0;
//             }
//         }
//     }
//     powxn(result,power);
//     vector<vector<int>> fresult(1,vector<int>(k));
//     for(int i=0;i<1;i++){
//         for(int j=0;j<k;j++){
//             fresult[i][j]+=fnel[j]*result[j][i];
//         }
//     }

//     return 0;
// }


//  #include <bits/stdc++.h>
//  using namespace std;

//  int main(){
//     int number;
//     cin>>number;
//     map<int,int> mp;
//     for(int i=2;i*i<number;i++){
//         if(number%i==0){
//             int count=0;
//             while(number%i==0){
//                 count++;
//                 number = number/i;
//             }
//             mp[i] = count;
//         }
//     }
//     return 0;
//  }


// // gcd

// #include<bits/stdc++.h>
// using namespace std;
//  
// int main(){
    
//     int number;
//     cin>>number;
    
//     return 0;
// }

// while(b==0){
//     temp =a
//     a = b
//     b = temp%b
// }
// return a


//codechef gcd queries

// #include<bits/stdc++.h>
// using namespace std;

// int main(){
    
//     return 0;
// }


// #include <bits/stdc++.h>
// using namespace std;


// int main(){
//     int base;
//     int power;
//     cin>>base;
//     cin>>power;
//     int result=1;
//     while(power!=0){
//         if (power&1==1){
//             power--;
//             result = result*base;
//         }
//         else{
//             power = power/2;
//             base*=base;
//         }
//     }
//     cout<<result;                                              
//     return 0;
// }

// matrix exponentiation
// #include <bits/stdc++.h>
// using namespace std;

// vector<vector<int>> multiplication(vector<vector<int>> a, vector<vector<int>> b, int size){
//     vector<vector<int>> temp(size,vector<int>(size));
//     for(int i=0;i<size;i++){
//         for(int j=0;j<size;j++){
//             int total=0;
//             for(int r=0;r<size;r++){
//                 total+=a[i][j]*b[size][i];
//             }
//             temp[i][j] = total;
//         }
//     }
// }

// int main(){
//     int size;
//     cin>>size;
//     int power;
//     cin>>power;
//     vector<vector<int>> base(size,vector<int>(size));
//     for(int i=0;i<size;i++){
//         for(int j=0;j<size;j++){
//             cin>> base[i][j];
//         }
//     }
//     vector<vector<int>> result(size,vector<int>(size));
//     for(int i=0;i<size;i++){
//         for(int j=0;j<size;j++){
//             if (i==j){
//                 result[i][j] = 1;
//             }
//         }
//     }
//     while(power!=0){
//         if(power&1==1){
//             power--;
//             result = multiplication(result,base,size);
//         }
//         else{
//             power = power/2;
//             result= multiplication(base,base,size);
//         }
//     }

// }

//GCD QUERIES
// #include <bits/stdc++.h>
// using namespace std;

// int gcd(int a,int b){
//     if (b==0){
//         return a;
//     }
//     else{
//         return gcd(b,a%b);
//     }
// }

// int buildSparse(int l, int r, int level, vector<vector<int>> &st, vector<int> &dataArr) {
//     if (level == 0) {
//         st[level][l] = dataArr[l];
//         return st[level][l];
//     }
//     if (st[level][l] != -1) {
//         return st[level][l];
//     }
    
//     int size = 1 << (level - 1);
//     int one = buildSparse(l, min(l + size - 1, r), level - 1, st, dataArr);
//     int two = buildSparse(l + size, r, level - 1, st, dataArr);

//     st[level][l] = gcd(one, two);
//     return st[level][l];
// }

// int queryFunc(int l, int r, vector<vector<int>> &st) {
//     int total = 0;
//     while (l <= r) {
//         int size = log2(r - l + 1);
//         total = gcd(total, st[size][l]);
//         l += 1 << size; // Move `l` to the next segment.
//     }
//     return total;
// }

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
//         int queries;
//         cin>>queries;
//         // sparse table initialization
//         int level = log2(size);
//         vector<vector<int>> st(level,vector<int>(size,-1));
//         buildSparse(0,size-1,level,st,dataArr);
//         //query
//         while(queries--){
//             int l,r;
//             cin>>l>>r;
//             cout<<queryFunc(l,r,st);
//         }
//     }
//     return 0;
// }


#include<bits/stdc++.h>
using namespace std;

int main(){
    // int size;
    // cin>>size;
    // vector<int> vec(size);
    // for(int i=0;i<size;i++){
    //     cin>>vec[i];
    // }
    // int result=vec[0];
    // for(int i=1;i<size;i++){
    //     result =(result^vec[i]); 
    // }
    // cout<<result;
    // return  0;

    // int a=9;
    // int b = 0;
    // a = (a^b);
    // b = (b^a);
    // a = (a^b);

    // cout<<a<<" "<<b;
//     vector<int> vec(6,0);
//     vec[0] = 3;
//     vec[1] = 1;
//     vec[2] = 2;
//     vec[3] = 2;
//     vec[4] = 3;
//     vec[5] = 1;
//     int result=vec[0];
//     for(int i=1;i<6;i++){
//         result = (result^vec[i]);
//     }
//     cout<<result;
// }


