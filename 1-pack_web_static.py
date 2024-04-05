#!/usr/bin/python3
"""
In this script I'll be writting a fabric script which will be generating
a .tgz archive from the contents of the web_static folder of my air bnb
clone using a function called do_pack
"""
from fabric.api import local
from datetime import datetime

def do_pack():
    """
    This function generates a .tgz archive from the contents of the web_static
    folder of the AirBnB Clone repository.
    
    All files in the folder web_static are added to the final archive.
    All archives are stored in the folder versions (this function creates
    this folder if it doesn’t exist).
    The name of the archive created follows the format:
    web_static_<year><month><day><hour><minute><second>.tgz
    
    Returns:
        (str): The archive path if the archive has been correctly generated,
        otherwise, None.
    """
    try:
        # Create the versions folder if it doesn't exist
        local("mkdir -p versions")

        # Generate the current timestamp
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")

        # Create the .tgz archive
        archive_name = "web_static_{}.tgz".format(timestamp)
        local("tar -czvf versions/{} web_static".format(archive_name))

        # Return the archive path
        return "versions/{}".format(archive_name)
    except Exception as e:
        print("Error:", e)
        return None
