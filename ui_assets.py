# -*- coding: utf-8 -*-
"""Central asset registry for the Lober_R1nderPest device UI."""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
IOS_DIR = BASE_DIR / "assets" / "icons" / "ios_versions"
DEVICE_DIR = BASE_DIR / "assets" / "images"
STATUS_DIR = BASE_DIR / "assets" / "icons" / "status"

DEVICE_ASSETS = {
    "iPhone 16 Pro": {
        "product_types": {"iPhone17,1", "iPhone17,2"},
        "ios_version": "26.6.2",
        "build": "23C90",
        "ios_logo": IOS_DIR / "ios-26-badge-icon.png",
        "device_image": DEVICE_DIR / "iphone_16_pro.png",
        "status_icon": STATUS_DIR / "status_unsupported.png",
        "supported": False,
    },
    "iPhone 14 Pro Max": {
        "product_types": {"iPhone15,3"},
        "ios_version": "26.6.2",
        "build": "23C90",
        "ios_logo": IOS_DIR / "IOS_18_logo.png",
        "device_image": DEVICE_DIR / "iphone_14_pro_max.png",
        "status_icon": STATUS_DIR / "status_supported.png",
        "supported": True,
    },
    "iPad mini 6": {
        "product_types": {"iPad14,1", "iPad14,2"},
        "ios_version": "26.6.2",
        "build": "23C90",
        "ios_logo": IOS_DIR / "ios-26-badge-icon.png",
        "device_image": DEVICE_DIR / "ipad_mini_6.png",
        "status_icon": STATUS_DIR / "status_supported.png",
        "supported": True,
    },
}

IOS_LOGOS = {
    "16": IOS_DIR / "IOS_16_Logo.png",
    "17": IOS_DIR / "IOS_17_logo.png",
    "18": IOS_DIR / "IOS_18_logo.png",
    "26": IOS_DIR / "ios-26-badge-icon.png",
    "27": IOS_DIR / "IOS_27_icon.png",
}


def get_device_asset(device_name: str, product_type: str = ""):
    """Return the best matching device configuration, with a safe generic fallback."""
    normalized = (device_name or "").strip()
    for name, data in DEVICE_ASSETS.items():
        if normalized == name or product_type in data["product_types"]:
            return name, data

    return normalized or "Unknown device", {
        "ios_version": "",
        "build": "",
        "ios_logo": IOS_LOGOS.get("26"),
        "device_image": DEVICE_DIR / "iphone_16_pro.png",
        "status_icon": STATUS_DIR / "status_unsupported.png",
        "supported": False,
    }
