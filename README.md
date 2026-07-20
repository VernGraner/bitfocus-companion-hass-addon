# Bitfocus Companion Home Assistant Add-on

This fork tracks stable Bitfocus Companion releases automatically. A scheduled
GitHub Actions workflow checks upstream every six hours, pins the verified
`amd64` and `aarch64` container digests, and increments the Home Assistant
add-on version so Home Assistant can offer the update.

This setup allows you to run Companion directly within Home Assistant. It integrates smoothly with the Stream Deck Companion plugin and is likely compatible with Companion Satellite as well.

## Installation

    Open Home Assistant.

    Go to Add-ons.

    Click the button to add a new repository.

    Click the three dots in the upper right corner and select Repositories.

    Add this link:
    https://github.com/VernGraner/bitfocus-companion-hass-addon

    Click Save.

    Install the Companion add-on and start hosting Bitfocus Companion!

## Getting started

    Create a Companion button on a Stream Deck page.

    Click "Open Companion Plugin General Configuration".

    Enter the IP address of your Home Assistant instance to connect.
    
    
## Troubleshooting

Apparently, the add-on may cause problems with other add-ons that use USB devices plugged into the device running HassOS.
To work around this issue:

    Stop the other add-on(s) that use a USB device
    
    Restart the Companion add-on
    
    Then restart the other add-on(s)
