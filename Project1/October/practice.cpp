// #include <iostream>
// #include <string>
// #include <vector>
// using namespace std;

// int main(){
//     pair<int,int> p = {1,3};
//     pair<int,int> x = {1,4};
//     cout << p.first<<" "<<p.second<<endl;
//     cout<< x.second<<" "<<x.first<<endl;
//     pair<int, pair<int,int>> p1 = {2,p};
//     cout<< p1.first<<" "<<p1.second.first<<endl;
//     pair <int,int> arr[3] = {{1,2},{3,4},{4,5}};
//     for (pair <int,int>i:arr){
//         cout<<i.first<<endl;
//     };

//     vector<pair<int,int>> array;
//     array.emplace_back(2,5);
//     array.emplace_back(3,4);
//     array.emplace_back(4,3);
//     for(auto it:array){
//         cout<<it.first<<endl;
//     }
//     for (vector<pair<int,int>>::iterator it = array.begin(); it!=array.end(); ++it){
//         cout<<it->first<<" "<<it->second<<endl;
//     }
//     return 0;
// }


// #include <iostream>
// #include <string>
// #include <vector>
// #include <list>
// #include <set>
// #include <stack>
// using namespace std;

// int main(){
//     pair<int,int> p = {1,2};
//     cout<<p.first<<" "<<p.second<<endl;
//     vector<pair<int,int>> vec;
//     vec.emplace_back(2,3);
//     vec.emplace_back(4,5);
//     vec.emplace_back(6,8);
//     for(auto it = vec.begin();it!=vec.end();++it){
//         cout<<it->first<<" "<<it->second<<endl;
//     };
//     list<int> ls;
//     ls.emplace_back(44);
//     ls.emplace_back(55);
//     ls.emplace_back(66);
//     cout<<ls.size()<<endl;
//     for (auto it = ls.begin();it!=ls.end();++it){
//         cout<<*(it)<<endl;
//     }

//     return 0;
// }


// #include <bits/stdc++.h>
// using namespace std;

// int victory(){
//     int l;
//     vector<int> v;
//     cin>>l;
//     int sumation = 0;
//     for (int i:v){
//         sumation = sumation+i;
//     }
//     return -sumation;
// }

// int main(){
//     int cases;
//     cin>>cases;
//     for (int i=0; i<cases;i++){
//         cout<<victory()<<endl;
//     }
//     return 0;
// }

// #include <bits/stdc++.h>
// using namespace std;

// int main(){
//     int cases;
//     cin>>cases;
//     for (int i=0; i<cases; i++){
//         cout<<func()<<endl;
//     }
//     return 0;
// }

// int func(){
//     int total;
//     vector<int,int> vec;
//     for (int i=0; i<10;i++){
//         string curr;
//         getline(curr,cin);
//         for (int j; j<10; j++){
//             if (curr[j]=="X"){
//                 vec.emplace_back(i,j);
//             }
//         }
//     }
//     for (auto& it = vec.begin(); it!=vec.end();it++){
//         if (*(it)[0]==0 || *(it)[1]==0){
//             total = total+1;
//         }
//         if (*(it)[0]==1 || *(it)[1]==1){
//             total = total+2;
//         }
//         if (*(it)[0]==2 || *(it)[1]==2){
//             total = total+3;
//         }
//         if (*(it)[0]==3 || *(it)[1]==3){
//             total = total+3;
//         }
//         if (*(it)[0]==4 || *(it)[1]==4){
//             total = total+5;
//         }
//     }
//     return total;
// }


// #include <bits/stdc++.h>
// using namespace std;

// int main(){
//     int length;
//     cin>>length;
//     vector<int> vec;
//     for (int i=0; i<length; i++){
//         int n;
//         cin>>n;
//         vec.push_back(n);
//     }
//     int minimum = numeric_limits<int>::max();
//     for(auto& i:vec){
//         if (abs(0-i)<minimum){
//             minimum = abs(0-i);
//         }
//     }
//     cout<<minimum<<endl;
//     return 0;
// }


// #include <bits/stdc++.h>
// using namespace std;

// int main(){
//     int cases;
//     cin>>cases;
//     for (int i=0;i<cases;i++){
//         vector<int> vec = function();
//         cout<<vec.size()<<endl;
//         for (int i:vec){
//             cout<<i<<" ";
//         }
//     }
//     return 0;
// }

// vector<int> function(){
//     int size;
//     cin>>size;
//     vector<int> temp;
//     vector<int> input;
//     for (int i = 0; i<size; i++){
//         int j;
//         cin>>j;
//         input.push_back(j);
//     }
//     temp.push_back(input[0]);
//     for (int i = 1; i<size; i++){
//         if (temp[i-1]>temp[i]){
//             temp.push_back(i);
//         }
//         temp.push_back(i);
//     }
//     return 
// }

// #include <bits/stdc++.h>
// using namespace std;

// vector<int> func() {
//     int size;
//     cin >> size;
//     vector<int> temp;
//     vector<int> input(size);

//     // Reading the input
//     for (int i = 0; i < size; i++) {
//         cin >> input[i];
//     }

//     // Always push the first element
//     temp.push_back(input[0]);

//     // Compare with the previous element and add to temp accordingly
//     for (int i = 1; i < size; i++) {
//         if (input[i] < input[i-1]) { // Compare with the last element in temp
//             temp.push_back(input[i]);
//         } 
//         temp.push_back(input[i]);
//     }

//     return temp; // Return the result vector
// }

// int main() {
//     int cases;
//     cin >> cases;

//     for (int i = 0; i < cases; i++) {
//         vector<int> vec = func();

//         // Output size of the vector
//         cout << vec.size() << endl;

//         // Output vector elements
//         for (int i : vec) {
//             cout << i << " ";
//         }
//         cout << endl; // Ensure new line after each case output
//     }

//     return 0;
// }


// #include <bits/stdc++.h>
// using namespace std;

// int queries(int l,int r,vector<int> prefix){
//     int result = prefix[r];
//     if (l>0){
//         result-=prefix[l-1];
//     }
//     return result;
// }


// int main(){
//     // Declare a single vector, not an array of vectors
//     vector<int> arr;
//     arr.emplace_back(1);
//     arr.emplace_back(2);
//     arr.emplace_back(3);
//     arr.emplace_back(4);
//     arr.emplace_back(5);
//     arr.emplace_back(6);
//     arr.emplace_back(7);
//     vector<int> prefix;
//     int sum = 0;
//     for(int i : arr) {
//         sum += i;
//         prefix.emplace_back(sum);
//     }
//     cout<<queries(2,4,prefix)<<endl;
//     return 0;
// }


// Breed Counting

// #include <bits/stdc++.h>
// using namespace std;

// int main(){
//     int number;
//     int queries;
//     cin>>number>>queries;
//     vector<int> arr;
//     for(int i=0; i<number; i++){
//         int cow;
//         cin>>cow;
//         arr.emplace_back(cow);
//     }
//     //precomputation
//     vector<pair<int,pair<int,int>>> pref (number,{0,{0,0}}) ;

//     if (arr[0] == 1) {
//         pref[0].first = 1;
//     } else if (arr[0] == 2) {
//         pref[0].second.first = 1;
//     } else if (arr[0] == 3) {
//         pref[0].second.second = 1;
//     }

//     for(int i=1; i<arr.size(); i++){
//         pref[i] = pref[i-1];
//         if (arr[i]==1){
//             pref[i].first+=1;
//         }
//         else if(arr[i]==2){
//             pref[i].second.first+=1;
//         }
//         else if(arr[i]==3){
//             pref[i].second.second+=1;
//         }
//     }

//     //query processing
//     for(int i=0; i<queries; i++){
//         int l;
//         int r;
//         cin>>l>>r;
//         int r1=0;
//         int r2=0;
//         int r3=0;
//         r1 = pref[r].first;
//         r2 = pref[r].second.first;
//         r3 = pref[r].second.first;
//         if (l-1>=0){
//             r1-=pref[l].first;
//             r2-=pref[l].second.first;
//             r3-=pref[l].second.second;
//         }
//         cout<<r1<<' '<<r2<<" "<<r3<<endl;
//     }
//     return 0;
// }


// // Subsequences Summing to Sevens

// #include<bits/stdc++.h>
// using namespace std;

// int main(){
//     //input
//     int length;
//     cin>>length;
//     vector<int> arr;
//     for(int i=0; i<length; i++){
//         int num;
//         cin>>num;
//         arr.emplace_back(num);
//     }
//     // prefix sum
//     vector<int> pref(length,0);
//     pref[0] = arr[0];
//     int total = pref[0];
//     for(int i=1;i<length; i++){
//         total+=arr[i];
//         pref[i] = total;
//     }
//     unordered_set<int> seti;
//     int maxlen=0;
//     for(int i=1; i<length; i++){
//         seti.insert(pref[i-1]);
//         int remainder = pref[i]%7;
//         if (seti.find(remainder)!=seti.end()){
//             int j=0;
//             while (i>j){
//                 if (pref[j]==remainder){
//                     break;
//                 }
//                 j++;
//             }
//             if (maxlen<i-j){
//                 maxlen = i-j;
//             }
//         }
//     }
//     cout<<maxlen<<endl;
//     return 0;
// }


// #include <bits/stdc++.h>
// using namespace std;

// int main() {
//     // Input
//     int length;
//     cin >> length;
//     vector<int> arr(length);
//     for (int i = 0; i < length; i++) {
//         cin >> arr[i];
//     }

//     // Prefix sum and mapping
//     unordered_map<int, int> modIndex; // stores first occurrence of each modulo
//     modIndex[0] = -1; // To handle the case where prefix sum itself is directly divisible by 7
//     int total = 0;
//     int maxLen = 0;

//     for (int i = 0; i < length; i++) {
//         total += arr[i];
//         int remainder = total % 7;

//         // If this remainder has been seen before
//         if (modIndex.find(remainder) != modIndex.end()) {
//             // Calculate the length of the subsequence
//             int len = i - modIndex[remainder];
//             maxLen = max(maxLen, len);
//         } else {
//             // Store the first occurrence of this remainder
//             modIndex[remainder] = i;
//         }
//     }

//     cout << maxLen << endl;
//     return 0;
// }


// #include <bits/stdc++.h>
// using namespace std;

// int main(){
    
//     int length;
//     cin>>length;
//     vector<char> arr;
//     int ts=0;
//     int th=0;
//     int tp=0;
//     for(int i=0;i<length;i++){
//         char c;
//         if (c=='P'){
//             tp++;
//         }
//         else if (c=="H"){
//             th++;
//         }
//         else if (c=="S"){
//             ts++;
//         }
//         cin>>c;
//         arr.emplace_back(c);
//     }

//     int gameswon=0;
//     bool flag=false;
//     char action=max(ts,th,tp);
//     for(int i=0; i<length; i++){

//     }

//     return 0;
// }


// #include <bits/stdc++.h>
// using namespace std;

// int main(){

//     int length;
//     int target;
//     cin>>length>>target;
//     vector<int> vec(length,0);
//     for (int i=0; i<length; i++){
//         int num;
//         cin>>num;
//         vec[i] = num;
//     }
//     vector<int> pref(length,0);
//     pref[0] = vec[0];
//     int total=pref[0];
//     for(int i=1; i<length; i++){
//         total+=vec[i];
//     }
//     int count=0;
//     unordered_set<int> seti;
//     seti.insert(0);
//     for(int i=0; i<length; i++){
//         int diff = target-pref[i];
//         if (seti.find(diff)!=seti.end()){
//             count+=1;
//         }
//         seti.insert(pref[i]);
//     }
//     cout<<count;
//     return 0;
// }


