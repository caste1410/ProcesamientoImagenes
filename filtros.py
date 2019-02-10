#########Librerias######################
import sys
import cv2
import numpy
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog, QGridLayout
from PyQt5.QtCore import Qt
########################################

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.image = None
        self.original = None
        self.label = QLabel()
        self.initUI()

    def initUI(self):
        self.label.setText('OpenCV Image')
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet('border: gray; border-style:solid; border-width: 1px;')

        btn_open = QPushButton('Abir Imagen...')
        btn_open.clicked.connect(self.abrirImagen)

        btn_original = QPushButton('Original')
        btn_original.clicked.connect(self.getOriginal)

        btn_inverse = QPushButton('Inverse')
        btn_inverse.clicked.connect(self.getInverse)


        btn_threshold = QPushButton('Threshold')
        btn_threshold.clicked.connect(self.getThreshold)

        btn_tInverted = QPushButton('Threshold Inverted')
        btn_tInverted.clicked.connect(self.getTI)

        btn_add = QPushButton('Suma')
        btn_add.clicked.connect(self.getAdd)

        btn_res = QPushButton('Resta')
        btn_res.clicked.connect(self.getRes)


        btn_lap = QPushButton('Laplacian')
        btn_lap.clicked.connect(self.getLaplacian)

        btn_red = QPushButton('Canal Rojo')
        btn_red.clicked.connect(self.getRed)

        btn_green = QPushButton('Canal Verde')
        btn_green.clicked.connect(self.getGreen)

        btn_blue = QPushButton('Canal Azul')
        btn_blue.clicked.connect(self.getBlue)

        btn_rblue = QPushButton('Canales Rojo y Azul')
        btn_rblue.clicked.connect(self.getRedBlue)

        btn_rgreen = QPushButton('Canales Rojo y Verde')
        btn_rgreen.clicked.connect(self.getRedGreen)

        btn_bgreen = QPushButton('Canales Azul y Verde')
        btn_bgreen.clicked.connect(self.getBlueGreen)

        btn_gris = QPushButton('Escala de grises')
        btn_gris.clicked.connect(self.getGray)

        btn_canny = QPushButton('Canny')
        btn_canny.clicked.connect(self.getCanny)

        btn_photo = QPushButton('Tomar Foto')
        btn_photo.clicked.connect(self.getPhoto)

        btn_salvar = QPushButton('Guardar')
        btn_salvar.clicked.connect(self.getSave)

        top_bar = QGridLayout()
        top_bar.addWidget(btn_open,0,0)
        top_bar.addWidget(btn_original,0,1)
        top_bar.addWidget(btn_inverse,0,2)
        top_bar.addWidget(btn_threshold,0,3)
        top_bar.addWidget(btn_tInverted,1,0)
        top_bar.addWidget(btn_add,1,1)
        top_bar.addWidget(btn_res,1,2)
        top_bar.addWidget(btn_lap,1,3)
        top_bar.addWidget(btn_red,2,0)
        top_bar.addWidget(btn_green,2,1)
        top_bar.addWidget(btn_blue,2,2)
        top_bar.addWidget(btn_rblue,2,3)
        top_bar.addWidget(btn_rgreen,3,0)
        top_bar.addWidget(btn_bgreen,3,1)
        top_bar.addWidget(btn_gris,3,2)
        top_bar.addWidget(btn_canny,3,3)
        top_bar.addWidget(btn_photo,4,0)
        top_bar.addWidget(btn_salvar,4,1)





        root = QVBoxLayout(self)
        root.addLayout(top_bar)
        root.addWidget(self.label)

        self.resize(540, 574)
        self.setWindowTitle('Filtros')

    def abrirImagen(self):
        filename, _ = QFileDialog.getOpenFileName(None, 'Buscar Imagen', '.', 'Image Files (*.png *.jpg *.jpeg *.bmp)')
        if filename:
            with open(filename, "rb") as file:

                imagen = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
                self.original = cv2.resize(imagen, (0, 0), None, .90, .90)
                self.image = self.original
                self.mostrarImagen()

    def getOriginal(self):
        if self.image is not None:
            self.image = self.original
            self.mostrarImagen()

    def getInverse(self):
        if self.image is not None:
            self.image =(255-self.image)
            self.mostrarImagen()

    def getThreshold(self):
        if self.image is not None:
            _,thresh = cv2.threshold(self.image,100,200,cv2.THRESH_BINARY)
            self.image = thresh
            self.mostrarImagen()
    def getTI(self):
        if self.image is not None:
            _,thresh = cv2.threshold(self.image,127,255,cv2.THRESH_BINARY_INV)
            self.image = thresh
            self.mostrarImagen()

    def getAdd(self):
        if self.image is not None:
            filename, _ = QFileDialog.getOpenFileName(None, 'Buscar Imagen', '.', 'Image Files (*.png *.jpg *.jpeg *.bmp)')
            if filename:
                with open(filename, "rb") as file:
                    imagen = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
                    imagen = cv2.resize(imagen, (0, 0), None, .50, .50)
                    self.image = cv2.add(self.image,imagen)
                    self.mostrarImagen()
    def getRes(self):
        if self.image is not None:
            filename, _ = QFileDialog.getOpenFileName(None, 'Buscar Imagen', '.', 'Image Files (*.png *.jpg *.jpeg *.bmp)')
            if filename:
                with open(filename, "rb") as file:
                    imagen = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
                    imagen = cv2.resize(imagen, (0, 0), None, .50, .50)
                    self.image = cv2.absdiff(self.image,imagen)
                    self.mostrarImagen()
    def getLaplacian(self):
        if self.image is not None:
            laplace = cv2.Laplacian(self.image, cv2.CV_64F)
            laplace = cv2.resize(laplace, (0, 0), None, 2, 2)
            cv2.imwrite("laplacian.jpg",laplace)
            laplace = cv2.imread("laplacian.jpg", cv2.IMREAD_UNCHANGED)
            self.image = cv2.resize(laplace, (0, 0), None, 0.5, 0.5)
            self.mostrarImagen()

    def getRed(self):
        b,g,r = cv2.split(self.image)
        self.image = cv2.merge((b-b,g-g,r))
        self.mostrarImagen()

    def getGreen(self):
        b,g,r = cv2.split(self.image)
        self.image = cv2.merge((b-b,g,r-r))
        self.mostrarImagen()

    def getBlue(self):
        b,g,r = cv2.split(self.image)
        self.image = cv2.merge((b,g-g,r-r))
        self.mostrarImagen()

    def getRedBlue(self):
        b,g,r = cv2.split(self.image)
        self.image = cv2.merge((b,g-g,r))
        self.mostrarImagen()

    def getRedGreen(self):
        b,g,r = cv2.split(self.image)
        self.image = cv2.merge((b-b,g,r))
        self.mostrarImagen()

    def getBlueGreen(self):
        b,g,r = cv2.split(self.image)
        self.image = cv2.merge((b,g,r-r))
        self.mostrarImagen()

    def getGray(self):
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.image = cv2.cvtColor(self.image, cv2.COLOR_GRAY2BGR)
        self.mostrarImagen()

    def getCanny(self):
        self.image = cv2.Canny(self.image, 100, 200)
        self.image = cv2.cvtColor(self.image, cv2.COLOR_GRAY2BGR)
        self.mostrarImagen()

    def getPhoto(self):
        cap = cv2.VideoCapture(1)
        _, self.original = cap.read()
        cap.release()
        self.original = cv2.resize(self.original, (0, 0), None, .50, .50)
        self.image = self.original
        self.mostrarImagen()

    def getSave(self):
        #self.image = cv2.resize(self.image, (0, 0), None, 2, 2)
        cv2.imwrite("imagen.jpg",self.image)
        self.image = cv2.resize(self.image, (0, 0), None, .50, .50)



    def mostrarImagen(self):
        size = self.image.shape
        step = self.image.size / size[0]
        qformat = QImage.Format_Indexed8

        if len(size) == 3:
            if size[2] == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888

        img = QImage(self.image, size[1], size[0], step, qformat)
        img = img.rgbSwapped()

        self.label.setPixmap(QPixmap.fromImage(img))
        self.resize(self.label.pixmap().size())

def main ():
    app = QApplication(sys.argv)
    win = Example()
    win.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()
