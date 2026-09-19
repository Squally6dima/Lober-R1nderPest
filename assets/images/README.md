# Device render assets

Put the following local renders here:

- `iphone_16_pro.png`
- `iphone_14_pro_max.png`
- `ipad_mini_6.png`
- `iphone16pro_natural_titanium.png` (legacy/fallback name supported by the UI)

Recommended:
- transparent PNG
- high-resolution source (at least 500 px on the long side)
- Natural Titanium / clean product render for iPhone 16 Pro
- preserve the device's aspect ratio

The app scales these images with Qt.KeepAspectRatio + Qt.SmoothTransformation.
