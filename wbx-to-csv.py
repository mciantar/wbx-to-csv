import csv
import argparse
import os

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Parse a binary WBX file and export to CSV.")
    parser.add_argument('-i', '--input', required=True, help='Input WBX file')
    parser.add_argument('-o', '--output', required=True, help='Output CSV file')
    parser.add_argument('-d', '--debug', action='store_true', help='Enable debugging output')
    return parser.parse_args()

def debug_log(message, debug):
    """Print debug message if debugging is enabled."""
    if debug:
        print(message)

def read_binary_file(filepath):
    """Read binary data from a file."""
    with open(filepath, 'rb') as file:
        return file.read()

def parse_binary_data(data, debug):
    """Parse binary data to extract fields into a list of dictionaries."""
    result = []
    i = 0
    current_entry = {}

    while i < len(data):
        if data[i:i+2] == b'\x00\x05':
            i += 2
            start = i
            debug_log(f"Debug: Examining possible 'group'/'login' section starting at {start}", debug)
            if data[i:i+5] == b'group':
                debug_log(f"Debug: Found 'group' section", debug)
                i += 5
                start = i
                while i < len(data) and data[i+1:i+2] != b'\x00':
                    i += 1
                group = data[start:i].decode('ascii')
                current_entry['group'] = group
                debug_log(f"Debug: 'group' at position {start}-{i-1}, value: {group}", debug)
            elif data[i:i+5] == b'login':
                debug_log(f"Debug: Found 'login' section", debug)
                i += 5
                start = i
                while i < len(data) and data[i+1:i+2] != b'\x00':
                    i += 1
                login = data[start:i].decode('ascii')
                current_entry['login'] = login
                debug_log(f"Debug: 'login' at position {start}-{i-1}, value: {login}", debug)
            else:
                debug_log(f"Debug: Unexpected data after x00 x05 at position {start}: {data[start:start+20]}", debug)
        elif data[i:i+2] == b'\x00\x04':
            i += 2
            start = i
            debug_log(f"Debug: Examining possible 'host'/'note' section starting at {start}", debug)
            if data[i:i+8] == b'typeaddr':
                debug_log("Debug: Skipping 'typeaddr' section.", debug)
                while i < len(data) and data[i+1:i+2] != b'\x00':
                    i += 1
            elif data[i:i+4] == b'host':
                debug_log(f"Debug: Found 'host' section", debug)
                i += 4
                start = i
                while i < len(data) and data[i+1:i+2] != b'\x00':
                    i += 1
                host = data[start:i].decode('ascii')
                current_entry['host'] = host
                debug_log(f"Debug: 'host' at position {start}-{i-1}, value: {host}", debug)
            elif data[i:i+4] == b'note':
                i += 4
                start = i
                while i < len(data) and data[i+1:i+2] != b'\x00':
                    i += 1
                note = data[start:i].decode('ascii')
                current_entry['note'] = note
                debug_log(f"Debug: 'note' at position {start}-{i-1}, value: {note}", debug)
            else:
                debug_log(f"Debug: Unexpected data after x00 x04 at position {start}: {data[start:start+20]}", debug)
        elif data[i:i+2] == b'\x00\x03' and data[i+2:i+5] == b'pwd':
            i += 5
            start = i
            while i < len(data) and data[i+1:i+2] != b'\x00':
                i += 1
            pwd = data[start:i].decode('ascii')
            current_entry['pwd'] = pwd
            debug_log(f"Debug: 'pwd' at position {start}-{i-1}, value: {pwd}", debug)
        elif data[i:i+2] == b'\x00\x0b':
            result.append(current_entry)
            debug_log(f"Debug: End record, final entry: {current_entry}", debug)
            current_entry = {}
            i += 2
        i += 1

    return result

def write_csv(data, filename):
    """Write parsed data to a CSV file."""
    fieldnames = ['group', 'host', 'login', 'note', 'pwd']
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for entry in data:
            writer.writerow(entry)

def main():
    args = parse_arguments()
    debug = args.debug

    if not os.path.exists(args.input):
        print("Error: Input file does not exist.")
        return

    try:
        binary_data = read_binary_file(args.input)
        parsed_data = parse_binary_data(binary_data, debug)
        write_csv(parsed_data, args.output)
        print("Data parsing complete. CSV file created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
