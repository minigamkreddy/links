import wx

class Interface(wx.Frame):
    def __init__(self, parent, title):
        super(Interface, self).__init__(parent, title=title)

        # Show the window on screen
	self.setup()
        self.Show()

    def setup(self):
        box = wx.BoxSizer(wx.VERTICAL)
        grid = wx.GridSizer(1, 4, 10, 10)

        grid.AddMany([
            (wx.Button(self, label='+'), 0, wx.EXPAND),
            (wx.Button(self, label='-'), 0, wx.EXPAND),
            (wx.Button(self, label='x'), 0, wx.EXPAND),
            (wx.Button(self, label='/'), 0, wx.EXPAND),
        ])

        box.Add(grid, proportion=1, flag=wx.EXPAND)
        self.SetSizer(box)

if __name__ == '__main__':
    # Create the application object
    app = wx.App()
    Interface(None, title='Calculator')

    app.MainLoop()
