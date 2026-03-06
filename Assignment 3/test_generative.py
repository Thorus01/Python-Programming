from __future__ import annotations
import unittest
from generative import flatten_image, unflatten_image, check_adjacent_for_one, pixel_flip, write_image, generate_new_images
from ai import read_image


class TestGenerative(unittest.TestCase):
    """Unit tests for the module generative.py"""

    def test_flatten_image(self) -> None:
        """
        Verify output of flatten_image for at least three different sizes of images.
        """
        image_3x3 = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
        ]

        image_5x5 = [
        [1, 0, 0, 0, 1],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [1, 0, 0, 0, 1]
        ]

        image_6x6 = [
        [1, 0, 0, 0, 1, 0],
        [0, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 0, 1],
        [0, 1, 0, 1, 0, 0],
        [1, 0, 0, 0, 1, 1],
        [0, 0, 1, 1, 0, 1]
        ]

        #checks a 3x3, 5x5, and 6x6 image
        assert flatten_image(image_3x3) == [1, 0, 0, 0, 1, 0, 0, 0, 1]
        assert flatten_image(image_5x5) == [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1]
        assert flatten_image(image_6x6) == [1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1]

        # raise NotImplementedError
        

    def test_unflatten_image(self) -> None:
        """
        Verify output of unflatten_image for at least three different sizes of flattened images.
        """

        image_3x3 = [1, 0, 0, 0, 1, 0, 0, 0, 1]
        image_5x5 = [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1]
        image_6x6 = [1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1]
        #checks a 3x3, 5x5, and 6x6 image
        assert unflatten_image(image_3x3) == [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
        ]

        assert unflatten_image(image_5x5) == [
        [1, 0, 0, 0, 1],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [1, 0, 0, 0, 1]
        ]

        assert unflatten_image(image_6x6) == [
        [1, 0, 0, 0, 1, 0],
        [0, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 0, 1],
        [0, 1, 0, 1, 0, 0],
        [1, 0, 0, 0, 1, 1],
        [0, 0, 1, 1, 0, 1]
        ]

        # raise NotImplementedError


    def test_check_adjacent_for_one(self) -> None:
        """
        Verify output of check_adjacent_for_one for three different pixel indexes of an image representing different scenarios.
        """
        #defining test parameters
        image = [
        [1, 0, 0],
        [1, 0, 0],
        [1, 1, 1],
        ]
        flat_image = flatten_image(image)

        #tests for positions 2, 4, and 5
        assert check_adjacent_for_one(flat_image, 2) == False
        assert check_adjacent_for_one(flat_image, 4) == True
        assert check_adjacent_for_one(flat_image, 5) == True

        # raise NotImplementedError


    def test_pixel_flip(self) -> None:
        """
        Verify output of pixel_flip for a 5x5 image with a budget of 2.
        """

        #defining test parameters
        test_list = flatten_image([
        [1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 0, 0, 0, 1]
        ])

        budget = 2
        #calls the function and tests the results
        results = []
        pixel_flip(test_list, test_list, budget, results)
        assert results == [[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1], [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1], [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1], [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1]]

        # raise NotImplementedError


    def test_generate_new_images(self) -> None:
        """
        Verify generate_new_images with image.txt and for each image of the generated images verify that:
        - image is of size 28x28,
        - all values in the generated image are either 1s or 0s,
        - the number of pixels flipped from original image are within budget,
        - all pixels flipped from the original image had an adjacent value of 1.
        """
        #defining test parameters
        test_image = read_image("image.txt")
        budget = 2
        #creates the list of images to be checked
        image_list = generate_new_images(test_image, budget)

        for image in range(len(image_list)):    #iterates through each image
            budget_usage = 0 #counter of pixels
            #verifies that image size is 28x28
            assert len(image_list[image]) == 28
            assert len(image_list[image][0]) == 28

            for row in range(len(image_list[image])):   #iterates through each row
                for pixel in range(len(image_list[image][row])):    #iterates through each pixel
                    #checks that all values are either 1 or 0
                    assert image_list[image][row][pixel] == 0 or image_list[image][row][pixel] == 1
                    #checks number of flips, assertion to check against budget is further down
                    if image_list[image][row][pixel] != test_image[row][pixel]:
                        budget_usage += 1
            #checks that all flipped pixels followed adjacency rules
            for i in range(len(flatten_image(image_list[image]))):
                if flatten_image(image_list[image])[i] != flatten_image(test_image)[i]:
                    assert check_adjacent_for_one(flatten_image(test_image), i) == True
            #checks that number of flips is within budget
            assert budget_usage <= budget

        # raise NotImplementedError


if __name__ == "__main__":
    unittest.main()

