#include <algorithm>
#include <cassert>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <vector>

constexpr const char* INPUT_FILE = "input.txt";
using value_type = int;

ulong distance(std::vector<value_type>& first, std::vector<value_type>& second) {
    assert(first.size() == second.size());
    ulong sum = 0;

    for (size_t i = 0; i < first.size(); ++i) {
        sum += abs(first[i] - second[i]);
    }

    return sum;
}

void load_input(std::vector<value_type>& first, std::vector<value_type>& second) {
    std::ifstream file(INPUT_FILE); // Open file for reading
    value_type num1, num2;

    while (file >> num1 >> num2) {
        first.push_back(num1);
        second.push_back(num2);
    }
    file.close();
}

int main() {
    std::vector<value_type> first { };
    std::vector<value_type> second { };

    // std::cerr << "loading input" << std::endl;
    load_input(first, second);
    // std::cerr << "input loaded" << std::endl;

    std::sort(first.begin(), first.end());
    std::sort(second.begin(), second.end());


    std::cout << distance(first, second) << std::endl;
}
