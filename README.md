# ocrmypdf-doxa-plugin

OCRmyPDF plugin including Δoxa binarization framework

## Features

Binarization using Δoxa's library algorithms (https://github.com/brandonmpetty/Doxa)

## Installation

```sh
pip install .
```

## Usage

```sh
ocrmypdf \
  --plugin ocrmypdf_doxa_plugin/plugin.py \
  --doxa-algorithm WAN \
  --doxa-parameters k=0.2 window=20  \
  -- input.pdf output.pdf
```

`--doxa-parameters` can be omitted and will be defaulted for each algorithm.


## Author

👤 **Tristan Porteries**

* Github: [@panzergame](https://github.com/panzergame)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/panzergame/ocrmypdf-doxa-plugin/issues). 

## Show your support

Give a ⭐️ if this project helped you!

## 📝 License

Copyright © 2020 [Tristan Porteries](https://github.com/panzergame).<br />
This project is [CC0-1.0 License](https://github.com/panzergame/ocrmypdf-doxa-plugin/blob/master/LICENSE.md) licensed.
