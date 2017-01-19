#Creates a button in the Slicer Window that prints "Button clicked!" in the console
def createButton():
	self.newButton = qt.QPushButton("New Button!")
    button.show()
	newButton.connect('clicked(bool)', onPressNewButton())
    
def onPressNewButton():
	print("Button clicked!")

createButton()
	