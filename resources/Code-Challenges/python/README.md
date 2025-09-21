# Python Code Challenges

This repo contains progressive Python challenges and exercises that can be used for self-study.

Each exercise has a corresponding solution file you may reference.

Some of these exercises may require you to do some googling to figure out the solution. Some resources that are great to rely on are:

* [w3 schools python reference](https://www.w3schools.com/python/)
* [official python3 documentation](https://docs.python.org/3/)
* [real python tutorials](https://realpython.com/)

---

## Running and Testing the Challenges

Each challenge in this repository has a corresponding Python file (e.g., `c01_repeat_statement.py`) and a test file (e.g., `test_c01_repeat_statement.py`) using Python’s built-in `unittest` framework. Follow these steps to run and test the challenges:

### 3. Run a Single Test File

You can run a specific test file to check your solution for that challenge:

```bash
python3 -m unittest tests.test_01_repeat_statement
```

Replace `test_01_repeat_statement.py` with the appropriate test file for the challenge you want to check.

### 4. Run All Tests at Once

If you want to run all test cases for all challenges in the `tests` folder, use:

```bash
python3 -m unittest discover -s tests
```

- `-s tests` tells unittest to look in the `tests` directory.

### 5. Interpreting Test Results

- **OK** – All test cases passed successfully.
- **FAIL** or **ERROR** – One or more test cases failed. Review the output to see which tests failed and debug your code accordingly.
- Example output:

```console
..F..
======================================================================
FAIL: test_repeat_statement_multiple (tests.test_c01_repeat_statement.TestRepeatStatement)
----------------------------------------------------------------------
Traceback (most recent call last):
  ...
AssertionError: 'Hello\nHello' != 'Hello\nHello\nHello'
```



---

## More Challenges

* [Big repo of progressive Python challenges](https://github.com/ChillFish8/Python-Challenges)
* [Coidio Python challenge labs](https://github.com/alicevillar/python-lab-challenges)
* [Edabit](https://edabit.com/challenges/python3) is an interactive site with many challenges to solve

---

## Sources

These exercises were adapted from the following sources:

* https://github.com/WDI-SEA/python-exercises
* https://github.com/WDI-SEA/python-challenges
* https://git.generalassemb.ly/team-wag/SEIR-Course-Materials/blob/main/Unit_3/1-python/1.2-python-control-flow.md
* https://git.generalassemb.ly/team-wag/SEIR-Course-Materials/blob/main/Unit_3/1-python/1.3.1-containers-lab.md
* https://git.generalassemb.ly/team-wag/SEIR-Course-Materials/blob/main/Unit_3/1-python/1.4-python-functions.md
* https://github.com/WDI-SEA/python-bank-account-inheritance
* https://github.com/weston-bailey/python-zoop-lab
