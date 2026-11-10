# TikTokLive-Gift Bot

> **Note:** this project does **not** give free TikTok coins, gifts or followers.
> It only reacts to gifts that viewers send on **your own** TikTok live stream.

A small Python script that connects to a TikTok live stream and presses a key every time a gift is received. Streamers can use it to trigger an action in a game or app whenever a viewer sends a gift.

Built in 2022 for a streamer, on top of the [TikTokLive](https://github.com/isaackogan/TikTokLive) library.

## How it works

1. The script asks for the TikTok username of the stream to watch.
2. It connects to that live stream with `TikTokLive`.
3. Whenever a gift arrives (for gift streaks, once the streak ends), it prints who sent what and presses the **Up arrow** key using `pynput`.

## Installation

Requires Python 3.

```bash
git clone https://github.com/benioriginal/TikTokLive-Gift.git
cd TikTokLive-Gift
pip install -r requirements.txt
```

## Usage

```bash
python script.py
```

Enter the TikTok username (without `@`) of a stream that is currently live. Keep the window you want to control focused, since the key press goes to the active window.

## Customizing

The action lives in the `on_gift` function in `script.py`. Replace the `keyboard.press(Key.up)` / `keyboard.release(Key.up)` lines with any key, or call your own function instead. You can also check `event.gift.extended_gift.name` to react differently to specific gifts.

## Note on TikTokLive versions

This script was written for an older version of `TikTokLive`. Newer versions of the library changed their event API, so you may need to pin an older version or update the event handlers.
