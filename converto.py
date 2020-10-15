'''
Module name: Converto.py
Author: Ebeledike C. Frank
purpose: A multi-purpose application; Calculator and Unit_Converter
'''

# File name: converto.py
import kivy
import math
from math import sin as sine, tan as tangent, cos as cosine, radians as rad
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
kivy.require('1.10.1')
from kivy.app import App
from kivy.lang import Builder
from kivy.logger import Logger
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout

class ScreenManagement(ScreenManager):
    pass

class Func(object):

    # defines the "DEl" key
    def delete(self, calculate):
        if calculate:
            calculate = list(calculate)
            calculate[-1] = ""
            self.display.text = "".join(calculate)

    #defines the "exit" key
    def exit(self):
        App.get_running_app().stop()
        Window.close()

class CalcScreen(Func, GridLayout, Screen):
    # defines the "=" key
    def calc(self, calculate):
        if calculate:
            try:
                self.display.text = str(eval(calculate))
            except:
                self.display.text = "Error"

class ConScreen(Func, GridLayout, Screen):
    # defines the "=" key
    def calc(self, calculate):
        try:
            #it gets the value of the left text and transforms it to metre and stores it in the variable "value"
            if self.disLeft.text == "Meter":
                value = float(eval(self.display.text))
            else:
                if self.disLeft.text == "Kilometer":
                    value = float(eval(self.display.text)) * 1000
                else:
                    if self.disLeft.text == "Centimeter":
                        value = float(eval(self.display.text)) / 100
                    else:
                        if self.disLeft.text == "Millimeter":
                            value = float(eval(self.display.text)) / 1000
                        else:
                            if self.disLeft.text == "Feet":
                                value = float(eval(self.display.text)) * 0.3048
                            else:
                                if self.disLeft.text == "Decimeter":
                                    value = float(eval(self.display.text)) / 10
                                else:
                                    pass
            #it gets the value of the right text and transforms it to metre and stores it in the variable "value"
            if self.disRight.text == "Kilometer":
                value = Kilometer(value)
            else:
                if self.disRight.text == "Centimeter":
                    value = Centimeter(value)
                else:
                    if self.disRight.text == "Millimeter":
                        value = Millimeter(value)
                    else:
                        if self.disRight.text == "Feet":
                            value = Feet(value)
                        else:
                            if self.disRight.text == "Decimeter":
                                value = Decimeter(value)
                            else:
                                pass
            self.display.text = str(eval(calculate))
            self.display2.text = str(value)
        except:
            self.display2.text = "Error"

class AboutScreen(Screen, Func):
    pass

# defines the "sin" key
def sin(x):
        return sine(rad(x))

# defines the "cos" keys
def cos(x):
        return sin(90-x)

# defines the "tan" key
def tan(x):
        return tangent(rad(x))


def Kilometer(x):
    return x/1000
def Centimeter(x):
    return x*100
def Millimeter(x):
    return x*1000
def Feet(x):
    return x/0.3048
def Decimeter(x):
    return x*10


presentation = Builder.load_file("design.kv")

class Converto(App):
    def on_stop(self):
        Logger.critical("Good Bye")
    def build(self):
        return presentation


if __name__ in ("__main__", "__android__"):
    Converto().run()

