import imageio.v3 as iio


filenames = [
    r'C:\Users\aybuk\PycharmProjects\WelcomeScreen\dino1.png',
    r'C:\Users\aybuk\PycharmProjects\WelcomeScreen\dino2.png',
    r'C:\Users\aybuk\PycharmProjects\WelcomeScreen\dino3.png',
    r'C:\Users\aybuk\PycharmProjects\WelcomeScreen\dino4.png'
]
images = []

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite(r'C:\Users\aybuk\PycharmProjects\WelcomeScreen\dino.gif', images, duration=500, loop=0)


