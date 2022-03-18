# Symantic Versioning system

https://semver.org/

- Symantic Versioning system uses major, minor, and patch release labels to track the current release of the software.

Eg: Django version `3.2.10`

- The major release is 3
- The minor release is 2
- The patch release is 10

Sometimes, additional labels for pre-releases are also tracked using `dev`, `alpha`, `beta`, and `release candidates`.
some examples are:
- `3.2.10-a1`
- `3.2.10-alpha.1`
- `3.2.10-beta`
- `3.2.10-rc.1`, etc.

## Major Release
- This release introduce new features
- It is going to break your existing code with previous versions
- With every major release, the first release number is going to be increased by 1 and other release numbers would be 0
  - `1.2.10` -> `2.0.0`

## Minor Release
- They introduce some new features, but not with heavy changes.
- The code might break in this case also, but can be fixed with small refactorings. (Backward Compatible)
- In this release, features just gets depreciated, but do not get removed.
- With this release second release number is going to be increased by 1 and the last would be 0
- `11.2.10` -> `11.3.0`

## Patch Release / Bugfix Release

- This release is not going to introduce any new features
- The older code is not going to break in this release
- Every changes is going to be internal changes or logical changes.
- With this release the last release number is going to be increased by 1
- `11.2.10` -> `11.2.11`
