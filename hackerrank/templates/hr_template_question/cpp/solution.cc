#include <iostream>
#include <string>

#include "solution.h"

std::string Solve(std::string input) {
    while (!input.empty() && (input.back() == '\n' || input.back() == '\r' || input.back() == ' ')) {
        input.pop_back();
    }
    std::size_t start = input.find_first_not_of(' ');
    if (start == std::string::npos) {
        return "";
    }
    return input.substr(start);
}

#ifndef ALGO_TEST
int main() {
    std::string line;
    std::getline(std::cin, line);
    std::cout << Solve(line) << std::endl;
    return 0;
}
#endif
