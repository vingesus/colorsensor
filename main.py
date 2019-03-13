import colorsensor

if __name__ == '__main__':
        try:
                colorsensor.setup(24, 22, 23, 4, 17, 18) #out, s2, s3, s0, s1, oe
                colorsensor.set_white_level([6780, 5930, 7330]) #Configure these to your enviorment! You can get the values by doing colorsensor.get_level()
                colorsensor.set_black_level([5060, 4500, 5720])
                while True:
                        print(colorsensor.get_rgb()) #You can also use colorsensor.get_avg_rgb(5) - The "5" defines the times you want to scan, each scan is 0.33s! (Can be altered)
        finally:
                colorsensor.cleanup()