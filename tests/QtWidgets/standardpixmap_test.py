
import unittest

from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QStyle

from helper import UsesQApplication

class StandardPixmapTest(UsesQApplication):
    def testDefaultOptions(self): # Bug 253
        pixmap = self.app.style().standardPixmap(QStyle.SP_DirClosedIcon)
        self.assert_(isinstance(pixmap, QPixmap))

if __name__ == '__main__':
    unittest.main()

