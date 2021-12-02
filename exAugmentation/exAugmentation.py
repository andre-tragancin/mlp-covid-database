import os, sys
import shutil 
from time import sleep
import cv2
from skimage import measure
import numpy as np
#from PyZenity import InfoMessage

# Aqui temos a geracao de um novo conjunto de imagens a partir de rotacoes sobre as originais
#https://stackoverflow.com/questions/1635027/whats-the-simplest-cross-platform-way-to-pop-up-graphical-dialogs-in-python

def pause():
  sys.stdin.readline()
  print('space was pressed, continuing...')

#https://stackoverflow.com/questions/39748916/find-maximum-value-and-index-in-a-python-list

def rotate_(img, ang): 
	#img = cv2.imread('messi5.jpg',0)
	rows,cols = img.shape
	if ang== 'flip':
		dst=cv2.flip(img, 1) 
	else:	
		
		M = cv2.getRotationMatrix2D((cols/2,rows/2),int(ang),1)
		dst = cv2.warpAffine(img,M,(cols,rows))
	return dst

"""
Aplica rotacoes para aumento da base de dados. 
Segmenta a regiao da mama e salva esta imagem na respectiva pasta criada.
A ideia eh poder acessar cada imagem individual por meio de um script que
leia uma relacao de nomes de imagens (imagens normais, por exemplo)
"""




if __name__ == "__main__":	
	# Open a file
	srcPath='/content/drive/MyDrive/Colab Notebooks/"
	destPath=srcPath+'dest/'
	dirs = os.listdir( srcPath )
	k=0
	# This would print all the files and directories
	f=[];
	for (dirpath, dirnames, filenames) in os.walk(srcPath):
		f.extend(filenames);
		break;
	print(f);
	#pause()
	for fileName in f:
		if fileName.endswith(".png"):
				print(fileName, type(fileName))
				#pause()    
				fileName=fileName.split('.')
				angs=['5',  '10', '15', 'flip']# 'flip' eh um flag para flipping vertical
				for c in angs:
       imgDestPathName= destPath+fileName[0]+"_R"+c+'.'+fileName[1];
					imgSrcPath=srcPath+fileName[0]+'.'+fileName[1];
					im = cv2.imread(imgSrcPath, cv2.IMREAD_GRAYSCALE)
					imgOut=rotate_(im,c)
					try:
							cv2.imwrite(imgDestPathName, imgOut)
					except IOError as e:
							print('4) Error: %s' % e.strerror)	
							pause()
							exit
					print('\n\n')		
	
