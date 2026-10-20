<p align="center">
  <img src="docs/images/icon.svg" width="112" height="112" alt="Forge TV icon">
</p>

<h1 align="center">Forge TV</h1>

<p align="center">
  <b>Live TV, a proper guide, movies and live scores, all on one remote.</b><br>
  A fast IPTV player for Android TV that works with your own M3U or Xtream Codes playlist.
</p>

<p align="center">
  <a href="https://github.com/tomdonegan/forge-standalone-releases/releases"><b>⬇ Download the latest APK</b></a> · <a href="https://tomdonegan.github.io/forge-standalone-releases/"><b>Website</b></a>
</p>

![Forge TV: live TV, a proper guide, movies and live scores, all on one remote](docs/images/hero.png)

## Why Forge TV

- **Built for the remote.** Every screen is designed for a TV: clear focus, one press to watch, and a guide that feels like a real set-top box.
- **Quick, even on slow boxes.** Channels start on the first decodable frame, the guide opens straight away from what is saved on the TV, and it runs on TVs as old as Android 6.
- **Everything stays on your TV.** Playlists, logins, favourites and guide data are stored on the device, and each channel plays straight from your provider.

## A look around

| | |
|---|---|
| ![Home: pick up right where you left off](docs/images/home.png) | ![TV guide: a time grid with a now line](docs/images/guide.png) |
| ![Live sports: scores beside the match](docs/images/live-sports.png) | ![Movies and TV shows as rows of posters](docs/images/movies.png) |

<details>
<summary><b>Settings screenshots</b></summary>

| | |
|---|---|
| ![Settings: bring your own playlists](docs/images/settings-playlists.png) | ![Playlist details: your account at a glance](docs/images/settings-account.png) |
| ![Guide settings: grid or Now and next](docs/images/settings-guide.png) | ![Playback: tuned for fast channel changes](docs/images/settings-playback.png) |
| ![Sports settings: one switch for the sports screen](docs/images/settings-sports.png) | |

</details>

## Features

### 📺 Live TV and guide
- Time-grid guide with a "now" line, or a simpler Now and next view.
- Categories, favourites, recently watched, and channel and programme search.
- Programme listings from your playlist's XMLTV guide, refreshed in the background.
- Number keys, Channel ±, Last channel and an info banner, just like a normal TV.
- Rename, hide, reorder and lock channels and categories, and keep those changes when the playlist refreshes.

### 🏠 Home screen
- What's on now beside a live preview, with one press to watch.
- Continue watching, Favourite channels and Recently watched rows, ready as soon as the app opens.

### ⚽ Live sports
- When a match is on, the picture shrinks to make room for live scores, scorers and the rest of the league.
- Match statistics along the bottom: possession, shots, corners and more.
- **Score delay** holds results back so the scores don't spoil what you haven't seen yet. Tune it with the coloured buttons, or let Auto follow the stream.
- Football across the UK, Europe and beyond, plus basketball, American football, baseball, ice hockey, rugby, tennis, golf, motor racing, cricket and more.

### 🎬 Movies and TV shows
- Your provider's library as rows of posters: recently added, new releases, top rated and every category.
- Details pages with synopsis, resume or start over, and the next episode playing automatically.
- Audio and subtitle track choice, skip back 10 s and forward 30 s.

### 📱 Phone companion
- Pair a phone by scanning a QR code on the TV. There is no app to install; it opens in the phone's browser.
- Add playlists, change settings, reorder favourites and show or hide categories from the phone instead of typing with the remote.
- Pairing uses a code shown only on the TV screen, and paired phones can be unlinked at any time.

### 🖐 Touch, mouse and VR
- Works on phones and tablets by touch: swipe to change channel, brightness and volume, pinch to fill the screen.
- Runs on Meta Quest, Android XR and Pico headsets, where the controller trigger or a hand pinch acts as a tap.

### 👪 Profiles and parental controls
- Profiles each keep their own favourites, recently watched and Continue watching.
- Optional "Who's watching?" when the app opens.
- A parental PIN locks whole categories out of the guide, search and channel changes.

### ⚡ Playback that keeps going
- Tuned for quick channel changes, with a choice of start-up buffer (Fast, Balanced or Steady).
- A dropped stream reconnects by itself, and straight away when the network comes back.
- Playback details on screen (formats, decoder, dropped frames, buffer) for diagnosing jerky video.

## Install

1. Open the [Releases page](https://github.com/tomdonegan/forge-standalone-releases/releases) and download `forge-tv-standalone-<version>.apk` from the newest release.
2. Get the APK onto your device, for example with a downloader app on the TV, a USB stick, or `adb install forge-tv-standalone-<version>.apk` from a computer.
3. Allow your device to install apps from that source when Android asks ("Install unknown apps").
4. Open Forge TV and add your playlist: an M3U/M3U8 link, an M3U file, or an Xtream Codes login. You can type it on the TV or send it from your phone.

### Updates

Forge TV checks this page for new versions a few seconds after it opens and offers **Update now**, **Later** or **Skip this version**. Updates download and install from inside the app, so you only sideload once. The check can be turned off, or run by hand, in **Settings › About**.

## Supported devices

- Android TV and Google TV boxes, sticks and televisions running **Android 6.0 or later**.
- Android phones and tablets, with touch and mouse.
- Meta Quest, Android XR and Pico headsets, where the app runs in a panel.

## Bring your own playlist

Forge TV is a player only. **It does not include, sell or provide any channels, streams or content.** You need your own M3U playlist or Xtream Codes login from a service you are entitled to use, and you are responsible for what you play with it.

---

<sub>This repository hosts the release builds of Forge TV. The app reads this repository's releases to find its updates, so release files keep their names.</sub>
