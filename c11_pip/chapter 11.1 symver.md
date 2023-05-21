- **created by**: Sudip Ghimire
- **URL**: https://www.sudipghimire.com.np
- **Github**: https://github.com/ghimiresdp

# 11.1. Symantic Versioning system

Ref: https://semver.org/

- Symantic Versioning system uses major, minor, and patch release labels to track the current release of the software.

Eg: Django version `3.2.10`

- The `major` release is `3`
- The `minor` release is `2`
- The `patch` release is `10`

Sometimes, additional labels for pre-releases are also tracked using `dev`, `alpha`, `beta`, `release candidates` or `rc`, and `build_id`.

Some examples of pre-release versions are as follows:
- `3.2.10-a1`
- `3.2.10-alpha.1`
- `3.2.10-beta`
- `3.2.10-rc.1`
- `3.2.10-rc.1+41A39F2`, etc.

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


The tree below shows an example of the release cycle of a software.

```
v0.1.0
v0.2.0
...
v0.9.0
v0.10.0
...
v1.0.0-a1
v1.0.0-a2
...
v1.0.0-b1
v1.0.0-b2
...
v1.0.0-rc.1
v1.0.0-rc.2
...
v1.0.0              (Major release)
        v1.0.1      (patch / bugfix)
        v1.0.2
        ...

    v1.1.0          (Minor Release)
        v1.1.1      (patch / bugfix)
        v1.1.2
        ...

    v1.2.0          (Minor Release)
    ...

v2.0.0              (Major Release)
```
