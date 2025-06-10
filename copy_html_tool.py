import os
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

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
    print("║     HTML + CSS COPY TOOL v2.0      ║")
    print("╚═════════════════════════════════════╝")
    print("\033[0;91m         DEVELOPED BY OLD HACKER\033[0m\n")

def main_menu():
    print("\033[1;36m[1] COPY WEBSITE HTML + CSS")
    print("[2] JOIN TOOL OWNER WHATSAPP CHANNEL\033[0m")
    return input("\n📥 ENTER OPTION (1/2): ").strip()

def post_copy_menu():
    print("\n\033[1;33m[1] COPY ANOTHER SITE")
    print("[2] EXIT TOOL\033[0m")
    return input("\n👉 ENTER OPTION (1/2): ").strip()

def copy_html_and_css():
    while True:
        url = input("\n🔗 Enter website link: ").strip()
        folder_path = "/sdcard/DCIM/copied_site"
        os.makedirs(folder_path, exist_ok=True)

        try:
            res = requests.get(url)
            res.raise_for_status()

            soup = BeautifulSoup(res.text, 'html.parser')

            # Save main HTML
            html_path = os.path.join(folder_path, "index.html")
            with open(html_path, "w", encoding="utf-8") as f:
                f.write(res.text)

            print("✅ HTML saved as index.html")

            # Extract and download CSS files
            css_links = soup.find_all("link", rel="stylesheet")
            css_count = 0
            for link in css_links:
                css_url = link.get("href")
                if not css_url:
                    continue
                full_url = urljoin(url, css_url)
                css_data = requests.get(full_url).text
                css_file_name = f"style_{css_count}.css"
                with open(os.path.join(folder_path, css_file_name), "w", encoding="utf-8") as css_file:
                    css_file.write(css_data)
                    css_count += 1

            print(f"✅ {css_count} CSS files downloaded")
            print("📁 Files saved in DCIM/copied_site folder")

        except Exception as e:
            print(f"\n❌ Error: {str(e)}")

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
    copy_html_and_css()
elif choice == "2":
    open_whatsapp_channel()
else:
    print("❌ Invalid option.")
