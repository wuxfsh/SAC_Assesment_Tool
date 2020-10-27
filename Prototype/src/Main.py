import sys
from PyQt5.QtWidgets import *

data = {"info": "成绩单",
        "grades": {
            "Chinese": {
                "小明": 60,
                "小红": 80
            },
            "Math": {
                "小明": 90,
                "小红": 70
            },
            "English": {
                "小明": 80,
                "小红": 80
            },
        }}


class TreeWidget(QTreeWidget):
    def __init__(self):
        super(TreeWidget, self).__init__()

        self.setColumnCount(2)  # 共2列
        self.setHeaderLabels(['Key', 'Value'])

        self.rootList = []
        root = self
        self.generateTreeWidget(data, root)

        print(len(self.rootList), self.rootList)

        self.insertTopLevelItems(0, self.rootList)

    def generateTreeWidget(self, data, root):
        if isinstance(data, dict):
            for key in data.keys():
                child = QTreeWidgetItem()
                child.setText(0, key)
                if isinstance(root, QTreeWidget) == False:  # 非根节点，添加子节点
                    root.addChild(child)
                self.rootList.append(child)
                print(key)
                value = data[key]
                self.generateTreeWidget(value, child)
        else:
            root.setText(1, str(data))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = TreeWidget()
    win.show()
    sys.exit(app.exec_())