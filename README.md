# Water Quality Exchange (WQX) API Wrapper

<!-- TABLE OF CONTENTS -->

## Table of Contents

- [About the Project](#about)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Quick Start](#quick-start)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)

<!-- ABOUT THE PROJECT -->

## About

This library allows you to quickly use the RESTful Web Service Methods provided by [WQX](https://cdx.epa.gov/WQXWeb/StaticPages/WebServicesGuide.htm#tabs-2) without having to worry about configurations.

<!-- GETTING STARTED -->

## Getting Started

### Prerequisites

- Python 3.6, 3.7, or 3.8
- Pip 3
- virtualenv

### Installation

1. Get a Central Data Exchange API Key at [CDX](https://cdx.epa.gov/)

2. Clone the repo

```sh
git clone https://github.com/FlowWest/wqxtools.git
```

3. Create a virtual environment

```sh
virtualenv .env
```

3. Install the Package.

```sh
pip3 install.
```

<!-- USAGE EXAMPLES -->

## Quick Start

```python3
from wqxtools.cdx import CDX

API_KEY = YOUR_API_KEY
USER_ID = YOUR_USER_ID
FILE_PATH = YOUR_FILE_PATH
FILE_NAME = YOUR_FILE_NAME
CONFIG_ID = YOUR_CONFIG_ID

# Create a session instance.
session = CDX(USER_ID, API_KEY, FILE_PATH, FILE_NAME)

# Upload the file and retrieve a file_id
file_id = session.upload()

# using the file_id and config_id start importing the file.
dataset_id = session.start_import(file_id, CONFIG_ID)

# Get status returns the most recent status of the process.
current_status = session.get_status(dataset_id)
```

_For more details about the endpoints, please refer to the [WQX](<(https://cdx.epa.gov/WQXWeb/StaticPages/WebServicesGuide.htm#tabs-2)>)_

<!-- ROADMAP -->

## Roadmap

See the [open issues](https://github.com/FlowWest/wqxtools/issues) for a list of proposed features (and known issues).

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->

## Contact

Celestino Salim - [@celestinosalim](https://twitter.com/celestinosalim) - csalim@flowwest.com

Emanuel Rodriguez - [@ergz]() - erodriguez@flowwest.com

Project Link: [https://github.com/FlowWest/wqxtools](https://github.com/FlowWest/wqxtools)

<!-- ACKNOWLEDGEMENTS -->

## Acknowledgements

- [Requests](https://requests.readthedocs.io/en/master/)
- [Pandas](https://pandas.pydata.org/)
