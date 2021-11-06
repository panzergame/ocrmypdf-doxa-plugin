from ocrmypdf import hookimpl, PageContext
import argparse
import numpy as np
import doxapy
from PIL import Image


@hookimpl
def add_options(parser: argparse.ArgumentParser):
	parser.add_argument(
		'--doxa-algorithm',
		metavar='NAME',
		default='WAN',
		choices=doxapy.Binarization.Algorithms.__members__.keys(),
		help='Algortihm name used for binarization'
	)
	parser.add_argument(
		'--doxa-parameters',
		nargs='*',
		metavar='KEY=VALUE',
		help='Binarization parameters'
	)


def parse_parameter(raw_parameter: str):
	key, value = raw_parameter.split('=')
	return key, int(value) if value.isnumeric() else float(value)


def parse_parameters(raw_parameters: list) -> dict:
	return dict(parse_parameter(pair) for pair in raw_parameters)


@hookimpl
def filter_ocr_image(page: PageContext, image: Image.Image):
	algorithm = doxapy.Binarization.Algorithms.__members__[page.options.doxa_algorithm]
	parameters = parse_parameters(page.options.doxa_parameters)

	# Convert input image into grayscale
	image_array = np.array(image.convert('L'))

	# Pick an algorithm from the DoxaPy library and convert the image to binary
	doxapy.Binarization.update_to_binary(algorithm, image_array, parameters)

	binary_image = Image.fromarray(image_array)
	binary_image.info['dpi'] = image.info['dpi']
	return binary_image
