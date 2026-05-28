# Team Project: Password Generator & Analyzer

A Python-based console application designed for automatic secure password generation based on user-defined criteria and static analysis of their cryptographic strength.

## Project Structure

* `src/` — source code of the application.
  * `main.py` — the main coordination module of the application.
  * `generator.py` — the computational module (generation and strength assessment).
  * `io_utils.py` — the module for handling file operations and configuration validation.
* `data/` — directory for storing input and resulting files.
  * `input.txt` — configuration file containing parameters for the generator.
  * `output.txt` — automatically generated report containing the created password.
* `tests/` — automated module tests.
  * `test_generator.py` — a set of unit tests to validate the generator logic.

## Team Role Distribution

* **Student A (Team Lead):** Developing the project architecture, implementing the input/output data system (`io_utils.py`), integrating modules at the main entry point (`main.py`), configuring version control, and coordinating code changes.
* **Student B (Developer):** Implementing the core password generator, creating the algorithm for evaluating resistance to compromise (`generator.py`), and writing unit tests (`tests/test_generator.py`).

