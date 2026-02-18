"""Import necessary libraries and define functions for secure file transfer via SFTP."""
import os
import sys
import paramiko

def get_server1_credentials():
    """Retrieve SERVER1 credentials from environment variables."""
    host = os.getenv('ALFA_HOST')
    user = os.getenv('ALFA_USER')
    password = os.getenv('ALFA_PWD')
    
    if not all([host, user, password]):
        print("Missing environment variables for SERVER1 (ALFA_HOST, ALFA_USER, ALFA_PASSWORD)")
        return None
    
    return host, user, password


def get_server2_credentials():
    """Retrieve SERVER2 credentials from environment variables."""
    host = os.getenv('SHINY_HOST')
    user = os.getenv('SHINY_USER')
    password = os.getenv('SHINY_PWD')
    
    if not all([host, user, password]):
        print("Missing environment variables for SERVER2 (SHINY_HOST, SHINY_USER, SHINY_PASSWORD)")
        return None
    
    return host, user, password


def transfer_file_via_sftp(host, username, password, local_file, remote_path, server_name):
    """
    Establish SSH connection, transfer file via SFTP, and close connection.
    
    Args:
        host: Server hostname/IP
        username: SSH username
        password: SSH password
        local_file: Path to local file to transfer
        remote_path: Remote destination path (include filename)
        server_name: Name of server (for logging)
    
    Returns:
        True if successful, False otherwise
    """
    ssh_client = None
    sftp_client = None
    
    # First verify local file exists
    if not os.path.exists(local_file):
        print(f"[{server_name}] Error: Local file '{local_file}' not found")
        return False
    
    try:
        # Create SSH client
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Establish secure connection
        print(f"[{server_name}] Connecting to {host}...")
        ssh_client.connect(
            hostname=host,
            username=username,
            password=password,
            timeout=30,
            look_for_keys=False,
            allow_agent=False
        )
        print(f"[{server_name}] Connection established successfully")
        
        # Open SFTP session
        sftp_client = ssh_client.open_sftp()
        
        # Transfer file
        print(f"[{server_name}] Transferring {local_file} to {remote_path}...")
        sftp_client.put(local_file, remote_path)
        print(f"[{server_name}] File transferred successfully")
        
        return True
    
    except paramiko.AuthenticationException:
        print(f"[{server_name}] Error: Authentication failed for {username}@{host}")
        return False
    except paramiko.SSHException as e:
        print(f"[{server_name}] Error: SSH connection failed - {str(e)}")
        return False
    except Exception as e:
        print(f"[{server_name}] Error: {str(e)}")
        return False
    
    finally:
        # Clean up session data
        if sftp_client:
            sftp_client.close()
            print(f"[{server_name}] SFTP session closed")
        
        if ssh_client:
            ssh_client.close()
            print(f"[{server_name}] SSH connection closed")


def main():
    """Main script execution"""
    
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    season_file = os.path.join(script_dir, 'season25.sqlite')
    
    # Verify file exists before attempting transfer
    if not os.path.exists(season_file):
        print(f"[FATAL] SQL file not found: {season_file}")
        print(f"[INFO] Looking in directory: {script_dir}")
        print(f"[INFO] Directory contents: {os.listdir(script_dir) if os.path.exists(script_dir) else 'Directory not found'}")
        return False
    
    print(f"[INFO] Found season25.sqlite at: {season_file}")
    
    # Define server configurations
    servers = [
        {
            'name': 'SERVER1',
            'get_credentials': get_server1_credentials,
            'local_file': season_file,
            'remote_path': '/html/dist/_file/data/season25.sqlite'
        },
        {
            'name': 'SERVER2',
            'get_credentials': get_server2_credentials,
            'local_file': season_file,
            'remote_path': '/srv/shiny-server/tablas/season25.sqlite'
        }
    ]
    
    # Process each server
    results = []
    for server_config in servers:
        server_name = server_config['name']
        credentials = server_config['get_credentials']()
        
        if not credentials:
            results.append((server_name, False))
            continue
        
        host, user, password = credentials
        success = transfer_file_via_sftp(
            host=host,
            username=user,
            password=password,
            local_file=server_config['local_file'],
            remote_path=server_config['remote_path'],
            server_name=server_name
        )
        results.append((server_name, success))
        print()  # Blank line for readability
    
    # Summary
    print("=" * 50)
    print("Transfer Summary:")
    for server_name, success in results:
        status = "✓ SUCCESS" if success else "✗ FAILED"
        print(f"{server_name}: {status}")
    
    return all(success for _, success in results)


if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)