# Color Scheme Generator for AwesomeWM.
## ScreenShots

![Mountain wallpaper](/screenshots/mountain.png)

![Galaxy wallpaper](/screenshots/galaxy.png)

![Nasa Image wallpaper](/screenshots/nasa.png)
## Usage

Clone this repo under  ``` ~/.config/awesome/ ``` and enter into this folder.
Edit the file ``` main.py ``` and pass the wallpaper and theme path that you're gonna use.

Then run:
``` python main.py ```
### Optional:
If you don't like the color scheme generated, you always can use the negative colors, changing the last parameter on the function ``` cc.extractColors() ``` from ``` False ``` to ``` True ```

As the default ``` theme.lua ``` generates the wallpaper through a function, I do recommend you checking the way in which it sets the wallpaper in the file ``` themeEditor.py ``` to prevent any error.

## Dependencies

```
python > 3.6
PIL (python library)

```

## How it works?

### Color Selection:
Here we use a
[K-means clustering](http://google.com)
for finding and selecting the colors from the image and return it sorted in an array.
### Editing the theme:
Actually, it's very simple. Manually we pass the theme's variables to edit, and store it in an array according to it's contrast. For example:
``` theme.bg_normal ```(the bar's color) and ``` theme.fg_normal ``` (the font's color) must contrast, we store ``` theme.bg_normal ``` on the first possition of the array and the ``` theme.bg_normal ``` on the last one.
Then the whole array will be matched with the color's array and the theme file will be edited.
