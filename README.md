# Lanify Docker Image

<!-- Project README scaffold: https://github.com/MRColorR/project-template -->

[Overview](#overview) | [Getting started](#getting-started) | [Documentation](#documentation) | [Contributing](#contributing) | [Support](#support) | [License](#license)

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

Ko-fi supports Mattia / MrColorRain's work across projects.

Support ongoing development, testing and documentation through [Ko-fi](https://ko-fi.com/mrcolorrain). One-time contributions and monthly memberships are welcome, and you can pledge above a tier's minimum.

Your contribution helps me keep building, testing and sharing useful work. Explore the membership benefits on Ko-fi and choose the way you would like to support. Technical decisions remain independent.

See the [supporters and sponsors directory](https://github.com/MRColorR/MRColorR/blob/main/SPONSORS.md) for acknowledgments.

## License

This program is free software distributed under the terms of the GNU General Public License (GPL-3.0). You can redistribute it and/or modify it under the terms of the license. However, there is no warranty provided, and you use it at your own risk.

<a name="disclaimer"></a>

### Disclaimer

This script is provided "as is" and without warranty of any kind.
The author makes no warranties, express or implied, that this script is free of errors, defects, or suitable for any particular purpose.
The author shall not be liable for any damages suffered by any user of this script, whether direct, indirect, incidental, consequential, or special, arising from the use of or inability to use this script or its documentation, even if the author has been advised of the possibility of such damages.
