import json
import webbrowser
import pandas as pd
import sys
import io

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QWidget,\
    QLabel, QSpacerItem, QSizePolicy, QHBoxLayout, QApplication, QTableView
from PyQt5.QtCore import QAbstractTableModel, Qt
from collections import OrderedDict
import chardet
import xml.etree.ElementTree as ET
import xmltodict


class pandasModel(QAbstractTableModel):

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parnet=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None

def iter_docs(author):
    author_attr = author.attrib
    for doc in author.iter('document'):
        doc_dict = author_attr.copy()
        doc_dict.update(doc.attrib)
        doc_dict['data'] = doc.text
        yield doc_dict

with open('./data/BI_Repository.json', 'rb') as load_f:
    load_dict = json.load(load_f)
    for key in load_dict.keys():
        if key == 'entries':
            #only read webi entries
            df = pd.json_normalize(load_dict[key])

            df_filtered = pd.DataFrame(columns = ["Name", "Description", "Can Schedule", "Property"])
            df_filtered['Name'] = df['SI_NAME']
            df_filtered['Description'] = df['SI_DESCRIPTION']
            df_filtered['Can Schedule'] = df['SI_IS_SCHEDULABLE']
            df_filtered['Property'] = pd.Series(df['SI_WEBI_DOC_PROPERTIES'], dtype="string")
            #Parse WebI property XML file
            xml_content = pd.Series(df['SI_WEBI_DOC_PROPERTIES'], dtype="string")
            etree = ET.parse('./data/WebI_Property.xml')
            #etree = ET.fromstring(xml_content)
            #print(etree)
            for node in etree.getroot():
                print(node.tag, node.attrib)
                print(node.attrib.get('NAME'), ":", node.attrib.get('VALUE'))

            #Generate Table layout
            if __name__ == '__main__':
                app = QApplication(sys.argv)
                model = pandasModel(df_filtered)
                view = QTableView()
                view.setModel(model)
                view.resize(800, 600)
                view.show()
                sys.exit(app.exec_())