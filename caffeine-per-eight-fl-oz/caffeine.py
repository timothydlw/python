drink_size = int(input('Enter drink size in fl oz: '))

caff_content = int(input('Enter total caffeine content in mg: '))

def convert():
    caff_per_eight = (caff_content * 8)/drink_size
    print(caff_per_eight, 'mg caffeine per 8 fl oz.')

convert()