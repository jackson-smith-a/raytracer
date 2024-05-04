from cv2 import imread, imshow, waitKey, destroyAllWindows

def view(*args: list[str]):
    for name in args:
        img = imread("images/" + name)
        imshow(name, img)

    while 1:
        if waitKey(33) == ord("q"):
            destroyAllWindows()
            return
    
if __name__ == "__main__":
    view("image.ppm")
