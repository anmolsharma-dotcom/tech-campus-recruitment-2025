import sys
import os

def binary_search_logs(log_file_path, target_date):
    """
    Efficiently extracts all log entries for a given date using binary search.
    Assumes the log file is sorted chronologically.
    :param log_file_path: Path to the log file.
    :param target_date: Date string in YYYY-MM-DD format.
    """
    try:
        with open(log_file_path, 'r', encoding='utf-8') as file:
            start, end = 0, os.path.getsize(log_file_path)
            while start < end:
                mid = (start + end) // 2
                file.seek(mid)
                file.readline()  # Move to the next complete line
                line = file.readline()
                if not line:
                    end = mid
                    continue
                
                log_date = line[:10]
                if log_date < target_date:
                    start = mid + 1
                else:
                    end = mid
            
            file.seek(start)
            for line in file:
                if line.startswith(target_date):
                    print(line.strip())
                elif line[:10] > target_date:
                    break
    except FileNotFoundError:
        print(f"Error: File '{log_file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python extract_logs.py <log_file_path> <YYYY-MM-DD>")
        sys.exit(1)
    
    log_file_path = sys.argv[1]
    target_date = sys.argv[2]
    binary_search_logs(log_file_path, target_date)
