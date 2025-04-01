#include <cstdlib>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

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

std::vector<int> vectorize(const std::string& s) {
    std::vector<int> v;
    std::stringstream ss(s);
    int i;
    while (ss >> i)
        v.push_back(i);
    return v;
}

bool process_record_with_skip(const std::vector<int>& v, size_t skip_inx) {
    if (v.size() <= 3) return true;

    bool is_asending = true;
    if (skip_inx == 0)
        is_asending = v[1] < v[2];
    else if (skip_inx == 1)
        is_asending = v[0] < v[2];
    else
        is_asending = v[0] < v[1];


    int end = (skip_inx == v.size() - 1) ? v.size() - 2 : v.size() - 1;
    for(int i = 0; i < end; ++i) {
        if (i == skip_inx) {
            continue;
        }
        else if (i + 1 == skip_inx)  {
            if (!check_levels_in_diff(v[i], v[i+2], is_asending))
                return false;
        }
        else if (!check_levels_in_diff(v[i], v[i+1], is_asending))
            return false;
    }

    return true;
}

bool process_record(const std::vector<int>& v) {
    for (int i = 0; i <= v.size(); ++i)
        if (process_record_with_skip(v, i))
            return true;
    return false;
}


int main() {
    std::ifstream file(INPUT_FILE); // Open file for reading
    std::string line;

    int res = 0;
    while (true) {
        std::getline(file, line);
        if (line == "") break;
        const std::vector<int> v = vectorize(line);
        if (process_record(v)) {
            ++res;
            std::cerr << "SAFE" << std::endl;
        }
        else {
            std::cerr << "UNSAFE" << std::endl;
        }

    }
    file.close();
    std::cout << res << std::endl;
}
