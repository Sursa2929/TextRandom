<p align="center">
  <img src="https://telegra.ph/file/d856ca30ffe9d6f4d1436.jpg" alt="BISHNOI Logo">
</p>


![Typing SVG](https://readme-typing-svg.herokuapp.com/?lines=Welcome+To+Surya+bishnoi+Text-Bot;A+Highly+Advance+Url+Uploader+Bot;Made+By+SURYA+BISHNOI+Love+❤️+B!;Must+Give+Credit+To+Surya+Bishnoi+Love+❤️+B;Thank+You!)
</p>
# Deploy To Heroku

[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Sursa2929/TextRandom)


```Credit By SURYA BISHNOI love ❤️ B```



{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "gpuType": "T4",
      "authorship_tag": "ABX9TyP5q8u3V4pXGQIwac7/iNWE",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    },
    "accelerator": "GPU"
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Sursa2929/TextRandom/blob/main/TextRandom.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "import shutil\n",
        "from IPython.display import clear_output\n",
        "\n",
        "#@title <h1><B><font color=red>TextRandom</B>\n",
        "# @markdown <div><center><a href=\"https://github.com/Sursa2929/TextRandom\"><img height=\"100\"  src=\"https://opengraph.githubassets.com/9s29ytrymhlrsfu1tqt1pzdxyfcsjeea/Sursa2929/TextRandom\"></center></a></div>\n",
        "# @markdown <br><center><h2><strong><font color=red>TextRandom</strong></h2></center>\n",
        "\n",
        "\n",
        "# GitHub repository URL\n",
        "GITHUB_URL = \"https://github.com/Sursa2929/TextRandom.git\"  # Updated URL\n",
        "BRANCH_NAME = \"v1.2-GC\"  # Specify the branch name\n",
        "\n",
        "# Base directory for cloning\n",
        "base_dir = './repo'  # Save repo in ./repo directory relative to current directory\n",
        "\n",
        "# Function to clone or update the repository\n",
        "def clone_or_update_repo(repo_url, base_directory, branch_name):\n",
        "    repo_name = os.path.basename(repo_url).replace('.git', '')\n",
        "    project_dir = os.path.join(base_directory, repo_name)\n",
        "\n",
        "    # Check if the repository directory exists\n",
        "    if os.path.exists(project_dir):\n",
        "        print(f\"Deleting existing repository at: {project_dir} ...\")\n",
        "        shutil.rmtree(project_dir)\n",
        "        print(\"Deleted existing repository successfully!\")\n",
        "\n",
        "    # Clone the repository from a specific branch\n",
        "    print(f\"Cloning repository from {repo_url} (branch: {branch_name})...\")\n",
        "    clone_cmd = f\"git clone -b {branch_name} {repo_url} {project_dir}\"\n",
        "    os.system(clone_cmd)\n",
        "    print(\"Repository cloned successfully!\")\n",
        "\n",
        "    return project_dir\n",
        "\n",
        "# Clone or update the repository\n",
        "project_dir = clone_or_update_repo(GITHUB_URL, base_dir, BRANCH_NAME)\n",
        "\n",
        "# Navigate to the project directory\n",
        "try:\n",
        "    print(f\"Entering project directory: {os.path.basename(project_dir)}...\")\n",
        "    os.chdir(project_dir)\n",
        "    print(\"Entered project directory successfully!\")\n",
        "except FileNotFoundError as e:\n",
        "    print(f\"Error: {e}\")\n",
        "    raise\n",
        "\n",
        "clear_output()\n",
        "\n",
        "# Install required dependencies\n",
        "PIP_INSTALL = \"requirements.txt\"  # Path to requirements file\n",
        "print(\"Installing required dependencies...\")\n",
        "!pip install -r {PIP_INSTALL}\n",
        "print(\"All requirements installed successfully!\")\n",
        "\n",
        "clear_output()\n",
        "\n",
        "# Install FFMPEG\n",
        "install_ffmpeg = \"Yes\"  # Prompt for FFMPEG installation\n",
        "if install_ffmpeg == \"Yes\":\n",
        "    print(\"Installing FFMPEG...\")\n",
        "    os.system(\"apt-get install ffmpeg -qq\")  # Install ffmpeg quietly\n",
        "    print(\"FFMPEG installed successfully!\")\n",
        "else:\n",
        "    print(\"Skipping FFMPEG installation.\")\n",
        "\n",
        "#@markdown ### <font color=ORANGE>Environment Variables\n",
        "\n",
        "API_ID = \"\"  #@param {type:\"string\"}\n",
        "os.environ['API_ID'] = API_ID\n",
        "\n",
        "API_HASH = \"\"  #@param {type:\"string\"}\n",
        "os.environ['API_HASH'] = API_HASH\n",
        "\n",
        "BOT_TOKEN = \"\"  #@param {type:\"string\"}\n",
        "os.environ['BOT_TOKEN'] = BOT_TOKEN\n",
        "\n",
        "#@markdown\n",
        "PORT = \"8800\"  #@param {type:\"string\"}\n",
        "os.environ['PORT'] = PORT\n",
        "\n",
        "clear_output()\n",
        "\n",
        "\n",
        "# Command to run the bot\n",
        "RUN_COMMAND = \"python3 modules/main.py\"  # Path to your main script\n",
        "print(f\"Running command: {RUN_COMMAND} ...\")\n",
        "!{RUN_COMMAND}\n",
        "print(\"Execution completed!\")\n"
      ],
      "metadata": {
        "cellView": "form",
        "id": "DWy3KUYwpdcx"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
