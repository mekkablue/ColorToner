# encoding: utf-8
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/Reporter

from __future__ import division, print_function, unicode_literals
import objc
from GlyphsApp import *
from GlyphsApp.plugins import *

class ColorToner(ReporterPlugin):
	@objc.python_method
	def start(self):
		Glyphs.registerDefault("com.mekkablue.ColorToner.darken", 0.15)

	@objc.python_method
	def settings(self):
		self.menuName = Glyphs.localize({
			'en': 'Darkened Colors',
			'de': 'Abgedunkelte Farben',
			})

	@objc.python_method
	def background(self, layer):
		tone = float(Glyphs.defaults["com.mekkablue.ColorToner.darken"]) % 1.0
		NSColor.blackColor().colorWithAlphaComponent_(tone).set()
		for shape in layer.shapes:
			if shape.shapeType == GSShapeTypeComponent:
				shape.bezierPath.fill()

	@objc.python_method
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
