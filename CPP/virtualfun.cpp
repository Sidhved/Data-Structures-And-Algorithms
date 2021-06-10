// CPP program to illustrate 
// concept of Virtual Functions 
#include <iostream> 
using namespace std; 
class Base { 
public: 
     virtual void print()
    { 
        cout << "print base class" << endl; 
    } 
    void show() 
    { 
        cout << "show base class" << endl; 
    } 
}; 
  
class Derived : public Base { 
public: 
    void print() 
    { 
        cout << "print derived class" << endl; 
    } 
     void show() 
    { 
        cout << "show derived class" << endl; 
    } 
}; 
  
int main() 
{ 
    Base* bptr; 
    Derived d; 
    // virtual function, binded at runtime 
    bptr = &d; 
  	bptr->print(); 
    // Non-virtual function, binded at compile time 
   	bptr->show(); 
   	
}
