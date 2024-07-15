import os
import time
import multiprocessing

#List of websites to be blocked
blocklist = ["www.yahoo.com"]

# Path to the hosts file
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect_ip = "127.0.0.1"

def block_websites():
  while True:
    try:
      with open(host_path, "r+") as file:
        content = file.read()
        for website in blocklist:
          if website not in content:
            file.write(f"{redirect_ip} {website}\n")
      time.sleep(60)  # Check and update the hosts file every 60 seconds
    except Exception as e:
      print(f"Error blocking websites: {e}")
      time.sleep(60)


def unblock_websites():
    try:
      with open(hosts_path, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
          if not any(website in line for website in blocklist):
            file.write(line)
        file.truncate()
    except Exception as e:
        print(f"Error unblocking websites: {e}")


def main():
    # Unblock websites on exit
    import atexit
    atexit.register(unblock_websites)

    # Start the blocking process
    p = multiprocessing.Process(target=block_websites)
    p.start()

    try:
        while True:
            time.sleep(1)  # Keep the main script running
    except KeyboardInterrupt:
        p.terminate()
        p.join()

if __name__ == "__main__":
    if os.name == 'nt':
        main()
    else:
        print("This script is intended to be run on Windows.")
