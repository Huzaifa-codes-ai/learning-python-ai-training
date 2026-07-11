def process_log_file(file_path, log_level):
    """
    Reads a file, filters lines by a specific log level, 
    and handles potential file system errors safely.
    """
    matching_logs = []
    
    # 1. The Error Handling Block: Protects the app from crashing
    try:
        # Open the file in 'r' (read) mode cleanly using a context manager
        with open(file_path, "r") as file:
            for line in file:
                # Clean up whitespace and check for the target keyword (case-insensitive)
                if log_level.lower() in line.lower():
                    matching_logs.append(line.strip())
                    
        return matching_logs

    except FileNotFoundError:
        print(f"Error: The file located at '{file_path}' could not be found.")
        return []
        
    except Exception as e:
        print(f"An unexpected system error occurred: {e}")
        return []

# --- MAIN EXECUTION BLOCK ---
print("=== AI LOG PARSER WORKSPACE ===")

target_file = "app_logs.txt"
severity_filter = "ERROR"

# 2. Call our function and capture the output
found_errors = process_log_file(target_file, severity_filter)

# 3. Print the results safely
if found_errors:
    print(f"\nSuccessfully found {len(found_errors)} matching entries:")
    for log in found_errors:
        print(f"-> {log}")
else:
    print("\nNo matching logs found or processing failed.")
