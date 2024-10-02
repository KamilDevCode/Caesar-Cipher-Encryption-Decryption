# 🎉 Caesar Cipher Encryption & Decryption with Facade 🔐

![Python](https://img.shields.io/badge/Python-3.12-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## 📖 Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Menu Options](#menu-options)
  - [Example Interaction](#example-interaction)
- [Saving and Loading History](#saving-and-loading-history)
- [Unit Tests](#unit-tests)
- [Code Structure](#code-structure)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## 🚀 Project Overview
The **Caesar Cipher Encryption & Decryption** application is a user-friendly command-line tool that implements the classic Caesar Cipher encryption algorithm. The application allows users to encrypt and decrypt text easily, manage operation history, and save/load this history from JSON files. This project follows the **Facade** design pattern, providing a simplified interface for complex functionality.

## 🌟 Features
- **Text Encryption and Decryption**: Supports the basic functionality of the Caesar Cipher, allowing for easy text manipulation.
- **Shift Value Flexibility**: Users can specify any integer shift value for encryption and decryption.
- **Operation History Management**: Automatically logs all operations performed during a session, including inputs, outputs, and timestamps.
- **JSON File Handling**: Save and load operation history using JSON files for easy persistence.
- **User-Friendly Menu Interface**: Clear navigation through various operations with prompts and instructions.
- **Unit Testing**: Comprehensive tests to ensure the correctness and reliability of the implementation.
- **Error Handling**: Robust error handling for invalid inputs and operations.

## 🛠️ Getting Started

### Prerequisites
Ensure you have the following installed:
- Python 3.12 or later
- Pip (Python package installer)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Caesar-Cipher-Encryption-Decryption-with-Facade.git
   ```
   2. Change your directory:
      ```bash
       cd Caesar-Cipher-Encryption-Decryption-with-Facade
      ```
   
## 🗂️ Code Structure
The project is organized into the following directories and files:

### Project Structure
```bash
Caesar-Cipher-Encryption-Decryption-with-Facade/
├── src/
│   ├── app.py                     # Main application entry point
│   ├── ciphers/
│   │   └── caeser.py              # Caesar Cipher implementation
│   ├── files/
│   │   └── json_manager.py         # JSON handling for saving/loading history
│   ├── history/
│   │   └── record.py               # Operation record management
│   └── facade.py                   # Menu and application control logic
│
├── tests/
│   ├── test_caeser.py              # Unit tests for the Caesar Cipher
│   ├── test_history.py             # Unit tests for history management
│   └── test_facade.py              # Unit tests for the facade
│
├── requirements.txt                 # Project dependencies
├── LICENSE                          # License information
└── README.md                        # Project documentation
```

## 🧪 Usage

### Menu Options
The following menu options are available:
Example Usage 💡
Encrypting Text:

Choose option 1.
Enter the text to encrypt and the desired shift value.
Decrypting Text:

Choose option 2.
Enter the text to decrypt and the shift value used during encryption.
Save and Load History:

Use options 3 and 4 to manage your operation history.


### Testing 🧪
Unit tests are written using pytest to verify the functionality of the encryption and decryption processes, as well as the JSONmanagement functionalities. To run the tests, execute the following command:

```bash
pytest tests/
```

### Contributing 🤝
Contributions are welcome! If you have suggestions for improvements or new features, please feel free to fork the repository and submit a pull request. Ensure to follow the project's coding standards and include tests for any new functionality.

### License 📄
This project is licensed under the MIT License. See the LICENSE file for more information
