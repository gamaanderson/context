echo $1
python3 $1.py > $1.tex
export HOME='/home/gama'
eval $(printenv | awk -F= '{ print "export " $1 }')
pdflatex -synctex=1 -interaction=nonstopmode $1.tex

