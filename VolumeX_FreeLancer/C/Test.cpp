#include <iostream>

int main() {
  std::cout << "Hello World!\nEnter Your Age: ";

  int x;
  std::cin >> x;
  if (x > 18){
    std::cout << "Hello Dude";
  } else {
    std::cout << "Hello Student";
  }
}