# dial-basic-nodes
Basic nodes for DL tasks, used by the Dial app.

## Documentation

This project's documentation lives at [readthedocs.io](https://dial-basic-nodes.readthedocs.io)

## License

All code is provided under the __GPL-3.0__ license. See [LICENSE](LICENSE) for more details.

## Authors

* **David Afonso (davafons)**: [Github](https://github.com/davafons) [Twitter](https://twitter.com/davafons)
	* dial-core
	* dial-gui
	* dial-basic-nodes

* **Javier Duque Melguizo**: [Github](https://github.com/JDM-ULL-93)
	* dial-Visualization

## Installation

To install modules

```bash

py install.py 
```

To execute app:

```bash
py main.py
```

To uninstall modules installed on install phase:

```bash
py clean.py
```


## Configuration

* On Linux: Go to ~/dial/plugins
* On Windows: Go to %userprofile%\AppData\Local\dial\plugins

And set up **plugins.json** like so:
```json
{
  "dial-basic-nodes": {
    "version": "0.8a0",
    "summary": "Basic nodes for the Dial app.",
    "active": true
  },
  "dial-visualization": {
    "version": "0.2a0",
    "summary": "Visualization techniques for CNN.",
    "active": true
  }
}
```

So nodes from dial-basic-nodes (to load convolutional neural network) and dial-visualization  (to execute visualization techniques on convolutional neural network) are loaded into the application.


### Configuration on Development Mode

Dial-App supports a special mode so you can work with not configured python packages (no setup.py or pyproject.toml created) :

```json
{
  "dial-basic-nodes": {
    "version": "0.8a0",
    "summary": "Basic nodes for the Dial app.",
    "active": true
  },
  "dial-visualization": {
    "version": "0.2a0",
    "summary": "Visualization techniques for CNN.",
    "active": true,
	"path": "<path_to>/dial-visualization/dial_visualization"
  }
}
```

By adding 'path' entry, dial_visualization python code will be lodead inside program memory to work with. No actual "dial-visualization" package is created.

