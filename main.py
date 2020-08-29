import clusterColor as cc
import themeEditor as te

wallpaperPath = "/home/nico/.config/awesome/wallpapers/galaxy.jpg"
themePath = "../themeTest.lua"
themeVariables = [
    "theme.bg_normal",
    "theme.bg_focus",
    "theme.bg_urgent",
    "theme.bg_minimize",
    "theme.fg_normal",
]
baseColors = len(themeVariables)
colors = cc.extractColors(wallpaperPath, baseColors, 1, False)
te.editTheme(themePath, colors, themeVariables, wallpaperPath)
