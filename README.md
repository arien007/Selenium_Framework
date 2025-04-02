# Automatic Bot Application

Welcome to the **Automatic Bot Application**! This project is a PySide6-based GUI application designed to automate browser interactions using Selenium. It allows users to input application names, browser links, and XPaths for automation tasks, making it a powerful tool for automating repetitive web tasks.

---

## Features

- **User-Friendly GUI**: Built with PySide6, the application provides an intuitive interface for users to interact with.
- **Browser Automation**: Uses Selenium to automate browser actions like clicking and typing.
- **Dynamic Input Handling**: Accepts user inputs for application names, browser links, and XPaths.
- **Output Logging**: Saves automation scripts and logs to a Python file (`text_output_pyside6.py`) for further use.
- **Customizable Actions**: Supports both "Click" and "Write" actions for web elements.

---

## How It Works

1. **Setup**:
   - The application initializes a GUI with input fields and buttons.
   - Users can input the application name, browser link, and XPaths for automation.

2. **Input Handling**:
   - The `lineeditApp` and `lineeditLink` fields accept the application name and browser link, respectively.
   - The `lineeditInput` field accepts XPaths for automation.

3. **Automation**:
   - Users can toggle between "Click" and "Write" modes using the respective buttons.
   - The application generates Selenium-based Python scripts for the specified actions.

4. **Output**:
   - The generated scripts are saved to `text_output_pyside6.py`.
   - Users can choose to open the output file directly from the application.

---

## How to Use

### Prerequisites

- Python 3.8 or higher
- Required Python libraries:
  - `PySide6`
  - `selenium`
  - `pystyle`
  - `undetected_chromedriver`
- Google Chrome installed on your system

### Installation

1. Clone the repository:
   ```bash
   git clone  https://github.com/arien007/Selenium_Framework.git
   cd automatic-bot
2. Install dependencies:
   ```bash
   pip install -r requirements .txt
3. Run the application:
   ```bash
   python hello. py

## Using the Application
1. Input Application Name:
 Enter the name of your application in the "Name" field.
2. Input Browser Link:
    Enter the URL of the website you want to automate in the "Browser" field.
3. Add XPaths:
    Enter the XPath of the web element in the "Add" field.
    Choose between "Click" or "Write" modes to specify the action.
4. Generate Script:
    Click the "Ready" button to generate the automation script.
    The script will be saved to text_output_pyside6.py .
5. Run Automation:
    Open the generated script and execute it to perform the automation.
   Example
## Here's an example of how to use the application:
1. Enter "MyApp" in the "Name" field.
2. Enter "example.com" in the "Browser" field.
3. Add an XPath (e.g., /html/body/div[1]/.../div[1]/form/div[5]/a ) in the "Add" field.
4. Select "Click" mode and click "Add".
5. Click "Ready" to generate the script.
6. Open text_output_pyside6.py to view the generated script.
### Contributing
Feel free to fork this repository and
submit pull requests. Contributions are
welcome!
### License
This project is licensed under the MIT
License. See the LICENSE file for details
### Contact
For any questions or feedback, please
contact tinasora5553@gmail.com

This README is designed to help users understand your project, its purpose, and how to use it effectively. It also includes tags to improve discoverability.
   
