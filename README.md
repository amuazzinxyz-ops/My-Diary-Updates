# My Diary New

**Independent identity:** My Diary New is a separate app and update channel. It is not part of MUAZZIN.

## Repository purpose

This repository, `My-Diary-Updates`, is reserved only for distributing official **My Diary New** Android app updates.

## Separation from MUAZZIN

- Keep the existing MUAZZIN website, repository, hosting, files, branding, and behavior unchanged.
- Do not place MUAZZIN website files or MUAZZIN app releases here.
- Do not connect this repository to the MUAZZIN website deployment.
- Diary branding and app identity must be maintained independently.

## What belongs here

- Signed My Diary New APK release files
- Version and update-check metadata for My Diary New
- Release notes for My Diary New

## What does not belong here

- The app's private diary entries or user data
- Signing keystores, passwords, access tokens, or other secrets
- MUAZZIN files or files for any other app

## Release requirements

Before publishing an update, verify all of the following against the actual Diary app project and its previously trusted release:

1. Android application ID (must remain the Diary app's own ID)
2. Version name and monotonically increasing version code
3. Signing certificate (must match the trusted Diary release key)
4. APK SHA-256 checksum
5. Install/update test on an Android device

Never invent an application ID, signing identity, version, checksum, or release file. Do not publish an APK until the original Diary app project and signing setup are available and verified.

## Current status

This repository currently contains release instructions only. No APK, update metadata, or app release has been published yet.
