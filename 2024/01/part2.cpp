#include <cassert>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <unordered_map>
#include <vector>

// constexpr const char* INPUT_FILE = "input.small.txt";
constexpr const char* INPUT_FILE = "input.txt";
using value_type = int;
using map_t = std::unordered_map<value_type, size_t>;

map_t calculate_frequency(const std::vector<value_type>& vec) {
    map_t res;

    for (auto num : vec) {
        ++res[num];
    }

    return res;
}

ulong distance(map_t& l1, map_t& l2) {
    ulong sum = 0;

    for (auto&& [key, value] : l1) {
        std::cerr << "Adding "
            << key << " * "
            << l1[key] << " * "
            << l2[key] << " = "
            << key * l1[key] * l2[key] << std::endl;
        sum += key * value * l2[key];
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

    load_input(first, second);

    map_t l1 = calculate_frequency(first);
    map_t l2 = calculate_frequency(second);

    std::cout << distance(l1, l2) << std::endl;
}
