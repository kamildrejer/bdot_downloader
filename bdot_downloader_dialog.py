# -*- coding: utf-8 -*-
"""
/***************************************************************************
 BdotDowloaderDialog
                                 A QGIS plugin
 pobiera BDOT i uzupełnia bazę danych
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2022-12-16
        git sha              : $Format:%H$
        copyright            : (C) 2022 by Kamil Drejer
        email                : kamil.drejer@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets
from qgis.PyQt.QtGui import *
from qgis.gui import QgsSpinBox

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'bdot_downloader_dialog_base.ui'))


class BdotDowloaderDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(BdotDowloaderDialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.data = [['BUBD01','budynki mieszkalne jednorodzinne',True,],
            ['BUBD02','budynki o dwóch mieszkaniach',True,],
            ['BUBD03','budynki o trzech i więcej mieszkaniach',True,],
            ['BUBD04','budynki zbiorowego zamieszkania',True,],
            ['BUBD05','budynki hoteli',False,],
            ['BUBD06','budynki zakwaterowania turystycznego, pozostałe',False,],
            ['BUBD07','budynki biurowe',False,],
            ['BUBD08','budynki handlowo usługowe',False,],
            ['BUBD09','budynki łączności, dworców i terminali',False,],
            ['BUBD10','budynki garaży',False,],
            ['BUBD11','budynki przemysłowe',False,],
            ['BUBD12','zbiorniki, silosy i budynki magazynowe',False,],
            ['BUBD13','ogólnodostępne obiekty kulturalne',False,],
            ['BUBD14','budynk imuzeów i bibliotek',False,],
            ['BUBD15','budynki szkół i instytucji badawczych',False,],
            ['BUBD16','budynki szpitali i zakładów opieki medycznej',False,],
            ['BUBD17','budynki kultury fizycznej',False,],
            ['BUBD18','budynki gospodarstw rolnych',False,],
            ['BUBD19','budynki przeznaczone do sprawowania kultu religijnego i czynności religijnych',False,],
            ['BUBD20','obiekty budowlane wpisane do rejestru zabytków i objęteindywidualną ochroną konserwatorską oraz nieruchome, archeologiczne dobra kultury',False,],
            ['BUBD21','pozostałe budynki niemieszkalne, gdzie indziej nie?wymienione',False,],
            ['SKJZ01','jezdnia autostrady',False,],
            ['SKJZ02','jezdnia drogi ekspresowej',False,],
            ['SKJZ03','jezdnia drogi głównej ruchu przyśpieszonego',False,],
            ['SKJZ04','jezdnia drogi głównej',False,],
            ['SKJZ05','jezdnia drogi zbiorczej',False,],
            ['SKJZ06','jezdnia drogi lokalnej',False,],
            ['SKJZ07','jezdnia drogi dojazdowej',False,],
            ['SKJZ08','jezdnia drogi innej',False,],
            ['SKDR01','autostrada',True,],
            ['SKDR02','droga ekspresowa',True,],
            ['SKDR03','droga główna ruchu przyśpieszonego',True,],
            ['SKDR04','droga główna',True,],
            ['SKDR05','droga zbiorcza',True,],
            ['SKDR06','droga lokalna',True,],
            ['SKDR07','droga dojazdowa',True,],
            ['SKDR08','droga inna',False,],
            ['SKRW01','rondo',False,],
            ['SKRW02','węzeł drogowy',False,],
            ['SKRP01','alejka',False,],
            ['SKRP02','pasaż',False,],
            ['SKRP03','ścieżka',False,],
            ['SKTR01','tor kolejowy',False,],
            ['SKTR02','tor metra',False,],
            ['SKTR03','tor tramwajowy',False,],
            ['SKPP01','bród',False,],
            ['SKPP02','przeprawa łodziami',False,],
            ['SKPP03','przeprawa promowa',False,],
            ['SWRS01','rzeka',False,],
            ['SWRS02','strumień, potok lub struga',False,],
            ['SWKN01','kanał',False,],
            ['SWRM01','rów melioracyjny zbiorczy',True,],
            ['SWRM02','rów melioracyjny zwykły',True,],
            ['SULN01','linia elektroenergetyczna najwyższego napięcia',True,],
            ['SULN02','linia elektroenergetyczna wysokiego napięcia',True,],
            ['SULN03','linia elektroenergetyczna średniego napięcia',True,],
            ['SULN04','linia elektroenergetyczna niskiego napięcia',False,],
            ['SULN05','linia telekomunikacyjna',False,],
            ['SUPR01','benzynowy',True,],
            ['SUPR02','ciepłowniczy',False,],
            ['SUPR03','gazowy',True,],
            ['SUPR04','kanalizacyjny',False,],
            ['SUPR05','naftowy',True,],
            ['SUPR06','wodociągowy',False,],
            ['PTWP01','woda morska',False,],
            ['PTWP02','woda płynąca',False,],
            ['PTWP03','woda stojąca',False,],
            ['PTZ1301','zabudowa wielorodzinna',False,],
            ['PTZ1302','zabudowa jednorodzinna',False,],
            ['PTZ1303','zabudowa przemysłowo-składowa',False,],
            ['PTZ1304','zabudowa handlowo-usługowa',False,],
            ['PTZ1305','pozostała zabudowa',False,],
            ['PTLZ01','las',False,],
            ['PTLZ02','zagajnik',False,],
            ['PTLZ03','zadrzewienie',False,],
            ['PTRK01','kosodrzewina',False,],
            ['PTRK02','krzewy',False,],
            ['PTUT01','ogród działkowy',False,],
            ['PTUT02','plantacja',False,],
            ['PTUT03','sad',False,],
            ['PTUT04','szkółka leśna',False,],
            ['PTUT05','szkółka roślin ozdobnych',False,],
            ['PTTR01','roślinność trawiasta',False,],
            ['PTTR02','uprawa na gruntach ornych',False,],
            ['PTKM01','teren pod drogą kołową',False,],
            ['PTKM02','teren pod torowiskiem',False,],
            ['PTKM03','teren pod drogą kołową i torowiskiem',False,],
            ['PTKM04','teren pod drogą lotniskową',False,],
            ['PTGN01','piarg, usypisko lub rumowisko skalne',False,],
            ['PTGN02','teren kamienisty',False,],
            ['PTGN03','teren piaszczysty lub żwirowy',False,],
            ['PTGN04','pozostały grunt nieużytkowany',False,],
            ['PTPL01','plac',False,],
            ['PTS001','teren składowania odpadów komunalnych',False,],
            ['PTS002','teren składowania odpadów przemysłowych',False,],
            ['PTWZ01','wyrobisko',False,],
            ['PTWZ02','zwałowisko',False,],
            ['PTNZ01','teren pod urządzeniami technicznymi lub budowlami',False,],
            ['PTNZ02','teren przemysłowo-składowy',False,],
            ['TC0N01','obszar Natura 2000',False,],
            ['TCPK01','park krajobrazowy',False,],
            ['TCPN01','park narodowy',False,],
            ['TCRZ01','rezerwat',False,],
            ['ADJA01','państwo',False,],
            ['ADJA02','województwo',False,],
            ['ADJA03','powiat',False,],
            ['ADJA04','gmina miejska',False,],
            ['ADJA05','gmina wiejska',False,],
            ['ADJA06','gmina miejsko-wiejska',False,],
            ['ADJA07','miasto w gminie miejsko-wiejskiej',False,],
            ['ADJA08','obszar wiejski w gminie miejsko-wiejskiej',False,],
            ['ADJA09','dzielnica',False,],
            ['ADJA10','delegatura',False,],
            ['ADMS01','miasto',False,],
            ['ADMS02','część miasta',False,],
            ['ADMS03','wieś',False,],
            ['ADMS04','część wsi',False,],
            ['ADMS05','kolonia',False,],
            ['ADMS06','część kolonii',False,],
            ['ADMS07','osada',False,],
            ['ADMS08','część osady',False,],
            ['ADMS09','osiedle',False,],
            ['ADMS10','przysiółek',False,],
            ['ADMS11','leśniczówka',False,],
            ['ADMS12','gajówka',False,],
            ['ADMS13','inny obiekt',False,],
            ['BUIN01','estakada',False,],
            ['BUIN02','kładka dla pieszych',False,],
            ['BUIN03','most',False,],
            ['BUIN04','przejście podziemne dla pieszych',False,],
            ['BUIN05','przepust',False,],
            ['BUIN06','tunel',False,],
            ['BUIN07','wiadukt',False,],
            ['BUHD01','jaz ruchomy lub zastawka piętrząca',False,],
            ['BUHD02','jaz stały',False,],
            ['BUHD03','śluza',False,],
            ['BUHD04','zapora',False,],
            ['BUSP01','basen odkryty',False,],
            ['BUSP02','basen z czaszą foliową',False,],
            ['BUSP03','bieżnia',False,],
            ['BUSP04','kort tenisowy',False,],
            ['BUSP05','kort tenisowy z czaszą foliową',False,],
            ['BUSP06','plac gier i zabaw',False,],
            ['BUSP07','plac sportowy',False,],
            ['BUSP08','skocznia narciarska',False,],
            ['BUSP09','stadion',False,],
            ['BUSP10','sztuczny stok',False,],
            ['BUSP11','tor samochodowy',False,],
            ['BUSP12','tor saneczkowy',False,],
            ['BUSP13','tor żużlowy',False,],
            ['BUWT01','chłodnia kominowa',False,],
            ['BUWT02','komin przemysłowy',False,],
            ['BUWT03','maszt oświetleniowy',False,],
            ['BUWT04','maszt telekomunikacyjny',False,],
            ['BUWT05','turbina wiatrowa',True,],
            ['BUWT06','słup energetyczny',False,],
            ['BUWT07','podpora kolei linowej',False,],
            ['BUWT08','wieża ciśnień',False,],
            ['BUWT09','wieża przeciwpożarowa',False,],
            ['BUWT10','wieża szybu kopalnianego',False,],
            ['BUWT11','wieża telekomunikacyjna',False,],
            ['BUWT12','wieża widokowa',False,],
            ['BUZT01','osadnik',False,],
            ['BUZT02','zbiornik na ciecz',False,],
            ['BUZT03','zbiornik na materiały pędne lub gaz',False,],
            ['BUZT04','zbiornik na materiały sypkie',False,],
            ['BUU001','falochron',False,],
            ['BUU002','ostroga',False,],
            ['BUU003','ściana oporowa',False,],
            ['BUU004','umocnienie brzegu',False,],
            ['BUZM01','fosa sucha lub wykop',False,],
            ['BUZM02','nasyp',False,],
            ['BUZM03','wał przeciwpowodziowy lub grobla',False,],
            ['BUTR01','kolej linowa',False,],
            ['BUTR02','obrotnica kolejowa',False,],
            ['BUTR03','suwnica',False,],
            ['BUTR04','taśmociąg',False,],
            ['BUTR05','wyciąg narciarski',False,],
            ['BUIT01','szyb naftowy lub gazowy',False,],
            ['BUIT02','ujęcie wody',False,],
            ['BUIT03','transformator',False,],
            ['BUIT04','zespół transformatorów',False,],
            ['BUIT05','zespół dystrybutorów paliwa',False,],
            ['BUIT06','zespół urządzeń stacji meteorologicznej',False,],
            ['BUIT07','zespół urządzeń terminalu ropy naftowej lub materiałów ropopochodnych',False,],
            ['BUCM01','zespół nagrobków cmentarnych',False,],
            ['BUIB01','estrada',False,],
            ['BUIB02','ogrodzenie trwałe',False,],
            ['BUIB03','peron kolejowy',False,],
            ['BUIB04','platforma widokowa',False,],
            ['BUIB05','rampa',False,],
            ['BUIB06','trybuna',False,],
            ['KUMN01','osiedle mieszkaniowe',False,],
            ['KUMN02','posesja',False,],
            ['KUPG01','elektrociepłownia',False,],
            ['KUPG02','elektrownia',False,],
            ['KUPG03','gazownia',False,],
            ['KUPG04','gospodarstwo hodowlane',True,],
            ['KUPG05','huta',True,],
            ['KUPG06','kopalnia',True,],
            ['KUPG07','oczyszczalnia ścieków',True,],
            ['KUPG08','podstacja elektroenergetyczna',False,],
            ['KUPG09','przepompownia',False,],
            ['KUPG10','rafineria',True,],
            ['KUPG11','składowisko odpadów',False,],
            ['KUPG12','teren ujęcia wody',False,],
            ['KUPG13','zakład metalurgiczny',True,],
            ['KUPG14','zakład produkcyjny, usługowy lub remontowy',True,],
            ['KUPG15','zakład utylizacji',True,],
            ['KUPG16','zakład wodociągowy',False,],
            ['KUHU01','centrum handlowo-usługowe',True,],
            ['KUHU02','targowisko lub bazar',False,],
            ['KUK001','dworzec autobusowy',False,],
            ['KUK002','lotnisko lub lądowisko',False,],
            ['KUK003','miejsce obsługi podróżnych',False,],
            ['KUK004','parking',False,],
            ['KUK005','port wodny lub przystań',False,],
            ['KUK006','stacja kolejowa',False,],
            ['KUK007','stacja metra',False,],
            ['KUK008','stacja paliw',False,],
            ['KUK009','teren kolejowy',False,],
            ['KUK010','zajezdnia lub baza transportowa',False,],
            ['KUSK01','ogród botaniczny',False,],
            ['KUSK02','ogród zoologiczny',False,],
            ['KUSK03','ośrodek sportowo-rekreacyjny',False,],
            ['KUSK04','park',False,],
            ['KUSK05','zespół domów letniskowych',False,],
            ['KUH001','hotel lub motel',False,],
            ['KUH002','kemping',False,],
            ['KUH003','ośrodek wypoczynkowy',False,],
            ['KUH004','schronisko turystyczne',False,],
            ['KU0S01','ośrodek naukowo-badawczy',False,],
            ['KU0S02','przedszkole lub żłobek',False,],
            ['KU0S03','szkoła lub zespół szkół',False,],
            ['KU0S04','szkoła wyższa',False,],
            ['KU0Z01','zakład opieki socjalnej lub dom dziecka',False,],
            ['KU0Z02','zespół szpitalny lub sanatoryjny',False,],
            ['KUZA01','miejsce pamięci narodowej',False,],
            ['KUZA02','skansen',False,],
            ['KUZA03','twierdza lub forteca',False,],
            ['KUZA04','zespół muzealny',False,],
            ['KUZA05','zespół pałacowy',False,],
            ['KUZA06','zespół zamkowy',False,],
            ['KUSC01','cmentarz',False,],
            ['KUSC02','zespół sakralny lub klasztorny',False,],
            ['KUIK01','poligon wojskowy',False,],
            ['KUIK02','zakład specjalny',False,],
            ['ADJA01','państwo',False,],
            ['ADJA02','województwo',False,],
            ['ADJA03','powiat',False,],
            ['ADJA04','gmina miejska',False,],
            ['ADJA05','gmina wiejska',False,],
            ['ADJA06','gmina miejsko-wiejska',False,],
            ['ADJA07','miasto w gminie miejsko-wiejskiej',False,],
            ['ADJA08','obszar wiejski w gminie miejsko-wiejskiej',False,],
            ['ADJA09','dzielnica',False,],
            ['ADJA10','delegatura',False,],
            ['ADMS01','miasto',False,],
            ['ADMS02','część miasta',False,],
            ['ADMS03','wieś',False,],
            ['ADMS04','część wsi',False,],
            ['ADMS05','kolonia',False,],
            ['ADMS06','część kolonii',False,],
            ['ADMS07','osada',False,],
            ['ADMS08','część osady',False,],
            ['ADMS09','osiedle',False,],
            ['ADMS10','przysiółek',False,],
            ['ADMS11','leśniczówka',False,],
            ['ADMS12','gajówka',False,],
            ['ADMS13','inny obiekt',False,],
            ['0IPR01','drzewo lub grupa drzew',False,],
            ['0IPR02','głaz narzutowy lub grupa głazów',False,],
            ['0IPR03','kępa krzewów',False,],
            ['0IPR04','kępa kosodrzewiny',False,],
            ['0IPR05','linia oddziałowa',False,],
            ['0IPR06','mały las',False,],
            ['0IPR07','odosobniona skała',False,],
            ['0IPR08','pas krzewów lub żywopłot',False,],
            ['0IPR09','próg skalny',False,],
            ['0IPR10','rząd drzew',False,],
            ['0IPR11','wejście do jaskini',False,],
            ['0IPR12','wodospad',False,],
            ['0IPR13','źródło',False,],
            ['0IKM01','ekran akustyczny',False,],
            ['0IKM02','pas startowy',False,],
            ['0IKM03','przejście graniczne',False,],
            ['0IKM04','przystanek autobusowy lub tramwajowy',False,],
            ['0IKM05','przystanek kolejowy',False,],
            ['0IKM06','schody',False,],
            ['0IKM07','sygnalizator świetlny',False,],
            ['0IKM08','wejście do stacji metra',False,],
            ['0IKM09','miejsce poboru opłat',False,],
            ['0I0R01','bunkier lub schron',False,],
            ['0I0R02','figura, kapliczka lub krzyż przydrożny',False,],
            ['0I0R03','fontanna',False,],
            ['0I0R04','mur historyczny',False,],
            ['0I0R05','odosobniona mogiła',False,],
            ['0I0R06','pomnik',False,],
            ['0I0R07','pomost lub molo',False,],
            ['0I0R08','ruina zabytkowa',False,],
            ['0I0R09','studnia głębinowa',False,],
            ['0I0R10','szklarnia (niebędąca budynkiem)',False,],
            ['0I0R11','wiata lub altana',False,],
            ['0I0R12','wiatrak (niebędący budynkiem)',False,],
            ['0I0R13','wieża obserwacyjna',False,],
            ['0I0R14','wodowskaz',False,],
            ['OIMK01','bagno',True,],
            ['OIMK02','teren podmokły',True,],
            ['OISZ01','szuwary',True,],]

        self.data_final = self.data

        self.tableWidget = self.tableWidget
        # header = self.tableWidget.horizontalHeader()
        # header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.Stretch)
        # header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        # header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)

        #Row count
        self.tableWidget.setRowCount(len(self.data))

        #Column count
        self.tableWidget.setColumnCount(len(self.data[0])+1)

        # for j in range(0, len(self.naglowki)):
        #     self.tableWidget.setHorizontalHeaderItem(j, QtWidgets.QTableWidgetItem(self.naglowki[j]))

        for i in range(0, len(self.data)):
            self.tableWidget.setItem(i,0, QtWidgets.QTableWidgetItem(self.data[i][0]))
            self.tableWidget.setItem(i,1, QtWidgets.QTableWidgetItem(self.data[i][1]))
            self.checkb1 = QtWidgets.QCheckBox()
            self.checkb1.setChecked(self.data[i][2])#self.data[i][j])
            self.tableWidget.setCellWidget(i,2, self.checkb1)
            self.lineedit1 = QtWidgets.QLineEdit(self.data[i][0])
            self.tableWidget.setCellWidget(i,3, self.lineedit1)

    def get_menu_status(self):
        self.data_final = self.data
        for row_number in range(0, len(self.data)):
            self.data_final[row_number][0] = self.tableWidget.item(row_number, 0).text()
            self.data_final[row_number][2] = self.tableWidget.cellWidget(row_number, 2).isChecked()
            self.data_final[row_number].append(self.tableWidget.cellWidget(row_number, 3).text())
        return self.data_final
