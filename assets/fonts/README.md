# Bundled Inter font

Place the official Inter font files from the [rsms/inter](https://github.com/rsms/inter) release in this directory.

Recommended file:
- `InterVariable.ttf`

Optional static files:
- `Inter-Regular.ttf`
- `Inter-Medium.ttf`
- `Inter-SemiBold.ttf`
- `Inter-Bold.ttf`

The application loads the bundled font with `QFontDatabase.addApplicationFont()` before applying the global QSS, so the UI does not depend on a user's Windows font installation.

Inter is distributed under the SIL Open Font License 1.1. Keep the upstream license with redistributed font files.
