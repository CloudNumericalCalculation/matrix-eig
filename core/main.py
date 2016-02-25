#coding: utf-8
from __future__ import division
import sys
import numpy as np
import math

def getMatrixString(idx):
	A = data[idx].replace("\n", ";")
	while A[-1:] == ";":
		A = A[:-1]
	return A

data = input()
try:
	A = np.matrix(getMatrixString("A"))
except:
	print "矩阵格式错误！"
	sys.exit(1)

def to_latex_bmatrix(A):
	n, m = A.shape
	latexStr = "\\begin{bmatrix}"
	for i in range(0, n):
		for j in range(0, m - 1):
			latexStr += "%s&" % (str(A[i, j]))
		latexStr += "%s\\\\\\\\" % (str(A[i, m - 1]))
		# 由于markdown的缘故，所以需要输出4个`\`供markdown转义
	latexStr += "\end{bmatrix}"
	return latexStr

n, m = A.shape
if n == m:
	w, B = np.linalg.eig(A)
	w = w.round(4)
	B = B.round(4)
	for i in range(0, len(w)):
		print "$$\\lambda\_{%d} = %s, \\alpha\_{%d} = %s$$\n\n" % (i + 1, str(w[i]), i + 1, to_latex_bmatrix(B[:, i]))
else:
	print "$$%s 不是方阵！$$\n\n" % (to_latex_bmatrix(A))
sys.exit(0)
