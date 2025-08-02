import asyncio
import shlex
import os
from typing import Tuple

# Set Git executable path explicitly for Heroku before importing git module
os.environ["GIT_PYTHON_GIT_EXECUTABLE"] = "/usr/bin/git"
os.environ["GIT_PYTHON_REFRESH"] = "quiet"

from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError

import config
from ..logging import LOGGER


def install_req(cmd: str) -> Tuple[str, str, int, int]:
    async def install_requirements():
        args = shlex.split(cmd)
        process = await asyncio.create_subprocess_exec(
            *args,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        return (
            stdout.decode("utf-8", "replace").strip(),
            stderr.decode("utf-8", "replace").strip(),
            process.returncode,
            process.pid,
        )

    return asyncio.get_event_loop().run_until_complete(install_requirements())


def git():
    # Validate UPSTREAM_REPO format when using GIT_TOKEN
    REPO_LINK = config.UPSTREAM_REPO
    if config.GIT_TOKEN:
        try:
            GIT_USERNAME = REPO_LINK.split("com/")[1].split("/")[0]
            TEMP_REPO = REPO_LINK.split("https://")[1]
            UPSTREAM_REPO = f"https://{GIT_USERNAME}:{config.GIT_TOKEN}@{TEMP_REPO}"
        except IndexError:
            LOGGER(__name__).error("Invalid UPSTREAM_REPO format")
            return False
    else:
        UPSTREAM_REPO = config.UPSTREAM_REPO

    try:
        # Try to initialize the repo
        try:
            repo = Repo()
            LOGGER(__name__).info("Git Client Found [VPS DEPLOYER]")
            return True
        except (InvalidGitRepositoryError, NoSuchPathError):
            # Initialize new repo if none exists
            repo = Repo.init()
            LOGGER(__name__).info("Initialized new Git repository")

        # Configure remote
        if "origin" in repo.remotes:
            origin = repo.remote("origin")
            origin.set_url(UPSTREAM_REPO)
        else:
            origin = repo.create_remote("origin", UPSTREAM_REPO)

        # Fetch updates
        origin.fetch()
        
        # Configure branch
        if config.UPSTREAM_BRANCH not in repo.heads:
            repo.create_head(
                config.UPSTREAM_BRANCH,
                origin.refs[config.UPSTREAM_BRANCH],
            )
        
        repo.heads[config.UPSTREAM_BRANCH].set_tracking_branch(
            origin.refs[config.UPSTREAM_BRANCH]
        )
        repo.heads[config.UPSTREAM_BRANCH].checkout(True)

        # Pull updates
        try:
            origin.pull(config.UPSTREAM_BRANCH)
        except GitCommandError as pull_error:
            LOGGER(__name__).warning(f"Pull failed, resetting: {pull_error}")
            repo.git.reset("--hard", "FETCH_HEAD")

        # Install requirements
        install_result = install_req("pip3 install --no-cache-dir -r requirements.txt")
        if install_result[2] != 0:  # Check return code
            LOGGER(__name__).error(f"Requirements installation failed: {install_result[1]}")
            return False

        LOGGER(__name__).info("Successfully fetched updates from upstream repository")
        return True

    except Exception as e:
        LOGGER(__name__).error(f"Git operation failed: {str(e)}")
        return False
