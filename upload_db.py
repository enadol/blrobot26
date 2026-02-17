import os
import paramiko
import sys

def upload_file(host, user, password, local_file, remote_path):
    print(f"Connecting to {host}...")
    try:
        transport = paramiko.Transport((host, 22))
        transport.connect(username=user, password=password)
        sftp = paramiko.SFTPClient.from_transport(transport)

        # Create remote directory if it doesn't exist
        try:
            sftp.chdir(remote_path)
        except IOError:
            print(f"Remote directory {remote_path} not found. Attempting to create...")
            # Simple recursive creation not implemented, assuming one level deep or existing structure
            # For robust recursive creation we'd need more logic, but let's try direct put to path
            # or creating the final directory.
            # Paramiko doesn't have mkdir -p. 
            # Let's try to just put the file to the full path if directory structure is assumed 
            # or try to make the specific directory.
            try:
                sftp.mkdir(remote_path)
                sftp.chdir(remote_path)
            except IOError:
                print(f"Error: Could not access or create remote directory {remote_path}")
                return False

        print(f"Uploading {local_file} to {remote_path}...")
        sftp.put(local_file, os.path.basename(local_file))
        print("Upload successful.")
        sftp.close()
        transport.close()
        return True
    except Exception as e:
        print(f"Failed to upload to {host}: {e}")
        return False

def main():
    db_file = "season25.sqlite"
    if not os.path.exists(db_file):
        print(f"Error: Database file {db_file} not found.")
        return

    # Server 1
    s1_host = os.environ.get("ALFA_HOST")
    s1_user = os.environ.get("ALFA_USER")
    s1_pass = os.environ.get("ALFA_PASS")
    s1_path = os.environ.get("ALFA_PATH")

    if s1_host and s1_user and s1_pass and s1_path:
        print(f"\n--- Server 1 ({s1_host}) ---")
        upload_file(s1_host, s1_user, s1_pass, db_file, s1_path)
    else:
        print("Skipping Server 1: Missing environment variables (ALFA_*)")

    # Server 2 Path 1
    s2_host = os.environ.get("SHINY_HOST")
    s2_user = os.environ.get("SHINY_USER")
    s2_pass = os.environ.get("SHINY_PASS")
    s2_path1 = os.environ.get("SHINY_PATH_1")
    s2_path2 = os.environ.get("SHINY_PATH_2")

    if s2_host and s2_user and s2_pass:
        if s2_path1:
            print(f"\n--- Server 2 Path 1 ({s2_host}) ---")
            upload_file(s2_host, s2_user, s2_pass, db_file, s2_path1)
        
        if s2_path2:
            print(f"\n--- Server 2 Path 2 ({s2_host}) ---")
            upload_file(s2_host, s2_user, s2_pass, db_file, s2_path2)
    else:
         print("Skipping Server 2: Missing environment variables (SHINY_*)")

if __name__ == "__main__":
    main()
