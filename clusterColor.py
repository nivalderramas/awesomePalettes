from PIL import Image
from math import sqrt
import random


class Point:
    def __init__(self, coordinates):
        self.coordinates = coordinates


class Cluster:
    def __init__(self, center, points):
        self.center = center
        self.points = points


class KMeans:
    def __init__(self, n_clusters, minDistance):
        self.n_clusters = n_clusters
        self.minDistance = minDistance

    def calculateCenter(self, points):
        dim = len(points[0].coordinates)
        values = [0.0 for i in range(dim)]
        for point in points:
            for i in range(dim):
                values[i] = values[i] + point.coordinates[i]
        centerCoords = [(v / len(points)) for v in values]
        return Point(centerCoords)

    def assignPoints(self, clusters, points):
        pointLists = [[] for i in range(len(clusters))]
        for p in points:
            minDistance = float("inf")
            for i in range(len(clusters)):
                distance = distancePoints(p, clusters[i].center)
                if minDistance > distance:
                    minDistance = distance
                    index = i
            pointLists[index].append(p)
        return pointLists

    def fit(self, points):
        clusters = [
            Cluster(center=p, points=[p])
            for p in random.sample(points, self.n_clusters)
        ]

        while True:

            plists = self.assignPoints(clusters, points)
            diff = 0
            for i in range(self.n_clusters):
                if not plists[i]:
                    continue
                old = clusters[i]
                center = self.calculateCenter(plists[i])
                new = Cluster(center, plists[i])
                clusters[i] = new
                diff = max(diff, distancePoints(old.center, new.center))
            if diff < self.minDistance:
                break
        return clusters


def getPoints(path):
    img = Image.open(path)
    w, h = img.size
    img.thumbnail((int(w * 0.1), int(h * 0.1)))
    img = img.convert("RGB")
    points = []
    w, h = img.size
    for count, color in img.getcolors(w * h):
        for _ in range(count):
            points.append(Point(color))
    return points


def distancePoints(p1, p2):
    dim = len(p1.coordinates)
    temp = 0
    for i in range(dim):
        temp = temp + pow((p1.coordinates[i] - p2.coordinates[i]), 2)
    temp = sqrt(temp)
    return temp


def rgbToHex(rgb):
    return "#%s" % "".join(("%02x" % p for p in rgb))


def invertRgb(rgb):
    rgb = list(rgb)
    for i in range(len(rgb)):
        rgb[i] = 255 - rgb[i]
    return rgb


def extractColors(filename, nColors, minDistance, invert=False):
    points = getPoints(filename)
    clusters = KMeans(nColors, minDistance).fit(points)
    clusters.sort(key=lambda c: len(c.points), reverse=True)
    rgbs = [map(int, c.center.coordinates) for c in clusters]
    if invert:
        rgbs = list(map(invertRgb, rgbs))
    rgbs = sorted(list(map(rgbToHex, rgbs)), reverse=False)
    return rgbs


# colors = extractColors("./img/wallpaper3.png",3,2,True)
# print(colors)
