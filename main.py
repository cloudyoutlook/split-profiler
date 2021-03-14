import subprocess
from zipfile import ZipFile
from glob import glob
import re

def unzipAPK(zipPath):
    with ZipFile(zipPath, "r") as zip_ref:
        zip_ref.extractall(zipPath + "_out")
        apkPaths = glob(zipPath + "_out/*.apk")
    return apkPaths


def fetchProperty(badgingOutput, property):

    # find the propery.
    packageRegex = re.compile(property)
    matches = re.findall(packageRegex, badgingOutput)

    return matches


def determineSplits(zipPath):

    apkPaths = unzipAPK(zipPath)

    arrayofobjects = []

    # Get Name
    for apkPath in apkPaths:

        packageDiscoveryCommand = ["lib/" + AAPT_NAME, "dump", "badging", apkPath]
        try:
            badgingOutput = subprocess.check_output(packageDiscoveryCommand)
        except Exception, e:
            badgingOutput = str(e.output)

        packageInfo = {}

        packageInfo['Name'] = fetchProperty(badgingOutput, "package: name='([a-zA-Z0-9._]+)'")
        packageInfo['versionCode'] = fetchProperty(badgingOutput, "package: .* versionCode='([a-zA-Z0-9._]+)'")
        packageInfo['versionName'] = fetchProperty(badgingOutput, "package: .* versionName='([a-zA-Z0-9._]+)'")
        packageInfo['split'] = fetchProperty(badgingOutput, "package: .* split='([a-zA-Z0-9._]+)'")
        packageInfo['sdkVersion'] = fetchProperty(badgingOutput, "sdkVersion:'([a-zA-Z0-9._]+)'")
        packageInfo['targetSdkVersion'] = fetchProperty(badgingOutput, "targetSdkVersion:'([a-zA-Z0-9._]+)'")
        packageInfo['Locale'] = fetchProperty(badgingOutput, "locales:([ a-zA-Z0-9._\\-']+)")
        packageInfo['Screens'] = fetchProperty(badgingOutput, "supports-screens:([ a-zA-Z0-9._\-']+)")
        packageInfo['AnyDensity'] = fetchProperty(badgingOutput, "supports-any-density:")
        packageInfo['Densities'] = fetchProperty(badgingOutput, "densities:( '[a-zA-Z0-9._-]+')+")
        packageInfo['native-code'] = fetchProperty(badgingOutput, "^native-code:( '[a-zA-Z0-9._-]+')+")
        packageInfo['alt-native-code'] = fetchProperty(badgingOutput, "alt-native-code:( '[a-zA-Z0-9._-]+')+")
        packageInfo['uses-feature'] = fetchProperty(badgingOutput, "uses-(?:implied-)?feature(?!-not-required)[a-zA-Z0-9-]+: name='([a-zA-Z0-9._]+)'")
        packageInfo['uses-permission'] = fetchProperty(badgingOutput, "uses-permission: name='([a-zA-Z0-9._]+)'")

        arrayofobjects.append(packageInfo)

    return arrayofobjects


if __name__ == '__main__':
    AAPT_NAME = "aapt"
    stuff = determineSplits(
        "~/Downloads/my.zip")

    print(stuff)
