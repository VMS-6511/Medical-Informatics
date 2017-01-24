#Creates a button in the Slicer Window that prints "Button clicked!" in the Python console
def createButton():
	self.newButton = qt.QPushButton("New Button!")
    button.show()
	newButton.connect('clicked(bool)', onPressNewButton())
    
def onPressNewButton():
	print("Button clicked!")

#Creates a transform node that translates
def createTransform():
	translationTransformNode = slicer.vtkMRMLLinearTransformNode()
	translationTransform = translationTransformNode.GetTransformToParent()
	translationTransform.Identity()
	translationTransform.translate(0,0,0)
	translationTransform.Modified()

createButton()
createTransform()
	