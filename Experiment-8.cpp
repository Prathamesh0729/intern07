#include<iostream>
#include<string>
#include<stack>

using namespace std;

string clean(string s){
    string result = "";

    for(char c : s){
        if(isalnum(c)){
            result+= c;
        }
    }
    return result;
}

bool palindrome(string s){
    stack<char> stk;

    for(char c: s){
        stk.push(c);
    }

    for(char c: s){
        if(c != stk.top()){
            return false;
        }
        stk.pop();
    }
    return true;
}


void rev(string s){
    stack<char> st;
    for(char c: s){
        st.push(c);
    }
    while(!st.empty()){
        cout<<st.top();
        st.pop();
    }
}

int main(){
    string str;

    cout<<"enter a string"<<endl;
    cin>> str;

    string cleaned;
    cleaned = clean(str);

    if(palindrome(cleaned)){
        cout<<"it is an pallindrome"<<endl;
    }
    else{
        cout<<"not an a pallindrome"<<endl;
    }

    cout<<"reverse string is : "<<endl;
    rev(cleaned);


    return 0;


}