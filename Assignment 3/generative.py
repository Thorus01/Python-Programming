from __future__ import annotations
from ai import predict_number, read_image

def flatten_image(image: list[list[int]]) -> list[int]:
    """
    Flattens a 2D list into a 1D list.
    
    :param image: 2D list of integers representing an image.
    :return: 1D list of integers representing a flattened image.
    """
    return [pixel for row in image for pixel in row]
    
def unflatten_image(flat_image: list[int]) -> list[list[int]]:
    """
    Unflattens a 1D list into a 2D list.
        
    :param flat_image: 1D list of integers representing a flattened image.
    :return: 2D list of integers.
    """
    decompressed_image = []
    row_length = int(len(flat_image)**0.5)  #determines the size of each unflattened row
    for i in range(row_length): #iterates through each row
        row_list = []
        current_front = i * row_length
        current_end = current_front + row_length
        row_list = (flat_image[current_front:current_end])  #adds a row to the list, as determined by slicing the flat image from its start to end
        decompressed_image.append(row_list)

    return decompressed_image
# Paste flatten_image and unflatten_image from task 1 here

def check_adjacent_for_one(flat_image: list[int], flat_pixel: int) -> bool:
    """
    Checks if a pixel has an adjacent pixel with the value of 1.
    
    :param flat_image: 1D list of integers representing a flattened image.
    :param flat_pixel: Integer representing the index of the pixel in question.
    :return: Boolean.
    """

    row_length = int(len(flat_image)**0.5)
    #Checks left and right, then up and down for ones
    if flat_pixel % row_length != 0 and flat_image[flat_pixel-1] == 1: 
        #checks whether the adjacent pixel is on the same row and whether it's a one
        return True

    elif (flat_pixel+1) % row_length != 0 and flat_pixel+1 != len(flat_image) and flat_image[flat_pixel+1] == 1: 
        #as above but for other side
        return True

    elif flat_pixel-row_length >= 0 and flat_image[flat_pixel-row_length] == 1:
        #checks whether the above pixel is a one
        return True

    elif flat_pixel+row_length < len(flat_image) and flat_image[flat_pixel+row_length] == 1:
        #checks whether the below pixel is a one
        return True

    else:
        return False
# Paste check_adjacent_for_one from task 2 here

def pixel_flip(lst: list[int], orig_lst: list[int], budget: int, results: list, i: int = 0) -> None:
    """
    Uses recursion to generate all possibilities of flipped arrays where
    a pixel was a 0 and there was an adjacent pixel with the value of 1.

    :param lst: 1D list of integers representing a flattened image.
    :param orig_lst: 1D list of integers representing the original flattened image.
    :param budget: Integer representing the number of pixels that can be flipped.
    :param results: List of 1D lists of integers representing all possibilities of flipped arrays, initially empty.
    :param i: Integer representing the index of the pixel in question.
    :return: None.
    """

    if i == len(orig_lst):  #defines the base case
        return None
    else:
        if orig_lst[i] != 1 and check_adjacent_for_one(orig_lst, i) == True and budget > 0: #checks whether a flip is allowed
            lst[i] = 1
            if lst not in results:  #updates the current list, avoiding duplicates
                results.append(lst)
            pixel_flip(lst[:], orig_lst, budget-1, results, i+1)    #checks the next possibility
            temp_lst = lst[:]
            temp_lst[i] = 0
            pixel_flip(temp_lst[:], orig_lst, budget, results, i+1) #checks the possibility where the current pixel was not flipped
            return
        else:
            pixel_flip(lst[:], orig_lst, budget, results, i+1)  #checks the next possibility where no flip is done
            return
        pixel_flip(orig_lst[:], orig_lst, budget, results, i+1) #checks the possibilities for the next i
# Paste pixel_flip from task 3 here

def write_image(orig_image: list[list[int]], new_image: list[list[int]], file_name: str) -> None:
    """
    Writes a newly generated image into a file where the modified pixels are marked as 'X'.
    
    :param orig_image: 2D list of integers representing the original image.
    :param new_image: 2D list of integers representing a newly generated image.
    :param file_name: String representing the name of the file.
    :return: None.
    """

    formatted_image = []    #container for the modified image

    with open(file_name, "w") as new_image_file:    #opens the file to write
        for i in range(len(new_image)): #iterates through each row
            for j in range(len(new_image)): #iterates through each item
                if new_image[i][j] != orig_image[i][j]:
                    new_image[i][j] = "X"
                formatted_image.append(str(new_image[i][j]))
            formatted_image.append("\n")
        new_image_file.write("".join(formatted_image))  #writes the image to the file

    return
# Paste write_image from task 4 here

def generate_new_images(image: list[list[int]], budget: int) -> list[list[list[int]]]:
    """
    Generates all possible new images that can be generated within the budget.
    
    :param image: 2D list of integers representing an image.
    :param budget: Integer representing the number of pixels that can be flipped.
    :return: List of 2D lists of integers representing all possible new images.
    """

    flipped_images = [] #container for the results of the below pixel_flip
    pixel_flip(flatten_image(image), flatten_image(image), budget, flipped_images)

    new_image_list = [] #list of new images that produce the same predicted number
    for i in flipped_images:    #iterates through flipped images
        if predict_number(unflatten_image(i)) == predict_number(image):
            new_image_list.append(unflatten_image(i))
    return new_image_list
# Paste generate_new_images from task 5 here


if __name__ == "__main__":
    image = read_image("image.txt")
    new_images = generate_new_images(image, 2)
    print(f"Number of new images generated: {len(new_images)}")
    # Write first image to test generation
    write_image(image, new_images[0], "new_image_1.txt")
