# MikroTik WBX to CSV Converter

This repository contains a Python script that converts MikroTik WBX files into CSV format. This tool is useful for network administrators and other users of MikroTik products who need to analyze or process configuration data exported from WinBox.

## What is MikroTik?

[MikroTik](https://mikrotik.com/) is a Latvian company that produces networking equipment and software for data network management purposes. MikroTik's RouterOS software, which powers their routers and wireless ISP systems, is renowned for its rich feature set which spans across numerous network protocols and features.

## What is a WBX File?

A WBX file is a binary file format used by MikroTik's WinBox application. WinBox is a GUI application for managing MikroTik RouterOS, and it allows administrators to save various configurations and settings of a MikroTik router into a single WBX file. These files are useful for backing up router configurations and moving settings from one router to another.

## Exporting WBX Files from WinBox

To export a WBX file from WinBox:

1. Open WinBox and connect to your MikroTik device.
2. Go to the "Tools" menu.
3. Select "Export" to export the configuration or parts of it.
4. Choose the sections you want to export and specify the format as WBX.
5. Save the file to your local machine.

## How to Use This Application

This Python script converts a WBX file into a readable CSV format, making it easier to view and analyze the data using spreadsheet software or other tools.

### Prerequisites

Ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Installation

Clone this repository to your local machine using Git:

\`\`\`bash
git clone https://github.com/yourgithubusername/mikrotik-wbx-to-csv.git
cd mikrotik-wbx-to-csv
\`\`\`

### Usage

Run the script with the following command-line arguments:

- \`-i\` or \`--input\`: Specifies the input WBX file.
- \`-o\` or \`--output\`: Specifies the output CSV file.
- \`-d\` or \`--debug\`: Enables debug output (optional).

Example command:

\`\`\`bash
python wbx_to_csv_converter.py -i input.wbx -o output.csv
\`\`\`

To enable debugging output, add the \`-d\` flag:

\`\`\`bash
python wbx_to_csv_converter.py -i input.wbx -o output.csv -d
\`\`\`

## License

This project is licensed under the MIT License - see the LICENSE file for details.
