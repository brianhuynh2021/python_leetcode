# LeetCode & Technical Interview Practice

A comprehensive repository for coding interview preparation, featuring solutions to LeetCode problems, "Cracking the Coding Interview" challenges, Object-Oriented Programming concepts, and System Design fundamentals.

## 📁 Repository Structure

```
├── coding_challenge/         # Core coding problems and solutions
│   ├── Python/              # Python implementations (97+ problems)
│   ├── C++/                 # C++ implementations
│   └── coding_log.md        # Detailed problem-solving journal
├── OOP/                     # Object-Oriented Programming concepts
│   ├── day01_intro/         # OOP fundamentals
│   ├── day02_encapsulation/ # Encapsulation principles
│   ├── day03_abstraction/   # Abstraction concepts
│   ├── day04_inheritance/   # Inheritance patterns
│   ├── day05_polymorphism/  # Polymorphism examples
│   └── oop_log.md          # OOP learning journal
├── system_design/           # System Design concepts and case studies
│   ├── CAP Theorem/         # Consistency, Availability, Partition tolerance
│   ├── Throttling_and_rate_limits/ # Rate limiting strategies
│   ├── message_queue/       # Message queue patterns
│   └── system_design_log.md # System design notes
├── flows_and_diagrams/      # Visual problem-solving diagrams
├── SQL/                     # SQL query practice
└── interview_questions/     # Common interview questions
```

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- g++ compiler (for C++ solutions)
- Virtual environment (recommended)

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/brianhuynh2021/python_leetcode.git
   cd python_leetcode
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 💡 Problem Categories

### Data Structures & Algorithms
- **Arrays & Strings**: Two-pointer technique, sliding window, string manipulation
- **Linked Lists**: Reversal, cycle detection, merging, intersection finding
- **Binary Search**: Search variations, peak finding, rotated arrays
- **Stack & Queue**: Parentheses validation, daily temperatures, heap operations
- **Sliding Window**: Maximum/minimum in window, longest substring problems
- **Heap**: Top K elements, median finding, priority queues

### Advanced Patterns
- **Two Pointers**: Target sum, triplet problems, array manipulation
- **Fast & Slow Pointers**: Cycle detection, middle node finding
- **Binary Search Variations**: Ceiling/floor finding, search in 2D matrix
- **Stack Applications**: Reverse Polish notation, histogram problems

## 🏃‍♂️ Running Solutions

### Python Solutions
```bash
# Run individual solution
python coding_challenge/Python/lc_97_sliding_window_maximum.py

# Run with unittest
python -m unittest tests.test_lc_83_minimum_different_element

# Discover and run all tests
python -m unittest discover -s tests
```

### C++ Solutions
```bash
# Compile and run C++ solution
g++ coding_challenge/C++/34_get_kth_to_last_node.cpp -o main
./main
```

## 📚 Learning Approach

### Problem-Solving Strategy
Each problem follows a structured approach documented in `coding_log.md`:
1. **Brute Force**: Initial O(n²) or O(n³) approach
2. **Optimization**: Improved time/space complexity solution
3. **Test Cases**: Edge cases and examples
4. **Self-Explanation**: Verbal walkthrough of solution

### Code Documentation Pattern
Solutions include:
- Problem description with examples
- Multiple approaches (brute force → optimized)
- Time/space complexity analysis
- Test cases and edge cases
- Type hints and clean variable naming

Example format:
```python
'''
Problem: Sliding Window Maximum
Given: Array of integers and window size k
Task: Return maximum element in each sliding window

Example:
nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
'''
```

## 🎯 Key Features

- **97+ LeetCode Problems**: Comprehensive coverage of common interview patterns
- **Dual Language Support**: Python and C++ implementations
- **Progressive Learning**: Problems organized by difficulty and concept
- **Detailed Logging**: Problem-solving thought process documented
- **Test Coverage**: Unit tests for validation
- **Visual Aids**: Flow diagrams for complex algorithms
- **System Design**: Scalability and architecture concepts

## 📈 Progress Tracking

Track your progress using the learning logs:
- `coding_challenge/coding_log.md` - Daily problem-solving sessions
- `OOP/oop_log.md` - Object-oriented programming concepts
- `system_design/system_design_log.md` - System design patterns

## 🤝 Contributing

Feel free to:
- Add new problem solutions
- Improve existing implementations
- Add test cases
- Update documentation

## 📄 License

This project is for educational purposes and interview preparation.
