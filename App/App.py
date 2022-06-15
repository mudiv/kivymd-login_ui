#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------
# Telegram : @DIBIBl , @TDTDI ,@ruks3
# Coded by ruks
# YouTube : https://youtube.com/channel/UCUNbzQRjfAXGCKI1LY72DTA
# Instagram : https://instagram.com/_v_go?utm_medium=copy_link
# github : https://github.com/muntazir-halim
# ---------------------
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
Window.softinput_mode = "below_target"


class App(MDApp): 
	def build(self):
		
		return Builder.load_file("ui.kv")    
		


if __name__ == '__main__':    
    App().run()   
