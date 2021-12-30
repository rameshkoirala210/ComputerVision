width = 512 # width = 256 for easy and medium, 512 for hard


with open("rkoirala_medium_float.txt", 'r') as f:
    text = f.read()

#removes [ , ] from the txt file 
    text = text.replace('[', '')
    text = text.replace(']', '')
    text = text.replace(',', '')

    #splits the txt file
    nums = []
    for i in text.split():
        nums.append(float(i))


    #makes a txt file with a plictue that was in the text
    with open('example.txt', 'w') as out:
        for i, n in enumerate(nums):
            if n < 0.5:
                out.write("_")
            else:
                out.write("#")

            if i % width == 0:
                out.write("\n")