# Spoti

## Navigation

- [About](https://github.com/ZeroNiki/Spoti?tab=readme-ov-file#About)
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

- [ ] Download all track from playlist
