import os
def editTheme(themePath, colors, themeVariables,wallpaperPath):
    themeFile = open(themePath)
    numberColors = len(themeVariables)
    tmpTheme = open("tmpTheme.lua","w")
    for line in themeFile:
        lineWritten = False
        line = line.split()
        for i in range(numberColors):
            try:
                #Search for theme Variables to change, if exists then update it
                idx = line.index(themeVariables[i])
                if idx==0:
                    line[2] = '"' + colors[i] + '"'
                    lineWritten = True
                    tmpTheme.write(" ".join(line))
                    tmpTheme.write("\n")
            except ValueError:
                pass
        if not lineWritten:
            if len(line)!=0 and line[0] == "theme.wallpaper":
                line [2] = '"'+wallpaperPath+'"'
            tmpTheme.write(" ".join(line))
            tmpTheme.write("\n")
    tmpTheme.close()
    themeFile.close()
    os.rename("tmpTheme.lua",themePath)
#colors=["#000000"]*5
#themeVariables = ["theme.fg_normal","theme.bg_normal","theme.bg_focus","theme.bg_urgent","theme.bg_minimize"]
#editTheme("themeExample.lua",colors,themeVariables)
