# GPT API Integration 💻🚀

This project demonstrates how to integrate OpenAI's GPT models into a Python application using the OpenAI API. It covers the setup process, dependency installation, and interaction with GPT models to generate text-based outputs.

## Getting Started 🚀

Follow these steps to set up and run the project on a local machine.

### **1. Install Python** 🐍

Ensure Python 3.11 or later is installed. If Python is not already installed, follow these steps:

- For a detailed guide on how to install Python on different operating systems, refer to the [Quick Guide for Installing Python](https://github.com/PackeTsar/Install-Python/blob/master/README.md#install-python-).
- The latest version of Python can be downloaded from the official website: [Download Python](https://www.python.org/downloads/).

### **2. Create a Virtual Environment** 💻

Creating a virtual environment is recommended to manage dependencies for the project.

- **For Windows**:
    ```bash
    python -m venv venv
    ```

- **For MacOS**:
    ```bash
    python3 -m venv venv
    ```

### **3. Activate the Virtual Environment** 🔑

After creating the virtual environment, it needs to be activated:

- **For Windows**:
    ```bash
    venv/Scripts/activate
    ```

- **For MacOS**:
    ```bash
    source venv/bin/activate
    ```

The terminal should display `(env)` at the beginning of the prompt after activation.

### **4. Install Project Dependencies** 📦

Install the required libraries using the `requirements.txt` file:

- **For Windows**:
    ```bash
    pip install -r requirements.txt
    ```

- **For MacOS**:
    ```bash
    pip3 install -r requirements.txt
    ```

This command will install all necessary dependencies for running the GPT API integration.

### **5. Obtain OpenAI API Key** 🔑

To use the GPT models, an API key from OpenAI is required.

1. Visit [OpenAI API Keys](https://platform.openai.com/account/api-keys).
2. Copy the API key.

### **6. Set Up the API Key** 🔑

Create a `.env` file in the root directory of the project and add the API key:

```
OPENAI_API_KEY=your_api_key_here
```

Alternatively, the API key can be exported in the terminal session:

- **For Windows**:
    ```bash
    set OPENAI_API_KEY=your_api_key_here
    ```

- **For MacOS**:
    ```bash
    export OPENAI_API_KEY='your_api_key_here'
    ```

### **7. Run the Script** ▶️

Once the setup is complete, the script can be executed to interact with the GPT models.

- **For Windows**:
    ```bash
    python main.py
    ```

- **For MacOS**:
    ```bash
    python3 main.py
    ```

The script will execute and interact with the GPT models as defined in `main.py`.


## Notes 📌

- A stable internet connection is required to access the OpenAI API.
- If issues arise, ensure that the virtual environment is activated and dependencies are installed correctly.
- The project is designed to work with Python 3.11 or later.

##  Contributing 💡

Contributions are welcome through forks and pull requests. Follow the contribution guidelines and ensure the code is well-documented.