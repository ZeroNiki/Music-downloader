# Spoti

lib:

- yt-dlp
- selenium
- requests
- bs4
- pyfiglet

Other tools:

- wget

Cli-tool for download music from spotify

## Pre-install

Install `wget` from your package manager

## Install

clone this repository:

```sh
git clone https://github.com/ZeroNiki/Spoti.git
```

```sh
cd Spoti
```

create virtual env:

```sh
python3 -m venv venv
```

```sh
source venv/bin/activate
```

install requirements:

```sh
pip install -r requirements.txt
```

## Start

in `src/.env` add full path to your music dir

let's start:

```sh
python3 start.py
```

## Usage

just copy link to track and paste:

```
Spotify link:
<paste link here>
```

## Todo

- [ ] Download all track from playlist
