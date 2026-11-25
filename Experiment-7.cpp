#include<iostream>
#include<list>
#include<string>

using namespace std;

void ones(list <int>& A){

    for(int &x: A){
        x = 1-x;
    }
}

void twos(list<int>& A){
    ones(A);

    auto i = A.rbegin();
    while( i !=A.rend() && *i ==1){
        *i=0;
        i++;
    }


    if(i != A.rend()){
        *i =1;
    }
}



list <int> binary(list<int> A , list<int> B){

    list<int> result;
    int carry = 0;

    while(!A.empty() || !B.empty()){
        int sum = carry;

        if(!A.empty()){
            sum += A.back();
            A.pop_back();
        }

        if(!B.empty()){
            sum += B.back();
            B.pop_back();
        }


        result.push_front(sum%2);
        carry = sum/2;


    }
    if(carry == 1){
        result.push_front(1);
    }

    return result;

    

} 
void display (list<int> A){

    for(int x : A){
        cout<<x;
    }
    cout<<endl;
}

int main(){

    list<int> A,B;
    string str1,str2;


    cout<<"enter the first binary number"<<endl;
    cin>>str1;

    cout<<"enter the second binary number"<<endl;
    cin>>str2;

    for(char x : str1){
        A.push_back(x - '0');
    }

     for(char x : str2){
        B.push_back(x - '0');
    }

    list<int> one = A;
    cout<<"ones comp : "<<endl;
    ones(one);
    display(one);


    list<int> two = A;
    cout<<"twos comp"<<endl;
    twos(two);
    display(two);

    list<int> sum = binary(A,B);
    cout<<"binary addition"<<endl;
    display(sum);
    




}