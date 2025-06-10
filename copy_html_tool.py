import os
import time
import requests

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def loading_animation():
    msg = "TOOLS IS STARTING"
    for c in msg:
        print(c, end='', flush=True)
        time.sleep(0.1)
    print("\n")
    for i in range(21):
        bar = "█" * i + '-' * (20 - i)
        print(f"\rLoading: [{bar}] {i * 5}%", end='', flush=True)
        time.sleep(0.05)
    print("\n")

def display_header():
    print("\033[1;32m╔═════════════════════════════════════╗")
    print("║        HTML COPY TOOL v1.0         ║")
    print("╚═════════════════════════════════════╝")
    print("\033[0;91m         DEVELOPED BY OLD HACKER\033[0m")
    print()

def main_menu():
    print("\033[1;36m[1] ENTRY TO COPY ANY WEBSITE HTML CODES")
    print("[2] JOIN TOOL OWNER WHATSAPP CHANNEL\033[0m")
    return input("\n📥 ENTER OPTION (1/2): ").strip()

def post_copy_menu():
    print("\n\033[1;33m[1] COPY ANOTHER CODE")
    print("[2] EXIT TOOL\033[0m")
    return input("\n👉 ENTER OPTION (1/2): ").strip()

def copy_html_code():
    while True:
        url = input("\n🔗 Enter your website link: ").strip()
        try:
            response = requests.get(url)
            response.raise_for_status()

            save_path = "/sdcard/DCIM/copied_html_code.html"
            with open(save_path, "w", encoding="utf-8") as f:
                f.write(response.text)

            print("\n✅ HTML code copied successfully!")
            print("📁 YOUR CODES SAVED IN DCIM FOLDER 📁")
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")

        # Ask user if they want to copy again or exit
        next_action = post_copy_menu()
        if next_action == "1":
            clear_screen()
            display_header()
            continue
        elif next_action == "2":
            print("\n👋 Exiting tool... Stay safe hacker 🕶️")
            break
        else:
            print("❌ Invalid option. Exiting.")
            break

def open_whatsapp_channel():
    print("\n📲 Opening WhatsApp Channel...")
    try:
        os.system("termux-open-url https://whatsapp.com/channel/0029VavHzv259PwTIz1XxJ09")
    except Exception as e:
        print(f"❌ Failed to open link: {e}")

# ==== RUN TOOL ====
clear_screen()
loading_animation()
clear_screen()
display_header()
choice = main_menu()

if choice == "1":
    copy_html_code()
elif choice == "2":
    open_whatsapp_channel()
else:
    print("❌ Invalid option.")