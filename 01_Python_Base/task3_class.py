class ImageProcessor:
    def __init__(self,name):
        self.name = name
        self.size = 0
    def process_image(self):
        self.size = 1024
    def show_info(self):
        print(self.name,self.size)
def main():
    processor = ImageProcessor("img1")
    processor.show_info()
    processor.process_image()
    processor.show_info()
if __name__ == '__main__':
  main()

