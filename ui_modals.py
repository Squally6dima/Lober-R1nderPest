# -*- coding: utf-8 -*-
"""Reusable frameless, centered modal dialogs for the PyQt5 UI."""

from PyQt5 import QtCore, QtGui, QtWidgets


class FramelessModal(QtWidgets.QDialog):
    """Borderless modal with a centered card-like surface."""

    def __init__(self, parent=None, object_name="Modal", width=480, height=260):
        flags = QtCore.Qt.Dialog | QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowSystemMenuHint
        super().__init__(parent, flags)
        self.setObjectName(object_name)
        self.setModal(True)
        self.resize(width, height)
        self.setMinimumSize(width, height)
        self.setMaximumSize(width, height)

        shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(36)
        shadow.setOffset(0, 12)
        shadow.setColor(QtGui.QColor(0, 0, 0, 80))
        self.setGraphicsEffect(shadow)

        if parent is not None:
            parent.installEventFilter(self)

    def show_centered(self):
        self._center()
        self.show()
        self.raise_()
        self.activateWindow()

    def showEvent(self, event):
        super().showEvent(event)
        self._center()

    def _center(self):
        parent = self.parentWidget()
        if parent is None:
            return
        center = parent.window().frameGeometry().center()
        self.move(center.x() - self.width() // 2, center.y() - self.height() // 2)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.reject()
            return
        super().keyPressEvent(event)

    def eventFilter(self, watched, event):
        if watched is self.parentWidget() and event.type() == QtCore.QEvent.Resize and self.isVisible():
            self._center()
        return super().eventFilter(watched, event)
