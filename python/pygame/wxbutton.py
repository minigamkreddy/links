import wx


class Interface(wx.Frame):
    def __init__(self, parent, title):
        super(Interface, self).__init__(parent, title=title, size=(300, 400))

        # Show the window on screen
        self.setup()
        self.Show()

    def setup(self):
        box = wx.BoxSizer(wx.VERTICAL)
        self.textbox = wx.TextCtrl(self, style=wx.TE_RIGHT)
        box.Add(self.textbox, flag=wx.EXPAND | wx.TOP | wx.BOTTOM, border=4)

        grid = wx.GridSizer(5, 4, 10, 10)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', 'C', '+',
            '='
        ]

        for label in buttons:
            button = wx.Button(self, -1, label)
            grid.Add(button, 0, wx.EXPAND)
            self.Bind(wx.EVT_BUTTON, self.on_button_press, button)

        box.Add(grid, proportion=1, flag=wx.EXPAND)
        self.SetSizer(box)

    def on_button_press(self, e):

        # Get label of button
        label = e.GetEventObject().GetLabel()

        # Get the input from the TextCtrl
        calculation = self.textbox.GetValue()

        # Handle the event based on the button pressed
        if label == '=':  # Calculate the result of the input in the TextCtrl
            # Ignore an empty calculation
            if not calculation:
                return

            try:
                # Calculate the result
                result = eval(calculation)
            except SyntaxError as err:  # Catch any input errors (e.g. '6 +* 2')
                wx.LogError('Invalid syntax ({}). Please check your input and try again.'.format(calculation))
                return
            except NameError as err:  # Catch any manually typed errors (e.g. '2 x three')
                wx.LogError('There was a error. Please check your input and try again.')
                return

            # Show the result
            self.textbox.SetValue(str(result))
        elif label == 'C':  # Clear the TextCtrl
            self.textbox.SetValue('')
        else:  # 0-9 (and .)
            # Add the label of the button press to the current calculation in the TextCtrl
            self.textbox.SetValue(calculation + label)


if __name__ == '__main__':
    # Create the application object
    app = wx.App()
    Interface(None, title='Calculator')

    app.MainLoop()

