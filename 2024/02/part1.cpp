#include <cstdlib>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>

// constexpr const char* INPUT_FILE = "input.small.txt";
constexpr const char* INPUT_FILE = "input.txt";
constexpr int MIN_DIFF_ON_LEVELS = 1;
constexpr int MAX_DIFF_ON_LEVELS = 3;

bool check_levels_in_diff(int l1, int l2, bool is_asending) {
    if (((l1 < l2) ^ is_asending) != 0)
        return false;

    int diffrence = std::abs(l1 - l2);

    if (diffrence < MIN_DIFF_ON_LEVELS || diffrence > MAX_DIFF_ON_LEVELS)
        return false;

    return true;
}

bool process_record(const std::string& line) {
    std::stringstream record(line);
    int last_num, curr_num;
    record >> last_num >> curr_num;
    bool is_assending = last_num < curr_num;
    if (!check_levels_in_diff(last_num, curr_num, is_assending))
        return false;

    last_num = curr_num;
    while (record >> curr_num) {
        if (!check_levels_in_diff(last_num, curr_num, is_assending))
            return false;
        last_num = curr_num;
    }
    return true;
}


int main() {
    std::ifstream file(INPUT_FILE); // Open file for reading
    std::string line;

    int res = 0;
    while (std::getline(file, line)) {
        if (process_record(line))
            ++res;
    }


    std::cout << res << std::endl;
}
