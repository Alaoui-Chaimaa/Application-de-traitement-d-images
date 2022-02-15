# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Window.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5.QtWidgets import (QMainWindow, QTextEdit, QVBoxLayout, QPushButton, QAction, QFileDialog, QApplication)
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from math import *
import numpy as np
import matplotlib.pyplot as plt
import cv2
from PIL import Image
import matplotlib.image as mpimg
import numpy as np
from random import randint
from scipy import ndimage
from sklearn.cluster import KMeans



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1043, 572)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(890, 480, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 410, 91, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(720, 410, 91, 21))
        self.label_2.setObjectName("label_2")
        self.ImageOrigine = QtWidgets.QLabel(self.centralwidget)
        self.ImageOrigine.setGeometry(QtCore.QRect(90, 140, 351, 231))
        self.ImageOrigine.setText("")
        self.ImageOrigine.setObjectName("label_3")
        self.ImageFinal = QtWidgets.QLabel(self.centralwidget)
        self.ImageFinal.setGeometry(QtCore.QRect(580, 140, 361, 231))
        self.ImageFinal.setText("")
        self.ImageFinal.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(760, 480, 101, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(500, 100, 20, 361))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(140, 60, 761, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(690, 30, 91, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(530, 30, 151, 21))
        self.label_5.setObjectName("label_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(790, 30, 111, 21))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(140, 30, 101, 21))
        self.label_6.setObjectName("label_6")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 30, 81, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(350, 30, 82, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(660, 120, 351, 231))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1043, 23))
        self.menubar.setObjectName("menubar")
        self.menufichier = QtWidgets.QMenu(self.menubar)
        self.menufichier.setObjectName("menufichier")
        self.menuBinarisation = QtWidgets.QMenu(self.menubar)
        self.menuBinarisation.setObjectName("menuBinarisation")

        self.menuFiltre = QtWidgets.QMenu(self.menubar)
        self.menuFiltre.setObjectName("menuFiltre")
        self.menuMoyenneur = QtWidgets.QMenu(self.menuFiltre)
        self.menuMoyenneur.setObjectName("menuMoyenneur")
        self.menuGaussien = QtWidgets.QMenu(self.menuFiltre)
        self.menuGaussien.setObjectName("menuGaussien")
        self.menuMedian = QtWidgets.QMenu(self.menuFiltre)
        self.menuMedian.setObjectName("menuMedian")
        self.menuContours = QtWidgets.QMenu(self.menubar)
        self.menuContours.setObjectName("menuContours")
        self.menuSegementation = QtWidgets.QMenu(self.menubar)
        self.menuSegementation.setObjectName("menuSegementation")
        self.menuNorphologie = QtWidgets.QMenu(self.menubar)
        self.menuNorphologie.setObjectName("menuNorphologie")

        self.menuBinarisation_2 = QtWidgets.QMenu(self.menubar)
        self.menuBinarisation_2.setObjectName("menuBinarisation_2")
        MainWindow.setMenuBar(self.menubar)
        self.actionOuvrir = QtWidgets.QAction(MainWindow)
        self.actionOuvrir.setObjectName("actionOuvrir")
        self.actionEnregistrer_sous = QtWidgets.QAction(MainWindow)
        self.actionEnregistrer_sous.setObjectName("actionEnregistrer_sous")
        self.actionQuitter = QtWidgets.QAction(MainWindow)
        self.actionQuitter.setObjectName("actionQuitter")
        self.actionNoir_et_Blanc = QtWidgets.QAction(MainWindow)
        self.actionNoir_et_Blanc.setObjectName("actionNoir_et_Blanc")
        self.actionNegatif = QtWidgets.QAction(MainWindow)
        self.actionNegatif.setObjectName("actionNegatif")
        self.actionSepia = QtWidgets.QAction(MainWindow)
        self.actionSepia.setObjectName("actionSepia")
        self.actionBinarisation = QtWidgets.QAction(MainWindow)
        self.actionBinarisation.setObjectName("actionBinarisation")
        self.actionGradient = QtWidgets.QAction(MainWindow)
        self.actionGradient.setObjectName("actionGradient")
        self.actionRobert = QtWidgets.QAction(MainWindow)
        self.actionRobert.setObjectName("actionRobert")
        self.actionPrewitt = QtWidgets.QAction(MainWindow)
        self.actionPrewitt.setObjectName("actionPrewitt")
        self.actionSobel = QtWidgets.QAction(MainWindow)
        self.actionSobel.setObjectName("actionSobel")
        self.actionLaplacien = QtWidgets.QAction(MainWindow)
        self.actionLaplacien.setObjectName("actionLaplacien")
        self.actionCroissance_des_regions = QtWidgets.QAction(MainWindow)
        self.actionCroissance_des_regions.setObjectName("actionCroissance_des_regions")
        self.actionDilatation = QtWidgets.QAction(MainWindow)
        self.actionDilatation.setObjectName("actionDilatation")
        self.actionErosion = QtWidgets.QAction(MainWindow)
        self.actionErosion.setObjectName("actionErosion")
        self.actionOuverture = QtWidgets.QAction(MainWindow)
        self.actionOuverture.setObjectName("actionOuverture")
        self.actionFermeture = QtWidgets.QAction(MainWindow)
        self.actionFermeture.setObjectName("actionFermeture")

        self.actionAvec_45_degre = QtWidgets.QAction(MainWindow)
        self.actionAvec_45_degre.setObjectName("actionAvec_45_degre")
        self.actionAvec_45_degre_2 = QtWidgets.QAction(MainWindow)
        self.actionAvec_45_degre_2.setObjectName("actionAvec_45_degre_2")
        self.actionAvec_45_degre_3 = QtWidgets.QAction(MainWindow)
        self.actionAvec_45_degre_3.setObjectName("actionAvec_45_degre_3")
        self.actionAvec_45_degre_4 = QtWidgets.QAction(MainWindow)
        self.actionAvec_45_degre_4.setObjectName("actionAvec_45_degre_4")
        self.actionAvec_90 = QtWidgets.QAction(MainWindow)
        self.actionAvec_90.setObjectName("actionAvec_90")
        self.actionAvec_180 = QtWidgets.QAction(MainWindow)
        self.actionAvec_180.setObjectName("actionAvec_180")

        self.actionx2_2 = QtWidgets.QAction(MainWindow)
        self.actionx2_2.setObjectName("actionx2_2")
        self.actionx3 = QtWidgets.QAction(MainWindow)
        self.actionx3.setObjectName("actionx3")
        self.actionHistogramme = QtWidgets.QAction(MainWindow)
        self.actionHistogramme.setObjectName("actionHistogramme")
        self.actionEtirement = QtWidgets.QAction(MainWindow)
        self.actionEtirement.setObjectName("actionEtirement")
        self.actionEgalisation = QtWidgets.QAction(MainWindow)
        self.actionEgalisation.setObjectName("actionEgalisation")
        self.action5x5 = QtWidgets.QAction(MainWindow)
        self.action5x5.setObjectName("action5x5")
        self.action7x7 = QtWidgets.QAction(MainWindow)
        self.action7x7.setObjectName("action7x7")
        self.actions_0_1 = QtWidgets.QAction(MainWindow)
        self.actions_0_1.setObjectName("actions_0_1")
        self.actions_0_8 = QtWidgets.QAction(MainWindow)
        self.actions_0_8.setObjectName("actions_0_8")
        self.action3x3 = QtWidgets.QAction(MainWindow)
        self.action3x3.setObjectName("action3x3")
        self.action5x5_2 = QtWidgets.QAction(MainWindow)
        self.action5x5_2.setObjectName("action5x5_2")
        self.actionPartition_des_regions = QtWidgets.QAction(MainWindow)
        self.actionPartition_des_regions.setObjectName("actionPartition_des_regions")
        self.actionMethode_des_K_means = QtWidgets.QAction(MainWindow)
        self.actionMethode_des_K_means.setObjectName("actionMethode_des_K_means")
        self.actionSeuillage_manuelle = QtWidgets.QAction(MainWindow)
        self.actionSeuillage_manuelle.setObjectName("actionSeuillage_manuelle")
        self.actionMethode_d_OTSU = QtWidgets.QAction(MainWindow)
        self.actionMethode_d_OTSU.setObjectName("actionMethode_d_OTSU")
        self.menufichier.addAction(self.actionOuvrir)
        self.menufichier.addAction(self.actionEnregistrer_sous)
        self.menufichier.addAction(self.actionQuitter)

        self.menuBinarisation.addAction(self.actionNegatif)
        self.menuBinarisation.addSeparator()

        self.menuBinarisation.addSeparator()
        self.menuBinarisation.addAction(self.actionHistogramme)
        self.menuBinarisation.addAction(self.actionEtirement)
        self.menuBinarisation.addAction(self.actionEgalisation)
        self.menuMoyenneur.addAction(self.action5x5)
        self.menuMoyenneur.addAction(self.action7x7)
        self.menuGaussien.addAction(self.actions_0_1)
        self.menuGaussien.addAction(self.actions_0_8)
        self.menuMedian.addAction(self.action3x3)
        self.menuMedian.addAction(self.action5x5_2)
        self.menuFiltre.addAction(self.menuMoyenneur.menuAction())
        self.menuFiltre.addAction(self.menuGaussien.menuAction())
        self.menuFiltre.addAction(self.menuMedian.menuAction())
        self.menuContours.addAction(self.actionGradient)
        self.menuContours.addAction(self.actionRobert)
        self.menuContours.addAction(self.actionSobel)
        self.menuContours.addAction(self.actionLaplacien)
        self.menuSegementation.addAction(self.actionCroissance_des_regions)
        self.menuSegementation.addAction(self.actionPartition_des_regions)
        self.menuSegementation.addAction(self.actionMethode_des_K_means)
        self.menuNorphologie.addAction(self.actionDilatation)
        self.menuNorphologie.addAction(self.actionErosion)
        self.menuNorphologie.addAction(self.actionOuverture)
        self.menuNorphologie.addAction(self.actionFermeture)

        self.menuBinarisation_2.addAction(self.actionSeuillage_manuelle)
        self.menuBinarisation_2.addAction(self.actionMethode_d_OTSU)
        self.menubar.addAction(self.menufichier.menuAction())
        self.menubar.addAction(self.menuBinarisation.menuAction())
        self.menubar.addAction(self.menuBinarisation_2.menuAction())
        self.menubar.addAction(self.menuFiltre.menuAction())
        self.menubar.addAction(self.menuContours.menuAction())
        self.menubar.addAction(self.menuSegementation.menuAction())
        self.menubar.addAction(self.menuNorphologie.menuAction())

        self.retranslateUi(MainWindow)
        self.actionQuitter.triggered.connect(MainWindow.close)
        self.pushButton.clicked.connect(MainWindow.close)
        self.actionOuvrir.triggered.connect(self.label.show)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Fermer"))
        self.label.setText(_translate("MainWindow", "Image Originale"))
        self.label_2.setText(_translate("MainWindow", "Image Traitee "))
        self.pushButton_2.setText(_translate("MainWindow", "Reinitialiser"))
        self.label_5.setText(_translate("MainWindow", "Donner un pourcentage :"))
        self.pushButton_3.setText(_translate("MainWindow", "Redimensionner"))
        self.label_6.setText(_translate("MainWindow", "Entrez un angle:"))
        self.pushButton_4.setText(_translate("MainWindow", "Rotation"))
        self.menufichier.setTitle(_translate("MainWindow", "Fichier"))
        self.menuBinarisation.setTitle(_translate("MainWindow", "Image"))

        self.menuFiltre.setTitle(_translate("MainWindow", "Filtrage"))
        self.menuMoyenneur.setTitle(_translate("MainWindow", "Moyenneur"))
        self.menuGaussien.setTitle(_translate("MainWindow", "Gaussien"))
        self.menuMedian.setTitle(_translate("MainWindow", "Median"))
        self.menuContours.setTitle(_translate("MainWindow", "Contours"))
        self.menuSegementation.setTitle(_translate("MainWindow", "Segementation"))
        self.menuNorphologie.setTitle(_translate("MainWindow", "Morphologie"))

        self.menuBinarisation_2.setTitle(_translate("MainWindow", "Binarisation"))
        self.actionOuvrir.setText(_translate("MainWindow", "Ouvrir"))
        self.actionOuvrir.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionEnregistrer_sous.setText(_translate("MainWindow", "Enregistrer sous "))
        self.actionEnregistrer_sous.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionQuitter.setText(_translate("MainWindow", "Quitter"))
        self.actionQuitter.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionNoir_et_Blanc.setText(_translate("MainWindow", "Noir et Blanc"))
        self.actionNegatif.setText(_translate("MainWindow", "Negatif"))
        self.actionSepia.setText(_translate("MainWindow", "Sepia"))
        self.actionBinarisation.setText(_translate("MainWindow", "Binarisation"))
        self.actionGradient.setText(_translate("MainWindow", "Gradient"))
        self.actionRobert.setText(_translate("MainWindow", "Robert"))
        self.actionPrewitt.setText(_translate("MainWindow", "Prewitt"))
        self.actionSobel.setText(_translate("MainWindow", "Sobel"))
        self.actionLaplacien.setText(_translate("MainWindow", "Laplacien"))
        self.actionCroissance_des_regions.setText(_translate("MainWindow", "Croissance des regions"))
        self.actionDilatation.setText(_translate("MainWindow", "Dilatation"))
        self.actionErosion.setText(_translate("MainWindow", "Erosion"))
        self.actionOuverture.setText(_translate("MainWindow", "Ouverture"))
        self.actionFermeture.setText(_translate("MainWindow", "Fermeture"))

        self.actionAvec_45_degre.setText(_translate("MainWindow", "Avec 45 droite"))
        self.actionAvec_45_degre_2.setText(_translate("MainWindow", "Avec 45 gauche"))
        self.actionAvec_45_degre_3.setText(_translate("MainWindow", "Avec 90 degre"))
        self.actionAvec_45_degre_4.setText(_translate("MainWindow", "Avec 45 degre"))
        self.actionAvec_90.setText(_translate("MainWindow", "Avec 90°"))
        self.actionAvec_180.setText(_translate("MainWindow", "Avec 180°"))

        self.actionx2_2.setText(_translate("MainWindow", "x2"))
        self.actionx3.setText(_translate("MainWindow", "x3"))
        self.actionHistogramme.setText(_translate("MainWindow", "Histogramme"))
        self.actionEtirement.setText(_translate("MainWindow", "Etirement"))
        self.actionEgalisation.setText(_translate("MainWindow", "Egalisation"))
        self.action5x5.setText(_translate("MainWindow", "5x5"))
        self.action7x7.setText(_translate("MainWindow", "7x7"))
        self.actions_0_1.setText(_translate("MainWindow", "s= 0.1"))
        self.actions_0_8.setText(_translate("MainWindow", "s= 0.8"))
        self.action3x3.setText(_translate("MainWindow", "3x3"))
        self.action5x5_2.setText(_translate("MainWindow", "5x5"))
        self.actionPartition_des_regions.setText(_translate("MainWindow", "Partition des regions"))
        self.actionMethode_des_K_means.setText(_translate("MainWindow", "Methode des K-means"))
        self.actionSeuillage_manuelle.setText(_translate("MainWindow", "Seuillage manuelle"))
        self.actionMethode_d_OTSU.setText(_translate("MainWindow", "Methode  d\'OTSU"))

        self.actionOuvrir.triggered.connect(self.openFile)
        #        self.actionAvec_90.triggered.connect(self.rotate90)
        #        self.actionAvec_180.triggered.connect(self.rotate180)
        self.actionNegatif.triggered.connect(self.negatif)
        self.action5x5.triggered.connect(self.Moyenneur5)
        self.action7x7.triggered.connect(self.Moyenneur7)
        self.actions_0_1.triggered.connect(self.gaussian5)
        self.actions_0_8.triggered.connect(self.gaussian7)
        self.action3x3.triggered.connect(self.median3)
        self.action5x5_2.triggered.connect(self.median5)
        self.actionGradient.triggered.connect(self.grad)
        self.actionRobert.triggered.connect(self.Robert)
        self.actionSobel.triggered.connect(self.Sobel)
        self.actionLaplacien.triggered.connect(self.laplacien)
        self.actionErosion.triggered.connect(self.Erosion)
        self.actionDilatation.triggered.connect(self.dilatation)
        self.actionOuverture.triggered.connect(self.ouverture)
        self.actionFermeture.triggered.connect(self.fermeture)
        self.actionEnregistrer_sous.triggered.connect(self.save)

        self.actionSeuillage_manuelle.triggered.connect(self.binarise)
        self.actionMethode_d_OTSU.triggered.connect(self.otsu)
        self.pushButton_4.clicked.connect(self.show_rotation)
        self.pushButton_3.clicked.connect(self.show_redimpurcentage)
        self.actionHistogramme.triggered.connect(self.histo)
        self.pushButton_2.clicked.connect(self.reset)
        self.actionCroissance_des_regions.triggered.connect(self.croissRegion)
        self.actionEtirement.triggered.connect(self.etire)
        self.actionEgalisation.triggered.connect(self.histeq)
        self.actionMethode_des_K_means.triggered.connect(self.Kmean)
        self.actionPartition_des_regions.triggered.connect(self.partRegion)

    def openFile(self):
        nom_fichier = QFileDialog.getOpenFileName(None, 'Open file', '', "Image files (*.BMP *.jpg *.gif *.png)")
        self.path = nom_fichier[0]
        pathx = self.path
        pixmap = QtGui.QPixmap(pathx)
        #        pixmap4 = pixmap.scaled(320, 320, QtCore.Qt.KeepAspectRatio)
        # pixmap4 = pixmap.scaled( 481, 461)

        self.ImageOrigine.setPixmap(pixmap)
        # self.ImageOrigine.adjustSize()
        self.ImageOrigine.setScaledContents(1)

    #    def save(self):
    #        #p = QtGui.QPixmap.grabWindow(self.ImageFinal.winId(), 0, 0, 691, 260)
    #        p = QtGui.QPixmap(self.ImageFinal)
    #        fileName = QtGui.QFileDialog.getSaveFileName(self, 'Save File', '', '*.jpg')
    #        file = open(fileName, 'w')
    #        p.save(file, "PNG")
    def save(self):
        self.fileName = QFileDialog.getSaveFileName(None, 'Save file', "Image",
                                                    "Image files ( *.png *.jpg *.BMP *.gif )")
        #            if "." not in fileName[0]:
        #            fileName[0] += ".png"

        pixmap = QtGui.QPixmap(self.ImageFinal.pixmap())
        # image = cv2.imread(pixmap)
        # pixmap.fill()
        # self.addRecentFile(fileName[0])
        self.fileName = self.fileName[0]

        # cv2.imwrite(file, pixmap)
        pixmap.save(self.fileName, "png")
        return self.save

    def reset(self):
        self.ImageOrigine.clear()
        self.ImageFinal.clear()

    def show_rotation(self):
        anglevalue = int(self.lineEdit_2.text())
        print(anglevalue)
        image = cv2.imread(self.path)
        (h, w) = image.shape[:2]
        center = (w / 2, h / 2)
        M = cv2.getRotationMatrix2D(center, anglevalue, 0.6)
        rotated = cv2.warpAffine(image, M, (h, w))
        # cv2.imshow("image rotation", rotated)
        # cv2.waitKey(0);
        # cv2.destroyAllWindows()  # destroys the window showing image
        random = randint(1, 2000)
        print(random)
        x = "image" + str(random)
        cv2.imwrite("D://image/" + x + ".png", rotated)
        pixmap = QtGui.QPixmap("D://image/" + x + ".png")
        self.ImageFinal.setPixmap(QtGui.QPixmap(pixmap))
        # self.ImageFinale.adjustSize()
        # self.ImageFinal.setScaledContents(1)
        self.label_2.setText("L\'image resultat : Rotation")
        self.label_2.adjustSize()

    def show_redimpurcentage(self):
        pourcentage = int(self.lineEdit.text())
        print(pourcentage)
        image = cv2.imread(self.path)
        scale_percent = pourcentage
        width = int(image.shape[1] * scale_percent / 100)
        height = int(image.shape[0] * scale_percent / 100)
        dim = (width, height)
        resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
        random = randint(1, 2000)
        print(random)
        x = "image" + str(random)
        cv2.imwrite("D://image/" + x + ".png", resized)
        pixmap = QtGui.QPixmap("D://image/" + x + ".png")
        # pixmap4 = pixmap.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.ImageFinal.setPixmap(pixmap)
        # self.ImageFinale.adjustSize()
        #       self.ImageFinal.setScaledContents(1)
        self.label_2.setText("L\'image resultat : Redimentionement")
        self.label_2.adjustSize()
        # cv2.imshow("redimmensionner image", resized)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

    def show_redimtaille(self):
        hauteur = int(self.lineEdit.text())
        largeur = int(self.lineEdit_2.text())
        print(hauteur)
        print(largeur)
        image = cv2.imread(self.path)
        dim = (hauteur, largeur)
        resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
        random = randint(1, 2000)
        print(random)
        x = "image" + str(random)
        cv2.imwrite("D://image/" + x + ".png", resized)
        pixmap = QtGui.QPixmap("D://image/" + x + ".png")
        # pixmap4 = pixmap.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.ImageFinal.setPixmap(pixmap)
        # self.ImageFinale.adjustSize()
        #      self.ImageFinal.setScaledContents(1)
        self.label_2.setText("L\'image resultat : Redimentionement")
        self.label_2.adjustSize()
        # cv2.imshow("redimmensionner image", resized)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

    def binarise(self):

        image_init = cv2.imread(self.path)
        gray_image = cv2.cvtColor(image_init, cv2.COLOR_BGR2GRAY)
        # Choisir l'image d'origine
        largeur = int(gray_image.shape[0])
        print('largeur=', largeur)
        hauteur = int(gray_image.shape[1])
        print('hauteur = ', hauteur)  # Affiche la taille de l'image
        # ret,thresh1 = cv2.threshold(gray_image, 120, 255, cv2.THRESH_BINARY)
        # cv2.imshow("fffffffff",thresh1)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        for i in range(1, largeur):
            for j in range(1, hauteur):
                if gray_image[i][j] <= 120:
                    gray_image[i][j] = 255
                else:
                    gray_image[i][j] = 0
        random = randint(1, 2000)
        print(random)
        x = "image" + str(random)
        cv2.imwrite("D://image/" + x + ".png", gray_image)
        pixmap = QtGui.QPixmap("D://image/" + x + ".png")
        self.ImageFinal.setPixmap(QtGui.QPixmap(pixmap))
        # self.ImageFinale.adjustSize()
        self.ImageFinal.setScaledContents(1)
        self.label_2.setText("L\'image resultat : Binarisation ")
        self.label_2.adjustSize()

    def otsu(self):
        image_init = cv2.imread(self.path)
        gray = cv2.cvtColor(image_init, cv2.COLOR_BGR2GRAY)
        pixel_number = gray.shape[0] * gray.shape[1]
        mean_weigth = 1.0 / pixel_number
        his, bins = np.histogram(gray, np.arange(0, 257))
        final_thresh = -1
        final_value = -1
        intensity_arr = np.arange(256)

        for t in bins[1:-1]:
            pcb = np.sum(his[:t])
            pcf = np.sum(his[t:])
            Wb = pcb * mean_weigth
            Wf = pcf * mean_weigth
            mub = np.sum(intensity_arr[:t] * his[:t]) / float(pcb)
            muf = np.sum(intensity_arr[t:] * his[t:]) / float(pcf)
            np.seterr(divide='ignore', invalid='ignore')
            value = Wb * Wf * (mub - muf) ** 2
            if value > final_value:
                final_thresh = t
                final_value = value

        final_img = gray.copy()
        final_img[gray > final_thresh] = 255
        final_img[gray < final_thresh] = 0
        random = randint(1, 2000)
        y = "image" + str(random)
        cv2.imwrite("D://image/" + y + ".png", final_img)
        pixmap = QtGui.QPixmap("D://image/" + y + ".png")
        self.ImageFinal.setPixmap(QtGui.QPixmap(pixmap))
        # self.ImageFinale.adjustSize()
        self.ImageFinal.setScaledContents(1)
        self.label_2.setText("L\'image resultat : Binarisation OTSU")
        self.label_2.adjustSize()

    def histo(self):
        img = cv2.imread(self.path, 0)
        equ = cv2.equalizeHist(img)
        res = np.hstack((img, equ))  # stacking images side-by-side
        cv2.imwrite('res.png', res)
        hist, bins = np.histogram(img.flatten(), 256, [0, 256])
        cdf = hist.cumsum()
        cdf_normalized = cdf * hist.max() / cdf.max()  # this line not necessary.
        plt.plot(cdf_normalized, color='b')
        plt.hist(img.flatten(), 256, [0, 256], color='r')

        plt.xlim([0, 256])
        plt.legend(('cdf', 'histogram'), loc='upper left')
        plt.savefig("D://image/out.png")
        plt.show()

        pixmap = QtGui.QPixmap("D://image/out.png")
        self.ImageFinal.setPixmap(QtGui.QPixmap(pixmap))
        self.ImageFinal.setScaledContents(1)

        # self.ImageFinal.add_subplot(111)

    def hist(self):
        image_init = cv2.imread(self.path)
        color = ('b', 'g', 'r')
        for i, col in enumerate(color):
            histr = cv2.calcHist([image_init], [i], None, [256], [0, 256])
            plt.plot(histr, color=col)
            plt.xlim([0, 256])

        plt.show()

    def histgray(self):
        image_init = cv2.imread(self.path)
        gray_image = cv2.cvtColor(image_init, cv2.COLOR_BGR2GRAY)
        Image = np.zeros(257)
        for i in range(1, gray_image.shape[0]):
            for j in range(1, gray_image.shape[1]):
                v = gray_image[i][j] + 1
                Image[v] = Image[v] + 1

        plt.plot(Image)
        plt.show()

    #    def rotate90(self):
    #        image = cv2.imread(self.path)
    #        o = Operation(image)
    #        img = o.rotate_image(90)
    #        height, width, byteValue = img.shape
    #        print(byteValue)
    #        if byteValue == 3:
    #            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
    #        else:
    #            imag = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
    #        pixmap = QtGui.QPixmap(imag)
    #        pixmap4 = pixmap.scaled(481, 461)
    #        self.ImageFinal.setPixmap(QtGui.QPixmap(pixmap))
    #        #self.ImageFinale.adjustSize()
    #        self.ImageFinal.setScaledContents(1)
    #        self.label_2.setText("L\'image resultat : rotation 90")
    #        self.label_2.adjustSize()
    #
    #
    #
    #
    #    def rotate180(self):
    #        imag = cv2.imread(self.path)
    #        o = Operation(imag)
    #        img = o.rotate_image(180)
    #        height, width, byteValue = img.shape
    #        print(byteValue)
    #        if byteValue == 3:
    #            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
    #        else:
    #            imag = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
    #        pixmap = QtGui.QPixmap(imag)
    #        pixmap4 = pixmap.scaled(481, 461)
    #        self.ImageFinal.setPixmap(QtGui.QPixmap(pixmap))
    #        #self.ImageFinale.adjustSize()
    #        self.ImageFinal.setScaledContents(1)
    #        self.label_2.setText("L\'image resultat : rotation 180")
    #        self.label_2.adjustSize()

    def negatif(self):
        image = cv2.imread(self.path)
        img = 255 - image
        height, width, byteValue = img.shape
        print(byteValue)
        if byteValue == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            imag = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(481, 461)
        self.ImageFinal.setPixmap(QtGui.QPixmap(pixmap))
        # self.ImageFinale.adjustSize()
        self.ImageFinal.setScaledContents(1)
        self.label_2.setText("L\'image resultat : negative")
        self.label_2.adjustSize()

    def Moyenneur5(self):
        image = cv2.imread(self.path)
        f = Filtrage(image)
        img = f.Moyenneur(5)
        height, width, byteValue = img.shape
        print(byteValue)
        if byteValue == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            imag = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(481, 461)
        self.ImageFinal.setPixmap(QtGui.QPixmap(pixmap))
        # self.ImageFinale.adjustSize()
        self.ImageFinal.setScaledContents(1)
        self.label_2.setText("L\'image resultat : f.moyenneur 5x5")
        self.label_2.adjustSize()

    def Moyenneur7(self):
        image = cv2.imread(self.path)
        f = Filtrage(image)
        img = f.Moyenneur(7)
        height, width, byteValue = img.shape
        print(byteValue)
        if byteValue == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            imag = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(481, 461)
        self.ImageFinal.setPixmap(QtGui.QPixmap(pixmap))
        # self.ImageFinale.adjustSize()
        self.ImageFinal.setScaledContents(1)
        self.label_2.setText("L\'image resultat : f.moyenneur 7x7")
        self.label_2.adjustSize()

    def gaussian5(self):
        image = cv2.imread(self.path)
        f = Filtrage(image)
        img = f.Gaussien(0.1)
        height, width, byteValue = img.shape
        print(byteValue)
        if byteValue == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            imag = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(481, 461)
        self.ImageFinal.setPixmap(QtGui.QPixmap(pixmap))
        # self.ImageFinale.adjustSize()
        self.ImageFinal.setScaledContents(1)
        self.label_2.setText("L\'image resultat : f.Gaussien 5x5")
        self.label_2.adjustSize()

    def gaussian7(self):
        image = cv2.imread(self.path)
        f = Filtrage(image)
        img = f.Gaussien(0.8)
        height, width, byteValue = img.shape
        print(byteValue)
        if byteValue == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            imag = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(481, 461)
        self.ImageFinal.setPixmap(QtGui.QPixmap(pixmap))
        # self.ImageFinale.adjustSize()
        self.ImageFinal.setScaledContents(1)
        self.label_2.setText("L\'image resultat : f.Gaussien 7x7")
        self.label_2.adjustSize()

    def median3(self):
        image = cv2.imread(self.path)
        f = Filtrage(image)
        img = f.Median(3)
        imag = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(481, 461)
        self.ImageFinal.setPixmap(QtGui.QPixmap(pixmap))
        # self.ImageFinale.adjustSize()
        self.ImageFinal.setScaledContents(1)
        self.label_2.setText("L\'image resultat : f.Median 3x3")
        self.label_2.adjustSize()

    def median5(self):
        image = cv2.imread(self.path)
        f = Filtrage(image)
        img = f.Median(5)
        imag = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap(imag)
        self.ImageFinal.setPixmap(QtGui.QPixmap(pixmap))
        # self.ImageFinale.adjustSize()
        self.ImageFinal.setScaledContents(1)
        self.label_2.setText("L\'image resultat : f.Median 5x5")
        self.label_2.adjustSize()

    def grad(self):
        image = cv2.imread(self.path)
        height, width, byteValue = image.shape
        print(byteValue)
        if byteValue == 3:
            imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            c = Contours(imag)
            img = c.grad(20)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            c = Contours(image)
            img = c.grad(20)
            imag = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)

        pixmap = QtGui.QPixmap(imag)
        self.ImageFinal.setPixmap(QtGui.QPixmap(pixmap))
        # self.ImageFinale.adjustSize()
        self.ImageFinal.setScaledContents(1)
        self.label_2.setText("L\'image resultat : grad")
        self.label_2.adjustSize()

    def Robert(self):
        image = cv2.imread(self.path)
        height, width, byteValue = image.shape
        print(byteValue)
        if byteValue == 3:
            imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            c = Contours(imag)
            img = c.Robert(20)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            c = Contours(image)
            img = c.Robert(20)
            imag = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)

        pixmap = QtGui.QPixmap(imag)
        self.ImageFinal.setPixmap(QtGui.QPixmap(pixmap))
        # self.ImageFinale.adjustSize()
        self.ImageFinal.setScaledContents(1)
        self.label_2.setText("L\'image resultat : Robert")
        self.label_2.adjustSize()

    def Sobel(self):
        image = cv2.imread(self.path)
        height, width, byteValue = image.shape
        print(byteValue)
        if byteValue == 3:
            imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            c = Contours(imag)
            img = c.Sobel(50)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            c = Contours(image)
            img = c.Sobel(50)
            imag = QtGui.QImage(img, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)

        pixmap = QtGui.QPixmap(imag)
        self.ImageFinal.setPixmap(QtGui.QPixmap(pixmap))
        # self.ImageFinale.adjustSize()
        self.ImageFinal.setScaledContents(1)
        self.label_2.setText("L\'image resultat : Sobel")
        self.label_2.adjustSize()

    def laplacien(self):
        image = cv2.imread(self.path)
        height, width, byteValue = image.shape
        print(byteValue)
        if byteValue == 3:
            imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            c = Contours(imag)
            img = c.Laplacien(20)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            c = Contours(image)
            img = c.Laplacien(20)
            imag = QtGui.QImage(img, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap(imag)
        self.ImageFinal.setPixmap(QtGui.QPixmap(pixmap))
        # self.ImageFinale.adjustSize()
        self.ImageFinal.setScaledContents(1)
        self.label_2.setText("L\'image resultat : laplacien")
        self.label_2.adjustSize()

    def Erosion(self):
        image = cv2.imread(self.path)
        height, width, byteValue = image.shape
        print(byteValue)
        if byteValue == 3:
            imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            m = Morphologie(imag)
            h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
            img = m.Erosion(h)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            m = Morphologie(image)
            h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
            img = m.Erosion(h)
            imag = QtGui.QImage(img, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap(imag)
        self.ImageFinal.setPixmap(QtGui.QPixmap(pixmap))
        # self.ImageFinale.adjustSize()
        self.ImageFinal.setScaledContents(1)
        self.label_2.setText("L\'image resultat : Erosion")
        self.label_2.adjustSize()

        ########################

    def dilatation(self):
        image = cv2.imread(self.path)
        height, width, byteValue = image.shape
        print(byteValue)
        if byteValue == 3:
            imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            m = Morphologie(imag)
            h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
            img = m.dilatation(h)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            m = Morphologie(image)
            h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
            img = m.dilatation(h)
            imag = QtGui.QImage(img, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap(imag)
        self.ImageFinal.setPixmap(QtGui.QPixmap(pixmap))
        # self.ImageFinale.adjustSize()
        self.ImageFinal.setScaledContents(1)
        self.label_2.setText("L\'image resultat : Dilatation")
        self.label_2.adjustSize()

    def ouverture(self):
        image = cv2.imread(self.path)
        height, width, byteValue = image.shape
        print(byteValue)
        if byteValue == 3:
            imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            m = Morphologie(imag)
            h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
            imaag = m.Erosion(h)
            m1 = Morphologie(imaag)
            h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
            img = m1.dilatation(h)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            m = Morphologie(image)
            h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
            imaag = m.Erosion(h)
            m1 = Morphologie(imaag)
            h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
            img = m1.dilatation(h)
            imag = QtGui.QImage(img, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap(imag)
        self.ImageFinal.setPixmap(QtGui.QPixmap(pixmap))
        # self.ImageFinale.adjustSize()
        self.ImageFinal.setScaledContents(1)
        self.label_2.setText("L\'image resultat : Ouverture")
        self.label_2.adjustSize()

    def fermeture(self):
        image = cv2.imread(self.path)
        height, width, byteValue = image.shape
        print(byteValue)
        if byteValue == 3:
            imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            m = Morphologie(imag)
            h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
            imaag = m.dilatation(h)
            m1 = Morphologie(imaag)
            h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
            img = m1.Erosion(h)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            m = Morphologie(image)
            h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
            imaag = m.dilatation(h)
            m1 = Morphologie(imaag)
            h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
            img = m1.Erosion(h)
            imag = QtGui.QImage(img, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap(imag)
        self.ImageFinal.setPixmap(QtGui.QPixmap(pixmap))
        # self.ImageFinale.adjustSize()
        self.ImageFinal.setScaledContents(1)
        self.label_2.setText("L\'image resultat : Fermeture")
        self.label_2.adjustSize()

    def rgb2gray(self, rgb):
        return np.dot(rgb[..., :3], [0.299, 0.587, 0.144])

    def croissRegion(self):
        image = cv2.imread(self.path)
        gray = self.rgb2gray(image)
        gray_r = gray.reshape(gray.shape[0] * gray.shape[1])
        for i in range(gray_r.shape[0]):

            if gray_r[i] > gray_r.mean():

                gray_r[i] = 255
            elif gray_r[i] > 0.5:
                gray_r[i] = 128
            elif gray_r[i] > 0.1:
                gray_r[i] = 128
            else:
                gray_r[i] = 0
        gray = gray_r.reshape(gray.shape[0], gray.shape[1])
        random = randint(1, 2000)
        print(random)
        x = "image" + str(random)
        cv2.imwrite("D://image/" + x + ".png", gray)
        pixmap = QtGui.QPixmap("D://image/" + x + ".png")
        # pixmap4 = pixmap.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.ImageFinal.setPixmap(pixmap)
        # self.ImageFinale.adjustSize()
        self.ImageFinal.setScaledContents(1)
        self.label_2.setText("L\'image resultat : Segmentation")
        self.label_2.adjustSize()

    def partRegion(self):
        image = cv2.imread(self.path)
        gray = self.rgb2gray(image)
        gray_r = gray.reshape(gray.shape[0] * gray.shape[1])
        for i in range(gray_r.shape[0]):

            if gray_r[i] > gray_r.mean():

                gray_r[i] = 255
            else:
                gray_r[i] = 0
        gray = gray_r.reshape(gray.shape[0], gray.shape[1])
        random = randint(1, 2000)
        print(random)
        x = "image" + str(random)
        cv2.imwrite("D://image/" + x + ".png", gray)
        pixmap = QtGui.QPixmap("D://image/" + x + ".png")
        # pixmap4 = pixmap.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.ImageFinal.setPixmap(pixmap)
        # self.ImageFinale.adjustSize()
        self.ImageFinal.setScaledContents(1)
        self.label_2.setText("L\'image resultat : Segmentation")
        self.label_2.adjustSize()

    #    def partRegion(self):
    #        image = cv2.imread(self.path)
    #        imag = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    #        s = Segmentation(imag)
    #        img = s.partition_regions()
    #        random = randint(1, 2000)
    #        y = "image" + str(random)
    #        cv2.imwrite("D://" + y + ".png", img)
    #        pixmap1 = QtGui.QPixmap("D://" + y + ".png")
    #        #pixmap5 = pixmap1.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
    #
    #        self.ImageFinal.setPixmap(pixmap1)
    #        #self.ImageFinale.adjustSize()
    # #       self.ImageFinal.setScaledContents(1)
    #        self.label_2.setText("L\'image resultat : Segmentation par Partition des regions")
    #        self.label_2.adjustSize()

    #    def Kmean(self):
    #        image = cv2.imread(self.path)
    #        imag = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    #        height, width, byteValue = imag.shape
    #        s = Segmentation(imag)
    #        img = s.k_means()
    #        random = randint(1, 2000)
    #        y = "image" + str(random)
    #        cv2.imwrite("D://" + y + ".png", img)
    #        pixmap1 = QtGui.QPixmap("D://" + y + ".png")
    #
    #        #pixmap5 = pixmap1.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
    #
    #        self.ImageFinal.setPixmap(pixmap1)
    #        #self.ImageFinale.adjustSize()
    # #       self.ImageFinal.setScaledContents(1)
    #        self.label_2.setText("L\'image resultat : Segmentation par Partition des regions")
    #        self.label_2.adjustSize()

    def Kmean(self):
        pic = cv2.imread(self.path)

        pic_n = pic.reshape(pic.shape[0] * pic.shape[1], pic.shape[2])
        pic_n.shape
        kmeans = KMeans(n_clusters=5, random_state=0).fit(pic_n)
        pic2show = kmeans.cluster_centers_[kmeans.labels_]
        cluster_pic = pic2show.reshape(pic.shape[0], pic.shape[1], pic.shape[2])
        pic2show = kmeans.cluster_centers_[kmeans.labels_]
        # plt.imshow(cluster_pic)
        random = randint(1, 2000)
        print(random)
        x = "image" + str(random)
        cv2.imwrite("D://image/" + x + ".png", cluster_pic)
        pixmap = QtGui.QPixmap("D://image/" + x + ".png")
        # pixmap4 = pixmap.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.ImageFinal.setPixmap(pixmap)
        # self.ImageFinale.adjustSize()
        self.ImageFinal.setScaledContents(1)
        self.label_2.setText("L\'image resultat : Segmentation par K-Means ")
        self.label_2.adjustSize()

    #    def on_mouse(self,event, x, y, flags, params):
    #        if event == cv.CV_EVENT_LBUTTONDOWN:
    #            print ('Start Mouse Position: ' + str(x) + ', ' + str(y))
    #            s_box = x, y
    #            self.boxes.append(s_box)
    #
    #
    #    def region_growing(self):
    #        self.boxes = []
    #        cv2.setMouseCallback('input', self.on_mouse, 0,)
    #        seed=self.boxes[0]
    #        img = cv2.imread(self.path)
    #        img = cv2.resize(img,(256,256))
    #
    #    #Parameters for region growing
    #        neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    #        region_threshold = 0.2
    #        region_size = 1
    #        intensity_difference = 0
    #        neighbor_points_list = []
    #        neighbor_intensity_list = []
    #
    #    #Mean of the segmented region
    #        region_mean = img[seed]
    #
    #    #Input image parameters
    #        height, width,s = img.shape
    #        image_size = height * width
    #
    #    #Initialize segmented output image
    #        segmented_img = np.zeros((height, width, 1), np.uint8)
    #
    #    #Region growing until intensity difference becomes greater than certain threshold
    #        while (intensity_difference < region_threshold) & (region_size < image_size):
    #        #Loop through neighbor pixels
    #            for i in range(4):
    #
    #            #Compute the neighbor pixel position
    #                x_new = seed[0] + neighbors[i][0]
    #                y_new = seed[1] + neighbors[i][1]
    #
    #            #Boundary Condition - check if the coordinates are inside the image
    #                check_inside = (x_new >= 0) & (y_new >= 0) & (x_new < height) & (y_new < width)
    #
    #            #Add neighbor if inside and not already in segmented_img
    #                if check_inside:
    #                    if segmented_img[x_new, y_new] == 0:
    #                        neighbor_points_list.append([x_new, y_new])
    #                        neighbor_intensity_list.append(img[x_new, y_new])
    #                        segmented_img[x_new, y_new] = 255
    #
    #        #Add pixel with intensity nearest to the mean to the region
    #            distance = abs(neighbor_intensity_list-region_mean)
    #            pixel_distance = min(distance)
    #            index = np.where(distance == pixel_distance)[0][0]
    #            segmented_img[seed[0], seed[1]] = 255
    #            region_size += 1
    #
    #        #New region mean
    #            region_mean = (region_mean*region_size + neighbor_intensity_list[index])/(region_size+1)
    #
    #        #Update the seed value
    #            seed = neighbor_points_list[index]
    #        #Remove the value from the neighborhood lists
    #            neighbor_intensity_list[index] = neighbor_intensity_list[-1]
    #            neighbor_points_list[index] = neighbor_points_list[-1]
    #         #plt.imshow(segmented_img)
    #        random = randint(1,2000)
    #        print(random)
    #        x="image"+str(random)
    #        cv2.imwrite("D://image/" + x + ".png", segmented_img)
    #        pixmap = QtGui.QPixmap("D://image/" + x + ".png")
    #        #pixmap4 = pixmap.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
    #        self.ImageFinal.setPixmap(pixmap)
    #        #self.ImageFinale.adjustSize()
    # #       self.ImageFinal.setScaledContents(1)
    #        self.label_2.setText("L\'image resultat : Segmentation par K-Means ")
    #        self.label_2.adjustSize()
    #
    #
    #        return segmented_img

    def etire(self):
        M = cv2.imread(self.path)
        MaxV = np.max(M)
        MinV = np.min(M)
        Y = np.zeros_like(M)
        m = M.shape
        for i in range(m[0]):
            for j in range(m[1]):
                Y[i, j] = (255 / (MaxV - MinV) * M[i, j] - MinV)
        plt.hist(Y.ravel(), 256, [0, 256])
        plt.savefig("D://image/out.png")
        plt.show()

        pixmap = QtGui.QPixmap("D://image/out.png")
        self.ImageFinal.setPixmap(QtGui.QPixmap(pixmap))
        self.ImageFinal.setScaledContents(1)
        self.label_2.setText("L\'image resultat : Etirement")
        self.label_2.adjustSize()

    #        random = randint(1,2000)
    #        print(random)
    #        x="image"+str(random)
    #        cv2.imwrite("D://image/" + x + ".png", Y)
    #        pixmap = QtGui.QPixmap("D://image/" + x + ".png")
    #        pixmap = QtGui.QPixmap(Y)
    #        self.ImageFinal.setPixmap(pixmap)
    #        self.ImageFinal.setScaledContents(1)

    def imhist(self, im):
        # calculates normalized histogram of an image
        m, n = im.shape
        h = [0.0] * 256
        for i in range(m):
            for j in range(n):
                h[im[i, j]] += 1
        return np.array(h) / (m * n)

    def cumsum(self, h):
        # finds cumulative sum of a numpy array, list
        return [sum(h[:i + 1]) for i in range(len(h))]

    def histeq(self):
        img = cv2.imread(self.path)
        im = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        h = self.imhist(im)
        cdf = np.array(self.cumsum(h))  # cumulative distribution function
        sk = np.uint8(255 * cdf)  # finding transfer function values
        s1, s2 = im.shape
        Y = np.zeros_like(im)
        # applying transfered values for each pixels
        for i in range(0, s1):
            for j in range(0, s2):
                Y[i, j] = sk[im[i, j]]
        H = self.imhist(Y)
        # return transformed image, original and new istogram,
        # and transform function
        plt.plot(H)
        plt.savefig("D://image/out.png")
        plt.show()

        pixmap = QtGui.QPixmap("D://image/out.png")
        self.ImageFinal.setPixmap(QtGui.QPixmap(pixmap))
        self.ImageFinal.setScaledContents(1)
        self.label_2.setText("L\'image resultat : Egalisation")
        self.label_2.adjustSize()


# plt.subplot(2, 2, 2)
# plt.imshow(img, 'gray')

# plt.subplot(2, 2, 4)

# plt.show()

# plt.imshow(gray, cmap='gray')
############################################################################
#####################################################
#####################################################
#####################################################


class Operation:
    def __init__(self, image):
        self.image = image

    def rotate_image(self, angle):
        # Get the image size
        # No that's not an error - NumPy stores image matricies backwards
        image_size = (self.image.shape[1], self.image.shape[0])
        image_center = tuple(np.array(image_size) / 2)

        # Convert the OpenCV 3x2 rotation matrix to 3x3
        rot_mat = np.vstack(
            [cv2.getRotationMatrix2D(image_center, angle, 1.0), [0, 0, 1]]
        )

        rot_mat_notranslate = np.matrix(rot_mat[0:2, 0:2])

        # Shorthand for below calcs
        image_w2 = image_size[0] * 0.5
        image_h2 = image_size[1] * 0.5

        # Obtain the rotated coordinates of the image corners
        rotated_coords = [
            (np.array([-image_w2, image_h2]) * rot_mat_notranslate).A[0],
            (np.array([image_w2, image_h2]) * rot_mat_notranslate).A[0],
            (np.array([-image_w2, -image_h2]) * rot_mat_notranslate).A[0],
            (np.array([image_w2, -image_h2]) * rot_mat_notranslate).A[0]
        ]

        # Find the size of the new image
        x_coords = [pt[0] for pt in rotated_coords]
        x_pos = [x for x in x_coords if x > 0]
        x_neg = [x for x in x_coords if x < 0]

        y_coords = [pt[1] for pt in rotated_coords]
        y_pos = [y for y in y_coords if y > 0]
        y_neg = [y for y in y_coords if y < 0]

        right_bound = max(x_pos)
        left_bound = min(x_neg)
        top_bound = max(y_pos)
        bot_bound = min(y_neg)

        new_w = int(abs(right_bound - left_bound))
        new_h = int(abs(top_bound - bot_bound))

        # We require a translation matrix to keep the image centred
        trans_mat = np.matrix([
            [1, 0, int(new_w * 0.5 - image_w2)],
            [0, 1, int(new_h * 0.5 - image_h2)],
            [0, 0, 1]
        ])

        # Compute the tranform for the combined rotation and translation
        affine_mat = (np.matrix(trans_mat) * np.matrix(rot_mat))[0:2, :]

        # Apply the transform
        result = cv2.warpAffine(
            self.image,
            affine_mat,
            (new_w, new_h),
            flags=cv2.INTER_LINEAR
        )
        img = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
        return result


class Morphologie:

    def __init__(self, image):
        self.image = image

    def dilatation(self, H):
        imagecopy = self.image.copy()
        for i in range(1, self.image.shape[0] - 1):
            for j in range(1, self.image.shape[1] - 1):
                s = 0;
                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        s = s + self.image[k, l] * H[k - i + 1][l - j + 1]
                if (s == 0):
                    imagecopy[i][j] = 0
                else:
                    imagecopy[i][j] = 255
        return imagecopy

    def Erosion(self, H):
        imagecopy = self.image.copy()

        for i in range(0, self.image.shape[0]):
            for j in range(0, self.image.shape[1]):
                if (self.image[i][j] > 128):
                    self.image[i][j] = 255
                else:
                    self.image[i][j] = 0

        for i in range(1, self.image.shape[0] - 1):
            for j in range(1, self.image.shape[1] - 1):
                s = 0;
                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        s = s + self.image[k, l] * H[k - i + 1][l - j + 1]
                if (s == 2295):
                    imagecopy[i][j] = 255
                else:
                    imagecopy[i][j] = 0
        return imagecopy

    def Ouverture(self, H):
        img = self.Erosion(self.image, H)
        image1 = self.dilatation(img, H)
        return image1

    def Fermeture(self, H):
        img = self.Erosion(self.image, H)
        image1 = self.dilatation(img, H)
        return image1


class Filtrage:
    def __init__(self, image):
        self.image = image

    def Moyenneur(self, taille):
        imagefiltrage = self.image.copy()
        x = int((taille - 1) / 2)
        for i in range(x, self.image.shape[0] - x):
            for j in range(x, self.image.shape[1] - x):
                s = 0
                for n in range(-x, x):
                    for m in range(-x, x):
                        s += self.image[i + n, j + m] / (taille * taille)
                imagefiltrage[i, j] = s
                s = 0
        return imagefiltrage

    def Median(self, taille):
        imagefiltrage = self.image.copy()
        x = int((taille - 1) / 2)
        for i in range(x, self.image.shape[0] - x):
            for j in range(x, self.image.shape[1] - x):
                liste = []
                for n in range(-x, x):
                    for m in range(-x, x):
                        liste.append(imagefiltrage[i + n, j + m])
                liste.sort()
                imagefiltrage[i, j] = liste[x + 1]
                while len(liste) > 0: liste.pop()
        return imagefiltrage

    def h(self, x, y, v):
        x = (1 / (2 * math.pi * math.pow(v, 2))) * (math.exp(-(math.pow(x, 2) + math.pow(y, 2)) / (2 * math.pow(v, 2))))
        return x

    def Gaussien(self, v):
        imagefiltrage = self.image.copy()
        x = 1
        for i in range(x, self.image.shape[0] - x):
            for j in range(x, self.image.shape[1] - x):
                s = 0
                for a in range(-x, x):
                    for b in range(-x, x):
                        s = s + self.h(a, b, v) * self.image[i + a, j + b]
                imagefiltrage[i, j] = s
                s = 0
        return imagefiltrage


class Contours:

    def __init__(self, image):
        self.image = image

    def grad(self, seuil):
        imageX = self.image.copy()
        imageY = self.image.copy()
        for i in range(1, self.image.shape[0] - 1):
            for j in range(1, self.image.shape[1] - 1):
                imageX[i, j] = self.image[i, j + 1] - self.image[i, j]
                imageY[i, j] = self.image[i + 1, j] - self.image[i, j]
        imageXY = self.image.copy()
        for i in range(1, self.image.shape[0] - 1):
            for j in range(1, self.image.shape[1] - 1):
                imageXY[i, j] = sqrt(imageX[i, j] ** 2 + imageY[i, j] ** 2)
                if imageXY[i, j] < seuil:
                    imageXY[i, j] = 0
                else:
                    imageXY[i, j] = 255
        return imageXY

    def Robert(self, seuil):
        imageX = self.image.copy()
        imageY = self.image.copy()
        for i in range(1, self.image.shape[0] - 1):
            for j in range(1, self.image.shape[1] - 1):
                imageX[i, j] = self.image[i, j] - self.image[i - 1, j - 1]
                imageY[i, j] = self.image[i, j] - self.image[i + 1, j + 1]
        imageXY = self.image.copy()
        for i in range(1, self.image.shape[0] - 1):
            for j in range(1, self.image.shape[1] - 1):
                imageXY[i, j] = sqrt(imageX[i, j] ** 2 + imageY[i, j] ** 2)
                if imageXY[i, j] < seuil:
                    imageXY[i, j] = 0
                else:
                    imageXY[i, j] = 255
        return imageXY

    def Sobel(self, seuil):
        imageX = self.image.copy()
        imageY = self.image.copy()
        for i in range(1, self.image.shape[0] - 1):
            for j in range(1, self.image.shape[1] - 1):
                imageY[i, j] = -self.image[i - 1, j - 1] - 2 * self.image[i, j - 1] - self.image[i + 1, j - 1] \
                               + self.image[i - 1, j + 1] + 2 * self.image[i, j + 1] + self.image[i + 1, j + 1]
                imageX[i, j] = self.image[i - 1, j - 1] + 2 * self.image[i - 1, j] + self.image[i - 1, j + 1] \
                               - self.image[i + 1, j - 1] - 2 * self.image[i + 1, j] - self.image[i + 1, j + 1]
        imageXY = self.image.copy()
        for i in range(1, self.image.shape[0] - 1):
            for j in range(1, self.image.shape[1] - 1):
                imageXY[i, j] = sqrt(imageX[i, j] ** 2 + imageY[i, j] ** 2)
                if imageXY[i, j] < seuil:
                    imageXY[i, j] = 0
                else:
                    imageXY[i, j] = 255
        return imageXY

    def Laplacien(self, seuil):
        imageXY = self.image.copy()
        for i in range(1, self.image.shape[0] - 1):
            for j in range(1, self.image.shape[1] - 1):
                imageXY[i, j] = -4 * self.image[i, j] + self.image[i - 1, j] + self.image[i + 1, j] \
                                + self.image[i, j - 1] + self.image[i, j + 1]
                if imageXY[i, j] < seuil:
                    imageXY[i, j] = 0
                else:
                    imageXY[i, j] = 255
        return imageXY

    def blur(image):
        F = image.copy()
        N, M = image.shape
        h = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        for i in range(2, N - 2):
            for j in range(2, M - 2):
                s = 0
                for n in range(-1, 1):
                    for m in range(-1, 1):
                        s += h[n + 1][m + 1] * image[i + n][j + m]

                F[i][j] = s

        return F

    def Moyenneur(image, taille):
        imagefiltrage = image.copy()
        x = int((taille - 1) / 2)
        for i in range(x, image.shape[0] - x):
            for j in range(x, image.shape[1] - x):
                s = 0
                for n in range(-x, x):
                    for m in range(-x, x):
                        s += image[i + n, j + m] / (taille * taille)
                imagefiltrage[i, j] = s
                s = 0
        return imagefiltrage


class Segmentation:

    def __init__(self, image):
        self.image = image

    def k_means(self):

        # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        pixel_values = self.image.reshape((-1, 3))
        # convert to float
        pixel_values = np.float32(pixel_values)
        # pixel_values = np.float32(image)

        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)

        k = 3
        # attempts=10
        ret, labels, (centers) = cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

        centers = np.uint8(centers)

        segmented_image = centers[labels.flatten()]

        segmented_image = segmented_image.reshape(self.image.shape)

        return segmented_image

    def partition_regions(self):
        # gray = rgb2gray(image)
        gray_r = self.image.reshape(self.image.shape[0] * self.image.shape[1])
        for i in range(gray_r.shape[0]):
            if gray_r[i] > gray_r.mean():
                gray_r[i] = 3
            elif gray_r[i] > 0.5:
                gray_r[i] = 2
            elif gray_r[i] > 0.25:
                gray_r[i] = 1
            else:
                gray_r[i] = 0
        gray = gray_r.reshape(self.image.shape[0], self.image.shape[1])
        plt.imshow(gray, cmap='gray')
        return gray


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

