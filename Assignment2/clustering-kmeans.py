import csv
import math
import numpy as np
import matplotlib.pyplot as plt
import random as rand
from copy import deepcopy


def main():
    kmeans = input("How many clusters? \n")
    ages, gpas = readData()
    writeData(ages, gpas)
    data = convertToXY(ages, gpas)
    values = np.array(list(zip(ages, gpas)))
    plt.scatter(ages, gpas, c='black', s=7)
    k = int(kmeans)
    centroid_x = np.random.randint(0, np.max(values) - 20, size=k)
    centroid_y = np.random.randint(0, np.max(values) - 20, size=k)
    C = np.array(list(zip(centroid_x, centroid_y)), dtype=np.float32)
    centroids = convertCentroidsXY(C, k)
    clusters = pointClusterMembership(data, centroids)
    plt.scatter(ages, gpas, c='#050505', s=7)
    plt.scatter(centroid_x, centroid_y, marker='*', s=200, c='g')
    old_centroids = np.zeros(C.shape)
    clusters = np.zeros(len(values))
    error = dist(C, old_centroids, None)
    counter = 0
    while error != 0:
        for i in range(len(values)):
            distances = dist(values[i], C)
            cluster = np.argmin(distances)
            clusters[i] = cluster
        old_centroids = deepcopy(C)
        for i in range(k):
            points = [values[j] for j in range(len(values)) if clusters[j] == i]
            C[i] = np.mean(points, axis=0)
        error = dist(C, old_centroids, None)
        colors = ['r', 'g', 'b', 'y', 'c', 'm']
        fig, ax = plt.subplots()
        for i in range(k):
            points = np.array([values[j] for j in range(len(values)) if clusters[j] == i])
            ax.scatter(points[:, 0], points[:, 1], s=7, c=colors[i])
        ax.scatter(C[:, 0], C[:, 1], marker='*', s=200, c='#050505')
        if counter == 0:
            plt.savefig('cluster-first-loop.pdf')
            centroids = convertCentroidsXY(C, k)
            clusters, clusterDistances, point_distances = pointClusterMembership(data, centroids)
            writeClusters(data, clusters, 'cluster-first-loop', clusterDistances)
            writeLoopData(clusters, clusterDistances, centroids, 'cluster-first-loop', k)
        if counter == 2:
            plt.savefig('cluster-middle-loop.pdf')
            centroids = convertCentroidsXY(C, k)
            clusters, clusterDistances, point_distances = pointClusterMembership(data, centroids)
            writeClusters(data, clusters, 'cluster-middle-loop', clusterDistances)
            writeLoopData(clusters, clusterDistances, centroids, 'cluster-middle-loop', k)
        if counter == 4:
            plt.savefig('cluster-final-loop.pdf')
            centroids = convertCentroidsXY(C, k)
            clusters, clusterDistances, point_distances = pointClusterMembership(data, centroids)
            writeClusters(data, clusters, 'cluster-final-loop', clusterDistances)
            writeLoopData(clusters, clusterDistances, centroids, 'cluster-final-loop', k)
        counter += 1


def convertCentroidsXY(c, k):
    centroids = []
    x = []
    y = []
    for i in range(0, k):
        x.append(c[i][0])
        y.append(c[i][1])
        centroids.append([x[i], y[i]])
    return centroids


def distance(p, q):
    return int(math.fabs(p[0] - q[0]) + math.fabs(p[1] - q[1]))


def pointClusterMembership(points, centroids):
    cluster = []
    clusterDistances = []
    point_distances = {}
    for i in range(0, len(points)):
        clusterNum, clusterDistance, point_distances = leastDistance(points[i], centroids)
        cluster.append(clusterNum)
        clusterDistances.append(clusterDistance)
    return cluster, clusterDistances, point_distances


def dist(a, b, ax=1):
    return np.linalg.norm(a - b, axis=ax)


def normalize(data):
    normalizedData = []
    for value in data:
        normalizedData.append(round(((value - min(data)) / (max(data) - min(data))) * 100))
    return normalizedData


def readData():
    with open('students.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        next(reader)
        ages = []
        gpas = []
        for row in reader:
            ages.append(int(row[2]))
            gpas.append(float(row[6]))
        ages = normalize(ages)
        gpas = normalize(gpas)
    csvFile.close()
    return ages, gpas


def writeData(ages, gpas):
    in_file = open("students.csv", "rt")
    reader = csv.reader(in_file)
    next(reader)
    out_file = open("students_normalized.csv", "wt")
    writer = csv.writer(out_file)
    writer.writerow(["Name", "Year", "Age", "Major", "Degree", "Living Condition", "GPA", "Passing"])
    counter = 0
    for row in reader:
        row[2] = ages[counter]
        row[6] = gpas[counter]
        writer.writerow(row)
        counter += 1
    in_file.close()
    out_file.close()


def convertToXY(ages, gpas):
    points = []
    for i in ages:
        points.append([ages[i], gpas[i]])
    return points


def leastDistance(point, centroids):
    point_distances = {}
    for i in centroids:
        distant = distance(point, i)
        point_distances[str(i)] = distant
    return min(point_distances, key=point_distances.get), point_distances[
        min(point_distances.keys(), key=(lambda k: point_distances[k]))], point_distances


def writeClusters(points, clusters, val, clusterDistances):
    file = open(val + ".csv", "wt")
    writer = csv.writer(file)
    writer.writerow(["Point", "X/Y", "Closest Centroid", "Distance From Centroid"])
    for i in range(0, len(points)):
        row = [i + 1, points[i], clusters[i], clusterDistances[i]]
        writer.writerow(row)
    file.close()


def writeLoopData(clusters, clusterDistances, centroids, val, k):
    centroid_distances = [0] * k
    for i in range(0, len(clusters)):
        for j in range(0, len(centroids)):
            # print(clusters[i], centroids[j])
            if str(clusters[i]) == str(centroids[j]):
                centroid_distances[j] += clusterDistances[i]
    file = open(val + "-centroid-sse" + ".txt", "w")
    for i in range(0, k):
        file.write("\nCluster " + str(i+1) + " SSE\nCentroid : " + str(centroids[i]) + " == " + str(centroid_distances[i]))
    file.close()


main()
