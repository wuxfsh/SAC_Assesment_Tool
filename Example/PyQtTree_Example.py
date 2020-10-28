import sys
from PyQt5.QtWidgets import *
import json
import chardet
import pandas as pd

with open('./data/BI_Repository.json', 'r') as load_f:
    data = json.load(load_f)

class TreeWidget(QTreeWidget):
    def __init__(self):
        super(TreeWidget, self).__init__()

        self.setColumnCount(2)  # 共2列
        self.setHeaderLabels(['Key', 'Value'])

        self.rootList = []
        root = self
        self.generateTreeWidget(data, root)
        #print(len(self.rootList), self.rootList)

        self.insertTopLevelItems(0, self.rootList)

    def generateTreeWidget(self, data, root):
        if isinstance(data, dict):
            for key in data.keys():
                child = QTreeWidgetItem()
                child.setText(0, key)
                """if key == 'entries':
                    entry_data = data[key]
                    for entry_item in entry_data:
                        print entry_item.
                """

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
    patients_df = pd.read_json('./Data/BI_Repository.json')
    print(patients_df.head())
    win = TreeWidget()
    win.show()
    sys.exit(app.exec_())