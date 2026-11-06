# Lanify Docker Image

<!-- Project README scaffold: https://github.com/MRColorR/project-template -->

**Run Lanify with an unofficial Docker image and setup instructions for supported architectures.**

[**🚀 See setup instructions**](#getting-started) · [📚 Documentation](#documentation) · [🫶 Support](#support)

**Leave a star ⭐ if you like this project 🙂 Thank you!**

## Overview

Unofficial [Lanify](https://lanify.ai/) Docker image for easy deployment and management. With multiarch support (x86_64, arm64,...) and auto-updates.

## Getting started

<a name="quick-start-"></a>

### Quick Start

  Go to [2captcha](https://2captcha.com/?from=15765395) or [CapSolver](https://dashboard.capsolver.com/passport/register?inviteCode=0gmGzMUUpLGb) and register to get your API key.
  (Both are referral links using them helps in developement)
  - You can run the Docker container with the appropriate environment variables.
    - Replace `<your_email>` and `<your_password>` with your actual Lanify account credentials:

    ```bash
    docker run -d -e USER=<your_email> -e PASS=<your_password> -e API=<your_api_key> carbon2029/lanify
    ```

## Documentation

<a name="some-random-questions"></a>

### Some random questions

Is it lightweight?
- Hopefully,yes........

Why use 2capcha and CapSolver?
- Well 2Capcha can be free(if you earn credits by solving capchas and use that to pay for api) while CopSolver is cheap if you plan to spend.

## Contributing

Ideas, bug reports, documentation fixes and focused changes are welcome through this repository's collaboration channels.

Please include enough context to reproduce a problem or review a change.

## Support

**🫶 Support the project**

Your contributions are vital in helping to sustain the development of open-source projects and tools made freely available to everyone. If you find value in my work and wish to show your support, kindly consider making a donation.

☕ [Support me on Ko-fi](https://ko-fi.com/mrcolorrain) · 💛 [Donate with cryptocurrency](https://github.com/MRColorR/MRColorR/blob/main/SPONSORS.md#cryptocurrency-wallets)

Thank you for helping me keep building and sharing! 🙏 See the [supporters and sponsors directory](https://github.com/MRColorR/MRColorR/blob/main/SPONSORS.md).

## License

This program is free software distributed under the terms of the GNU General Public License (GPL-3.0). You can redistribute it and/or modify it under the terms of the license. However, there is no warranty provided, and you use it at your own risk.

<a name="disclaimer"></a>

### Disclaimer

This script is provided "as is" and without warranty of any kind.
The author makes no warranties, express or implied, that this script is free of errors, defects, or suitable for any particular purpose.
The author shall not be liable for any damages suffered by any user of this script, whether direct, indirect, incidental, consequential, or special, arising from the use of or inability to use this script or its documentation, even if the author has been advised of the possibility of such damages.
