# File: stoxus_jupiterhub.py

import os
import subprocess
import json
from datetime import datetime
from tornado.ioloop import IOLoop
from jupyterhub.app import JupiterHub
from jupyterhub.spawner import LocalProcessSpawner
from oauthenticator.github import GitHubOAuthenticator

# Configuration for JupiterHub
class StoxusJupiterHub:
    def __init__(self):
        self.config = {
            "hub_ip": "0.0.0.0",
            "hub_port": 8000,
            "ssl_cert": "/etc/jupiterhub/ssl/cert.pem",
            "ssl_key": "/etc/jupiterhub/ssl/key.pem",
            "authenticator": {
                "type": "GitHubOAuthenticator",
                "client_id": os.getenv("GITHUB_CLIENT_ID", "your-client-id"),
                "client_secret": os.getenv("GITHUB_CLIENT_SECRET", "your-client-secret"),
                "oauth_callback_url": os.getenv("OAUTH_CALLBACK_URL", "https://hub.stoxus.com/hub/oauth_callback"),
                "admin_users": {"admin1", "admin2"},
            },
            "idle_culler": {
                "enabled": True,
                "timeout_seconds": 3600,
                "cull_interval": 300,
            },
            "user_quota": {
                "cpu": 2,
                "memory": "4G",
                "disk_space": "10G",
            },
            "log_level": "INFO",
        }

    def setup_logging(self):
        log_file = "/var/log/stoxus_jupiterhub.log"
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        with open(log_file, "a") as log:
            log.write(f"\n[{datetime.now()}] JupiterHub Initialized.\n")
        return log_file

    def configure_ssl(self):
        if not os.path.exists(self.config["ssl_cert"]) or not os.path.exists(self.config["ssl_key"]):
            raise FileNotFoundError("SSL certificate or key not found. Ensure paths are correct.")
        print(f"SSL configured with {self.config['ssl_cert']} and {self.config['ssl_key']}.")

    def start_idle_culler(self):
        """Cull idle servers based on configuration."""
        cull_script = "/etc/jupiterhub/cull_idle_servers.py"
        if not os.path.exists(cull_script):
            raise FileNotFoundError(f"Idle culler script not found: {cull_script}")
        subprocess.Popen(
            [
                "python3",
                cull_script,
                f"--timeout={self.config['idle_culler']['timeout_seconds']}",
                f"--cull-interval={self.config['idle_culler']['cull_interval']}",
            ]
        )
        print("Idle culler started.")

    def launch_jupiterhub(self):
        hub = JupiterHub()
        hub.ip = self.config["hub_ip"]
        hub.port = self.config["hub_port"]
        hub.ssl_cert = self.config["ssl_cert"]
        hub.ssl_key = self.config["ssl_key"]
        hub.authenticator_class = GitHubOAuthenticator

        # Configuring authenticator
        authenticator = hub.authenticator
        authenticator.client_id = self.config["authenticator"]["client_id"]
        authenticator.client_secret = self.config["authenticator"]["client_secret"]
        authenticator.oauth_callback_url = self.config["authenticator"]["oauth_callback_url"]
        authenticator.admin_users = self.config["authenticator"]["admin_users"]

        # Set spawner
        spawner = LocalProcessSpawner()
        spawner.mem_limit = self.config["user_quota"]["memory"]
        spawner.cpu_limit = self.config["user_quota"]["cpu"]
        hub.spawner_class = spawner

        print("JupiterHub configured. Starting...")
        IOLoop.current().run_sync(hub.initialize)
        hub.start()

    def run(self):
        try:
            self.setup_logging()
            self.configure_ssl()
            self.start_idle_culler()
            self.launch_jupiterhub()
        except Exception as e:
            print(f"Error starting JupiterHub: {e}")


if __name__ == "__main__":
    hub = StoxusJupiterHub()
    hub.run()