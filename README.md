# Ulauncher Terminator Extension

This Ulauncher extension allows you to open the Terminator terminal in a
specific folder.

## Features

- Open Terminator in a folder of your choice.
- Autocompletion for folder paths.

## Installation

1. Clone this repository:

  ```bash
   git clone https://github.com/your-repo/ulauncher-terminator.git
   ```

2. Navigate to the project directory:

   ```bash
   cd ulauncher-terminator
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Link the extension to Ulauncher:

   ```bash
   ln -s $(pwd) ~/.local/share/ulauncher/extensions/ulauncher-terminator
   ```

## Usage

1. Open Ulauncher.
2. Type the keyword `term` followed by a folder path (e.g., `term
   ~/Documents`).
3. Select a folder from the suggestions or press Enter to open Terminator in
   the specified folder.

## Requirements

- Ulauncher 5.0.0 or higher.
- Terminator terminal installed on your system.

## Development

To contribute or modify the extension:

1. Make your changes in the `main.py` file.
2. Test the extension by restarting Ulauncher.

## License

This project is licensed under the GNU General Public License v3.0 or later.  
See the [LICENSE](LICENSE) file for more details.
