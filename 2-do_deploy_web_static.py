#!/usr/bin/python3
"""
Fabric script to distribute an archive to web servers
"""

from fabric.api import env, put, run, sudo
from os.path import exists

env.hosts = ['<IP web-01>', 'IP web-02']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'

def do_deploy(archive_path):
    """
    Distribute an archive to web servers.

    Args:
        archive_path (str): Path to the archive file to be deployed.

    Returns:
        bool: True if all operations have been done correctly, False otherwise.
    """
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")

        # Extract archive filename without extension
        archive_filename = archive_path.split('/')[-1].split('.')[0]

        # Uncompress the archive to /data/web_static/releases/<archive_filename> on the web server
        run("mkdir -p /data/web_static/releases/{}/".format(archive_filename))
        run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/"
            .format(archive_filename, archive_filename))

        # Delete the archive from the web server
        run("rm /tmp/{}.tgz".format(archive_filename))

        # Delete the symbolic link /data/web_static/current from the web server
        run("rm -rf /data/web_static/current")

        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(archive_filename))

        return True
    except Exception as e:
        print("Error:", e)
        return False
