import time
import os
import random
import sys

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

def slow_print(text, delay=0.04):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def banner():
    os.system("clear")
    print(RED + r"""
  ██████╗ ██████╗ ███████╗ ██████╗  ██████╗  ██████╗ ███████╗
 ██╔════╝ ██╔══██╗██╔════╝██╔════╝ ██╔═══██╗██╔════╝ ██╔════╝
 ██║  ███╗██████╔╝█████╗  ██║  ███╗██║   ██║██║  ███╗█████╗  
 ██║   ██║██╔═══╝ ██╔══╝  ██║   ██║██║   ██║██║   ██║██╔══╝  
 ╚██████╔╝██║     ███████╗╚██████╔╝╚██████╔╝╚██████╔╝███████╗
  ╚═════╝ ╚═╝     ╚══════╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝
                   IP Spoofing & Traffic Generation Toolkit
:: Disclaimer: Developers assume no liability and are not responsible for any misuse or damage caused by ipsxa ::
:: Only use for educational purposes!!                                                   ::
:: Created by amaelahmed
""" + RESET)
    time.sleep(2)

def loading_animation(task, duration=3):
    print(f"{CYAN}[+] {task}...{RESET}")
    for i in range(duration):
        sys.stdout.write(f"\r    [{'.' * (i % 4)}{' ' * (3 - i % 4)}] {int((i+1)/duration*100)}%")
        sys.stdout.flush()
        time.sleep(1)
    print("\r    [✓] Done.\n")
    time.sleep(0.5)

def spoof_ip(target_ip):
    loading_animation(f"Spoofing IP {target_ip}", 4)
    slow_print(f"{GREEN}[✓] Spoof successful. System identity masked as: {target_ip}{RESET}")
    time.sleep(1)

def inject_payloads():
    print(f"{YELLOW}[*] Injecting crafted payloads into outbound traffic...{RESET}")
    payloads = [
        "SQLi test string appended to URL",
        "Encoded shell script injected into user-agent",
        "Authorization headers fuzzed with random tokens",
        "Base64-encoded reverse shell in POST body",
        "Long parameter overflow on /api/auth",
        "Session hijack attempt using stolen cookie"
    ]
    for payload in payloads:
        time.sleep(0.9)
        slow_print(f"    > {payload}")
    time.sleep(1)
    print(f"{GREEN}[+] Payload stack transmitted successfully.{RESET}")
    time.sleep(1)

def generate_suspicious_requests():
    print(f"{YELLOW}[*] Generating high-volume traffic to monitored endpoints...{RESET}")
    endpoints = [
        "https://gov-secureportal.net/auth",
        "https://bank-core-api.com/login",
        "https://corp-admin-panel.in/upload",
        "https://mil-net-router/command",
        "https://records.internal/reset"
    ]
    actions = ["POST /auth", "GET /admin", "DELETE /logs", "UPLOAD malware.tar", "PATCH /user/config"]

    for i in range(10):
        ip = f"10.0.0.{random.randint(2, 254)}"
        url = random.choice(endpoints)
        action = random.choice(actions)
        print(f"{CYAN}    [{ip}] => {action} -> {url}{RESET}")
        time.sleep(0.5)

    time.sleep(1)
    print(f"{GREEN}[+] Traffic spike completed. Logs show activity from spoofed source.{RESET}")

def cleanup():
    print(f"{YELLOW}\n[*] Cleaning up environment and spoof traces...{RESET}")
    loading_animation("Erasing temporary routing rules", 2)
    loading_animation("Flushing DNS & ARP cache", 2)
    loading_animation("Wiping spoof history", 2)
    print(f"{GREEN}[✓] Session terminated cleanly. No trace left behind.{RESET}\n")
    time.sleep(1)

def main():
    banner()
    target_ip = input(f"{CYAN}Enter IP address to spoof: {RESET}").strip()
    spoof_ip(target_ip)
    inject_payloads()
    generate_suspicious_requests()
    cleanup()

if __name__ == "__main__":
    main()
