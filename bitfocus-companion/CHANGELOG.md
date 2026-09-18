## 0.4.7

- Updated Bitfocus Companion to v5.0.6.

## 0.4.6

- Updated Bitfocus Companion to v5.0.5.

## 0.4.5

- Updated Bitfocus Companion to v5.0.4.

## 0.4.4

- Updated Bitfocus Companion to v5.0.3.

## 0.4.3

- Mount the Home Assistant `share` directory read-only at `/share` so Companion modules can read shared files.

## 0.4.2

- Updated Bitfocus Companion to v5.0.2.

## 0.4.1

- Normalize the startup script to Unix line endings during the image build.

## 0.4.0

- Updated Bitfocus Companion to v5.0.1.

## 0.3.1
Updated Companion docker image to v4.3.4

## 0.3.0
- Updated Companion docker image to v4.2.5
- Added custom UDP and TCP listeners:
  - 12321/udp: "OSC Listener"
  - 7788/tcp: "RossTalk Listener"
  - 9092/tcp: "Ember+ Listener"
  - 6454/udp: "Art-Net / Art-Net II"
  - 9990/tcp: "Videohub Panel Listener"  

## 0.2.9
Updated Companion docker image to v4.2.4

## 0.2.8
Updated Companion docker image to v4.2.2

## 0.2.7
Bugfix: reworked add-on startup to prevent Node.js permission errors in Companion modules
- /data/companion is now used as the actual config base directory:
- Companion and its modules now operate on a real directory, not a symlink.
- This avoids Node.js permission checks failing on /companion.
- The add-on remains compatible with Home Assistant’s persistent /data storage model.

## 0.2.6
Updated Companion docker image to v4.2.1

## 0.2.5
Updated Companion docker image to v4.1.4

## 0.2.4
Updated Companion docker image to v4.1.3

## 0.2.3.1
Updated Companion docker image to v4.1.1
- bugfix

## 0.2.3
Updated Companion docker image to v4.1.1

## 0.2.2
Updated Companion docker image to v4.0.3

## 0.2.1
Updated Companion docker image to v4.0.2
7
