# Spoti

## Navigation

- [About](https://github.com/ZeroNiki/Spoti?tab=readme-ov-file#About)
- [Pre-Install](https://github.com/ZeroNiki/Spoti?tab=readme-ov-file#Pre-Install)
- [Install](https://github.com/ZeroNiki/Spoti?tab=readme-ov-file#Install)
- [Usage](https://github.com/ZeroNiki/Spoti?tab=readme-ov-file#Usage)
- [Todo](https://github.com/ZeroNiki/Spoti?tab=readme-ov-file#Todo)

## About

lib:

- yt-dlp
- selenium
- requests
- bs4
- pyfiglet
- wget

Cli-tool for download music from spotify

## Pre-Install

Install selenium driver (geckodriver) from Linux repo:

If your using Arch Linux:
[install](https://archlinux.org/packages/extra/x86_64/geckodriver/)

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

in 'src/spotify.py' add your selenium driver path:

```python
service = Service('/path/to/your/geckodriver') # default /usr/bin/geckodriver
```

in `src/.env` add full path to your music dir

let's start:

## Usage

```sh
python3 spoti [url]
```

or (if you're in linux)

```
chmod +x spoti

./spoti [url]
```

## Todo

- [x] Download Lyrics
- [ ] Download all track from playlist
