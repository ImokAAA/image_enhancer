from django.test import TestCase

####### CORE IMPORTS ###############
from ml.ml_service import ML

class MLTests(TestCase):

    def test_fsrcnnx3_model(self):
        """ This method tests the FSRCNN x3 model """
        test_image_path = '/home/imangali/Documents/django-projects/image_enhancer/backend/server/ml/test.jpg'
        image = ML.get_image_with_path(test_image_path = test_image_path)

        initial_height = image.shape[0]
        initial_width = image.shape[1]

        upscaled_image = ML.upScaleFSRCNN(image)
        ML.save("test_result",upscaled_image)

        final_height = upscaled_image.shape[0]
        final_width = upscaled_image.shape[1]

        final_height_expected = initial_height * 3
        final_width_expected = initial_width * 3

        self.assertEqual(final_height, final_height_expected)
        self.assertEqual(final_width, final_width_expected)
        