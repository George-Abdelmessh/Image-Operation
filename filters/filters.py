from mean_filter import MeanFilter
from median_filter import MedianFilter

class Filters:
    def __init__(self):
        self.img = ''
        self.option = 0

    
    def choose_filter(self):
        while (True):
            try:
                self.option = int(input('''Choose The Filter: 
        1- Mean Filter
        2- Median Filter
        3- Gaussian Filter
        4- Laplacian Filter
        5- Unsharp Filter
                '''))
                if self.option > 0 and self.option <= 5:
                    break
                else:
                    print('''
                    Your Input Out Of The Range!
                    Enter Number Between 1 and 5
                    ''')
            except:
                print('Your Input Not Valid Number Please Try Again!')
        return self.option
        

    def main(self):
        self.choose_filter()
        self.img = input("Enter Image Path: ")
        if self.option == 1:
            mn = MeanFilter(self.img)
            mn.apply_filter()
        elif self.option  == 2:
            md = MedianFilter(self.img)
            md.apply_filter()
        elif self.option  == 3:
            pass
        elif self.option  == 4:
            pass
        elif self.option  == 5:
            pass
        else:
            print("Something Went Wrong, Please Try Agine!")
