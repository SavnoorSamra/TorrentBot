<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->




<h3 align="center">Torrent Bot</h3>


<!-- TABLE OF CONTENTS -->
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>




<!-- ABOUT THE PROJECT -->
## About The Project
Want to be able to view the download status of your torrents in discord? Now you can with this simple bot!

<!-- GETTING STARTED -->
## Getting Started

You may either run this bot in a docker container using the provided DOCKERFILE or run it "bare-metal" by manually installing the following prerequisites.

### Prerequisites
If Using docker:
Install docker engine https://docs.docker.com/engine/install/

If NOT using docker,
Install the following packages:
* python
  ```sh
  sudo apt install python3
  ```
* python discord library
  ```sh
  pip install discord
  ```
* dotenv
  ```sh
  pip install python-dotenv
  ```

### Installation

1. Login at [https://discord.dev](https://discord.dev)
2. Create a new application and note down the Token in the "BOT" page found in the left sidebar
   1. (Feel free to give your bot a cool profile picture while in here too!)
3. Enable Presence Intent, Server Members Intent, and Message Content Intent.
4. On the OAuth2 page, scroll down to the OAuth2 URL Generator and check the box for "bot" and check off the following boxes. Copy the generated link into a browser and add the bot to your server.![img.png](/img/permissions.png)

5. Clone the repo
  ```sh
   git clone https://github.com/SavnoorSamra/TorrentBot.git
   ```
   
6. Create a file in the root of the repo named ".env" and fill in the following information in the format shown below where
   ```sh
   DISCORD_TOKEN=XXXXXXXXXXXXXXXXXXXX
   username=XXX
   password=XXX
   host=XXX.XXX.XXX.XXX
   port=XXXX
   ```
* DISCORD_TOKEN = The token obtained in step 2
* username = The username of your qBittorrent server
* password = The password of your qBittorrent server
* host = The host IP of your qBittorrent server
* port = The port on which the webUI of your qBittorrent server runs

7. Run main.py
   ```sh
   python3 main.py
   ```

<!-- USAGE EXAMPLES -->
## Usage

There are two commands to view the status of your downloads
* /downloading
  * Shows all currently downloading torrents
* /all
  * Shows all torrents currently in qBittorrent

If using sonarr and/or radarr, torrents are also sorted by category.

<!-- CONTACT -->
## Contact

Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - email@email_client.com

Project Link: [https://github.com/github_username/repo_name](https://github.com/github_username/repo_name)


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()
