import sys
import pandas as pd
from PyQt5 import QtWidgets
from gMain import Ui_MainWindow
from gResult import Ui_Form
from movie_recommender import main as get_similar_movies


def search():
	search_ui = Ui_Form()
	search_ui.setupUi(widget)

	tw = search_ui.tree_result
	tw.setHeaderLabels(["Ranking", "Movie Title", "Director", "Genres", "Release Date", "Cast"])

	movies = get_similar_movies()
	for i in range(movies.shape[0]):
		QtWidgets.QTreeWidgetItem(tw, 
			[str(i+1), str(movies.iloc[i]["original_title"]), str(movies.iloc[i]["director"]),
			 str(movies.iloc[i]["genres"]), str(movies.iloc[i]["release_date"]), str(movies.iloc[i]["cast"])]
			)
	
	widget.show()
	return None


app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()
widget = QtWidgets.QWidget()

ui = Ui_MainWindow()
ui.setupUi(window)
ui.search_btn.clicked.connect(search)

window.show()
sys.exit(app.exec_())