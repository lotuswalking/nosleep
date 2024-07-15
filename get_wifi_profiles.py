import subprocess


def get_cmd_encoding():
    """
    Get the current command prompt encoding using chcp command.
    """
    try:
        output = subprocess.check_output(['chcp'], shell=True)
        code_page = int(output.decode().strip().split(':')[-1].strip())
        encoding = f'cp{code_page}'
        return encoding
    except Exception as e:
        print(f"Error determining code page: {e}")
        return 'utf-8'  # Default to utf-8 if there's an error
def get_wifi_profiles(encoding):
    """
    Get the list of all saved Wi-Fi profiles.
    """
    profiles = []
    try:
        output = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'], encoding=encoding,errors='ignore')
        for line in output.split('\n'):
            if "All User Profile" in line:
                profile = line.split(":")[1].strip()
                profiles.append(profile)
    except subprocess.CalledProcessError as e:
        print(f"Error retrieving Wi-Fi profiles: {e}")
    return profiles

def get_wifi_password(profile,encoding):
    """
    Get the Wi-Fi password for a specific profile.
    """
    try:
        output = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', f'name={profile}', 'key=clear'], encoding=encoding,errors='ignore')
        for line in output.split('\n'):
            if "Key Content" in line:
                password = line.split(":")[1].strip()
                return password
    except subprocess.CalledProcessError as e:
        print(f"Error retrieving password for profile {profile}: {e}")
    return None

def main():
    encoding = get_cmd_encoding()
    profiles = get_wifi_profiles(encoding)
    for profile in profiles:
        password = get_wifi_password(profile,encoding)
        if password:
            print(f"SSID: {profile}\nPassword: {password}\n")
        else:
            print(f"SSID: {profile}\nPassword: None or not found\n")

if __name__ == "__main__":
    main()
