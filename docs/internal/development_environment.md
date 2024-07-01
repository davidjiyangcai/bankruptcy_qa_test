## Virtual environment

### Setting up the virtual environment (one-time)

This section describes how to set up a Python virtual environment in the `<REPO>` directory.

1. Install Python Globally: 
   If you haven't installed Python yet, download it from [the official Python downloads page](https://www.python.org/downloads/). The latest version is `3.12.4`, we may fix a version later if there are compatibility issues.
2. Open <REPO> in VS Code:
   Launch Visual Studio Code and navigate to File > Open Folder, then select the <REPO> directory.
3. Open a Terminal in VS Code: 
   In VS Code, go to Terminal > New Terminal to open a new terminal.
4. Navigate to `<REPO>`.
    ```sh
    cd <REPO>
    ```
5. Create the Virtual Environment: 
   Set up the virtual environment in `<REPO>/.venv`. If Python is not recognized, refer to [this guide](https://realpython.com/add-python-to-path/) on adding Python to PATH.
    ```sh
    # For Windows
    python -m venv .venv

    # For macOS
    python3 -m venv .venv
    ```
6. Activate the Virtual Environment: 
   You should see `(.venv)` at the start of the command line, indicating activation. If you encounter a script execution error on Windows, see [this solution](https://stackoverflow.com/a/4038991). 
    ```sh
    # For Windows
    .venv/Scripts/activate

    # For macOS
    source .venv/bin/activate
    ```
7.  Install Dependencies:
    Install all required packages. This may take some time.
    ```sh
    pip install -r requirements.txt
    ```
8.  Verify Installation:
    List the installed packages to confirm successful installation.
    ```sh
    pip freeze
    ```
The virtual environment is now configured in `<REPO>/.venv.` This directory is ignored by Git and is local to your setup. If you want to view the hidden folder, you can:

For macos: press `Cmd + Shift + .`

For Windows 11: Three dots menu (...) > Options > View > Show hidden files, folders, and drives.

For Windows 10: View tab in Ribbon > Check Hidden items.


* To update the virtual environment, re-run step 7 to install new dependencies.
* To recreate the virtual environment, delete the `<REPO>/.venv folder` and repeat steps 4-8.



### Activating the virtual environment

VS Code generally activates the virtual environment automatically when you open `<REPO>`. If you need to activate it manually:

* Follow step 6 in [Setting Up the Virtual Environment (One-Time)](#setting-up-the-virtual-environment-one-time) to activate it.
* To select the appropriate Python interpreter in VS Code, press `Ctrl+P`, type `> Python: Select Interpreter` (don't forget the `>` sign), and select `<REPO>\.venv\Scripts\python.exe` for Windows or `<REPO>/.venv/bin/python3` for macOS.

To deactivate the virtual environment, run:

```sh
deactivate
```



### Updating the virtual environment

1. Add New Packages:
   Update the `<REPO>/requirements.txt` file with the new package names.
2. Install New Dependencies:
   With the virtual environment active ((.venv) in the prompt), run:

    ```sh
    pip install -r requirements.txt
    ```
    This might also update other packages for consistency.
