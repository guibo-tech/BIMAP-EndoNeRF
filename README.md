# BIMAP-EndoNeRF

## Introduction
This project uses endoscopy images to generate a 3D reconstruction of the inside of the human body. This is done by using the endoscope's position and orientation as input to the NeRF network, along with the 2D images captured by the endoscope. The NeRF network then generates a 3D model of the internal structure of the body that matches the captured images.

## Git - Tagging
Proper Tag usage is important for self-documenting commits that introduce, improve, or fix features. This will make semantic versioning much easier.

[FEATURE]: A feature or functionality has been developed for the first time.
[IMPROVE]: Existing correct functionality has been improved.
[FIX]: Existing incorrect code has been fixed.
[TESTS]: A commit concerns test coverage or functionality only.
[CHORE]: Something that is not a feature, fix, improvement, test, release or pipeline commit. For example, a code style cleanup.
[CLEANUP]: To clean up redundant or outdated files.
[STYLE]: For commits regarding the style guidelines
[MISC]: A general miscellaneous type of changes which does not lie in any of other categories.
[REPOSITORY]: When changes are related to repository structure and settings, creating tags, branches, shelves, folders and etc.
[RELEASE]: When a new installer version is created or anything for the Project release version (i.e. documentation, ...) was changed.
