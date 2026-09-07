import os
import sys

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def banner():
    os.system('clear')
    print(f"{Colors.CYAN}{Colors.BOLD}")
    print(r"""
    ██████╗  █████╗ ████████╗██╗  ██╗██╗   ██╗███╗   ██╗████████╗
    ██╔══██╗██╔══██╗╚══██╔══╝██║  ██║██║   ██║████╗  ██║╚══██╔══╝
    ██████╔╝███████║   ██║   ███████║██║   ██║██╔██╗ ██║   ██║   
    ██╔═══╝ ██╔══██║   ██║   ██╔══██║██║   ██║██║╚██╗██║   ██║   
    ██║     ██║  ██║   ██║   ██║  ██║╚██████╔╝██║ ╚████║   ██║   
    ╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   
    """)
    print(f"    [ PathHunt v0.1 - Blue Team File & Integrity Scanner ]")
    print(f"    [ Coder: YourName ]{Colors.ENDC}\n")

def search_files(target_dir, keyword, file_extension):
    print(f"\n{Colors.BLUE}[*] Scanning directory: {target_dir}{Colors.ENDC}")
    print(f"{Colors.BLUE}[*] Searching for keyword: '{keyword}' inside '{file_extension}' files...{Colors.ENDC}\n")
    
    found_count = 0
    
    if file_extension and not file_extension.startswith('.'):
        file_extension = '.' + file_extension

    for root, dirs, files in os.walk(target_dir):
        for file in files:
            file_path = os.path.join(root, file)
            
            # Check in filename
            if keyword.lower() in file.lower():
                print(f"{Colors.GREEN}[+] Found in Filename: {file_path}{Colors.ENDC}")
                found_count += 1
                continue
            
            # Check inside files matching user's extension choice
            if file_extension and file.endswith(file_extension):
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        if keyword.lower() in content.lower():
                            print(f"{Colors.GREEN}[+] Found in Content: {file_path}{Colors.ENDC}")
                            found_count += 1
                except Exception:
                    pass
                    
    print(f"\n{Colors.HEADER}[*] Scan complete. Total matches found: {found_count}{Colors.ENDC}")

def start_fim(target_dir):
    print(f"\n{Colors.WARNING}[*] FIM engine for '{target_dir}' is under development...{Colors.ENDC}")
    input(f"\n{Colors.CYAN}Press Enter to return to the main menu...{Colors.ENDC}")

def main_menu():
    while True:
        banner()
        print(f"{Colors.HEADER}--- MAIN MENU ---{Colors.ENDC}")
        print(f"{Colors.GREEN}[1]{Colors.ENDC} Search Keyword in Files")
        print(f"{Colors.GREEN}[2]{Colors.ENDC} File Integrity Monitoring (FIM)")
        print(f"{Colors.FAIL}[3]{Colors.ENDC} Exit\n")
        
        choice = input(f"{Colors.WARNING}PathHunt > {Colors.ENDC}").strip()
        
        if choice == "1":
            print(f"\n{Colors.BLUE}[*] Starting Keyword Search Engine...{Colors.ENDC}")
            target = input("Enter directory to search (e.g., /home/user or .): ").strip()
            keyword = input("Enter keyword to find: ").strip()
            file_extension = input("Enter file extension to scan inside (e.g., txt, json, log): ").strip()
            
            if os.path.exists(target):
                search_files(target, keyword, file_extension)
            else:
                print(f"{Colors.FAIL}[-] Error: The specified directory does not exist.{Colors.ENDC}")
            
            input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.ENDC}")
            
        elif choice == "2":
            print(f"\n{Colors.BLUE}[*] File Integrity Monitoring (FIM) Mode{Colors.ENDC}")
            print(f"{Colors.GREEN}[1]{Colors.ENDC} Scan entire system (Root /)")
            print(f"{Colors.GREEN}[2]{Colors.ENDC} Choose a specific directory")
            
            sub_choice = input(f"{Colors.WARNING}FIM > {Colors.ENDC}").strip()
            
            if sub_choice == "1":
                target_dir = "/"
                print(f"{Colors.WARNING}[!] Warning: Scanning the entire system might take a while.{Colors.ENDC}")
                start_fim(target_dir)
            elif sub_choice == "2":
                target_dir = input("Enter path to monitor: ").strip()
                if os.path.exists(target_dir):
                    start_fim(target_dir)
                else:
                    print(f"{Colors.FAIL}[-] Error: The specified directory does not exist.{Colors.ENDC}")
                    input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.ENDC}")
            else:
                print(f"{Colors.FAIL}[-] Invalid FIM option!{Colors.ENDC}")
                input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.ENDC}")

        elif choice == "3":
            print(f"\n{Colors.FAIL}[*] Exiting PathHunt... Stay secure!{Colors.ENDC}\n")
            sys.exit()
        else:
            print(f"\n{Colors.FAIL}[-] Invalid choice! Please select 1, 2, or 3.{Colors.ENDC}")
            input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.ENDC}")

if __name__ == "__main__":
    main_menu()
