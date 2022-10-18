# ColorToner

Glyphs.app plug-in for darkening shapes in Edit view. For now it only supports darkening components. Useful if you use a canvas color that makes the components disappear.

In the future, may support more color tweaks. Let me know if you need something special.

## Usage

Choose *View > Show Darkened Colors* (de: *abgedunkelte Farben*), and the shapes will be rendered with an extra 15% black.

To change the amount of darkening, run this code in Macro Window:

```python
Glyphs.defaults["com.mekkablue.ColorToner.darken"] = 0.15
```

Replace `0.15` with the amount you want instead. Maximum (full black) is `1.0`, the minimum (no change) is `0.0`.


## Installation

Color Toner is available in the Glyphs&nbsp;3 Plugin Manager, accessible via `glyphsapp3://showplugin/Color%20Toner%20(Show%20Darkened%20Colors)`. Click on the *Install* button next to it and restart Glyphs.


## Requirements

The plug-in works in Glyphs 3.1 and later.


# License

Copyright 2022 Rainer Erich Scheichelbauer (@mekkablue). Based on template code by Georg Seifert (@schriftgestalt) and Jan Gerner (@yanone).

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

See the License file included in this repository for further details.
