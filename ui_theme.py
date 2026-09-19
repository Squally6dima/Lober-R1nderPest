# -*- coding: utf-8 -*-
"""Global Light/Dark theme and bundled Inter font support for the PyQt5 UI."""

from pathlib import Path
from typing import Dict

from PyQt5 import QtGui, QtWidgets


class ThemeManager:
    LIGHT = "light"
    DARK = "dark"

    TOKENS: Dict[str, Dict[str, str]] = {
        LIGHT: {
            "bg": "#F4F5F7",
            "surface": "#FFFFFF",
            "surface_alt": "#F8FAFC",
            "text": "#0F172A",
            "sub": "#64748B",
            "border": "#E2E8F0",
            "accent": "#FF6B00",
            "accent_hover": "#E05E00",
            "success": "#22C55E",
            "error": "#EF4444",
            "input": "#FFFFFF",
        },
        DARK: {
            "bg": "#09090B",
            "surface": "#18181B",
            "surface_alt": "#1F1F23",
            "text": "#F8FAFC",
            "sub": "#94A3B8",
            "border": "#27272A",
            "accent": "#FF6B00",
            "accent_hover": "#E05E00",
            "success": "#22C55E",
            "error": "#EF4444",
            "input": "#111113",
        },
    }

    @classmethod
    def load_inter(cls, base_dir: str) -> str:
        font_dir = Path(base_dir) / "assets" / "fonts"
        candidates = (
            "InterVariable.ttf",
            "Inter-VariableFont_opsz,wght.ttf",
            "Inter-Regular.ttf",
            "Inter-Medium.ttf",
            "Inter-SemiBold.ttf",
            "Inter-Bold.ttf",
        )
        loaded_family = ""
        for filename in candidates:
            path = font_dir / filename
            if not path.exists():
                continue
            font_id = QtGui.QFontDatabase.addApplicationFont(str(path))
            if font_id < 0:
                continue
            families = QtGui.QFontDatabase.applicationFontFamilies(font_id)
            if families and not loaded_family:
                loaded_family = families[0]
            for family in families:
                if "inter" in family.lower():
                    loaded_family = family
                    break

        if loaded_family:
            return loaded_family

        system_font = QtGui.QFont("Inter")
        if system_font.family().lower() == "inter":
            return "Inter"
        return "Segoe UI"

    @classmethod
    def font(cls, family: str) -> QtGui.QFont:
        qfont = QtGui.QFont(family, 10)
        qfont.setStyleStrategy(QtGui.QFont.PreferAntialias)
        qfont.setHintingPreference(QtGui.QFont.PreferNoHinting)
        return qfont

    @classmethod
    def qss(cls, mode: str, family: str) -> str:
        t = cls.TOKENS[mode]
        return f'''
        * {{ font-family: "{family}"; }}
        QWidget {{ color: {t["text"]}; background: transparent; }}
        QMainWindow {{ background: {t["bg"]}; }}

        QFrame#Intro, QFrame#HomePage, QWidget#centralwidget {{
            background: {t["bg"]};
        }}
        QLabel {{ background: transparent; }}

        QLabel#welcomeTitle {{
            color: {t["text"]}; font-size: 28px; font-weight: 600;
        }}
        QLabel#welcomeMessage {{
            color: {t["sub"]}; font-size: 13px; font-weight: 400;
        }}
        QLabel#introStatusLabel {{
            color: {t["sub"]}; font-size: 12px; font-weight: 500;
        }}

        QFrame#frame {{
            background: {t["surface_alt"]};
            border: 1px solid {t["border"]};
            border-radius: 10px;
        }}
        QFrame#pb1, QFrame#progressFrame {{
            background: {t["accent"]}; border: none; border-radius: 4px;
        }}

        QFrame#sidebar {{
            background: {t["surface"]};
            border-right: 1px solid {t["border"]};
        }}

        QLabel#headerTitle {{
            color: {t["text"]}; font-size: 17px; font-weight: 600;
        }}
        QLabel#themeHint {{
            color: {t["sub"]}; font-size: 11px; font-weight: 500;
        }}
        QLabel#devicesCaption, QLabel#deviceSectionLabel {{
            color: {t["sub"]}; font-size: 11px; font-weight: 600;
        }}
        QLabel#iosVersionLarge {{
            color: {t["text"]}; font-size: 23px; font-weight: 600;
        }}
        QLabel#buildNumber, QLabel#deviceUDID, QLabel#activationState,
        QLabel#capabilitySubtitle, QLabel#apiUrlHint {{
            color: {t["sub"]}; font-size: 10px; font-weight: 400;
        }}
        QLabel#deviceName {{
            color: {t["text"]}; font-size: 19px; font-weight: 600;
        }}
        QLabel#capabilityHeader {{
            color: {t["sub"]};
            font-size: 11px;
            font-weight: 600;
        }}

        QLabel#capabilityTitle {{
            color: {t["text"]}; font-size: 14px; font-weight: 600;
        }}

        QLabel#iosBadge {
            background: transparent;
            border: none;
        }

        QLabel#capabilityIcon {{
            background: {t["success"]}; color: #FFFFFF;
            border-radius: 14px; font-size: 16px; font-weight: 600;
        }}
        QLabel#capabilityIcon[assetMissing="false"] {{
            background: transparent;
            border: none;
        }}
        QLabel#capabilityIcon[state="error"] {{ background: {t["error"]}; }}
        QLabel#capabilityIcon[state="neutral"] {{ background: #94A3B8; }}

        QFrame#summaryCard, QFrame#deviceCard, QFrame#capabilityCard {{
            background: {t["surface"]};
            border: 1px solid {t["border"]};
            border-radius: 12px;
        }}
        QFrame#devicePreviewFrame {{
            background: {t["surface_alt"]};
            border: 1px solid {t["border"]};
            border-radius: 10px;
        }}

        QListWidget#devicesList {{
            background: transparent; border: none; color: {t["text"]};
            outline: none; font-size: 11px;
        }}
        QListWidget#devicesList::item {{
            padding: 8px 10px; margin: 2px 0; border-radius: 8px;
            color: {t["sub"]};
        }}
        QListWidget#devicesList::item:hover {{
            background: {t["surface_alt"]}; color: {t["text"]};
        }}
        QListWidget#devicesList::item:selected {{
            background: {t["accent"]}; color: #FFFFFF;
        }}

        QPushButton {{
            min-height: 38px; padding: 0 12px; border-radius: 8px;
            border: 1px solid {t["border"]}; background: {t["surface"]};
            color: {t["text"]}; font-size: 12px; font-weight: 500;
        }}
        QPushButton:hover {{
            background: {t["surface_alt"]}; border-color: {t["accent"]};
        }}
        QPushButton:pressed {{ background: {t["surface_alt"]}; }}
        QPushButton:focus {{ border: 1px solid {t["accent"]}; }}

        QPushButton#activateButton {{
            background: {t["accent"]}; color: #FFFFFF; border: none;
            font-size: 12px; font-weight: 600;
        }}
        QPushButton#activateButton:hover,
        QPushButton#activateButton:pressed {{
            background: {t["accent_hover"]};
        }}
        QPushButton#activateButton:disabled {{
            background: {t["surface_alt"]}; color: {t["sub"]};
            border: 1px solid {t["border"]};
        }}

        QPushButton#settingsButton, QPushButton#themeButton,
        QPushButton#settingsCancel, QPushButton#closePopup,
        QPushButton#detailsToggle, QPushButton#dependenciesChoose,
        QPushButton#logsChoose {{
            background: transparent; color: {t["text"]};
            border: 1px solid {t["border"]};
        }}
        QPushButton#settingsButton:hover, QPushButton#themeButton:hover,
        QPushButton#settingsCancel:hover, QPushButton#closePopup:hover,
        QPushButton#detailsToggle:hover, QPushButton#dependenciesChoose:hover,
        QPushButton#logsChoose:hover {{
            background: {t["surface_alt"]}; border-color: {t["accent"]};
        }}

        QPushButton#settingsSave, QPushButton#activationDone {{
            background: {t["accent"]}; color: #FFFFFF;
            border: 1px solid {t["accent"]}; font-weight: 600;
        }}
        QPushButton#settingsSave:hover, QPushButton#activationDone:hover {{
            background: {t["accent_hover"]}; border-color: {t["accent_hover"]};
        }}
        QPushButton#activationDone:disabled {{
            background: {t["surface_alt"]}; color: {t["sub"]};
            border-color: {t["border"]};
        }}

        QLineEdit, QTextEdit {{
            min-height: 38px; padding: 8px 12px;
            border: 1px solid {t["border"]}; border-radius: 8px;
            background: {t["input"]}; color: {t["text"]};
            selection-background-color: {t["accent"]};
            selection-color: #FFFFFF;
        }}
        QTextEdit {{ min-height: 82px; }}
        QLineEdit:hover, QTextEdit:hover {{ border-color: #CBD5E1; }}
        QLineEdit:focus, QTextEdit:focus {{ border: 1px solid {t["accent"]}; }}

        QFrame#pbFrame {{
            background: {t["surface_alt"]};
            border: 1px solid {t["border"]};
            border-radius: 6px;
        }}
        QProgressBar {{
            min-height: 8px; max-height: 8px; border: none;
            border-radius: 4px; background: {t["surface_alt"]};
        }}
        QProgressBar::chunk {{ border-radius: 4px; background: {t["accent"]}; }}

        QFrame#InfoNotification, QFrame#LoadingNotification {{
            background: {t["surface"]}; border: 1px solid {t["border"]};
            border-radius: 12px;
        }}
        QLabel#messageTitle, QLabel#activationDeviceTitle, QLabel#settingsTitle {{
            color: {t["text"]}; font-size: 13px; font-weight: 600;
        }}
        QLabel#messageContent, QLabel#loadingText, QLabel#activationStep {{
            color: {t["sub"]}; font-size: 11px; font-weight: 400;
        }}

        QDialog#activationDialog, QDialog#settingsDialog {{
            background: {t["surface"]}; border: 1px solid {t["border"]};
            border-radius: 16px;
        }}
        QDialog#activationDialog QLabel, QDialog#settingsDialog QLabel {{
            color: {t["text"]};
        }}
        QDialog#activationDialog QLabel#activationStep,
        QDialog#settingsDialog QLabel#apiUrlHint {{
            color: {t["sub"]};
        }}

        QScrollBar:vertical {{
            background: transparent; width: 8px; margin: 2px;
        }}
        QScrollBar::handle:vertical {{
            background: {t["border"]}; min-height: 24px; border-radius: 4px;
        }}
        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
            height: 0; background: transparent;
        }}
        '''

    @classmethod
    def apply(cls, app: QtWidgets.QApplication, mode: str, base_dir: str) -> str:
        family = cls.load_inter(base_dir)
        app.setStyle("Fusion")
        app.setFont(cls.font(family))
        app.setStyleSheet(cls.qss(mode, family))
        return family
