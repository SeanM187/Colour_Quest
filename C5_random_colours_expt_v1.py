import random

some_colours = [
    ['alice blue', '19', 'black'], ['antique white', '20', 'black'], ['AntiqueWhite1', '20', 'black'],
    ['AntiqueWhite2', '19', 'black'], ['AntiqueWhite3', '16', 'black'], ['AntiqueWhite4', '11', 'black'],
    ['aquamarine', '10', 'black'], ['aquamarine2', '9', 'black'], ['aquamarine3', '8', 'black'],
    ['aquamarine4', '5', 'white'], ['azure', '19', 'black'], ['azure2', '18', 'black'], ['azure3', '15', 'black'],
    ['azure4', '10', 'black'], ['beige', '19', 'black'], ['bisque', '20', 'black'], ['bisque2', '19', 'black'],
    ['bisque3', '16', 'black'], ['bisque4', '11', 'black'], ['black', '0', 'white'],
    ['blanched almond', '20', 'black'], ['blue violet', '11', 'white'], ['brown', '13', 'black'],
    ['brown1', '20', 'black'], ['brown2', '19', 'black'], ['brown3', '16', 'black'], ['brown4', '11', 'white'],
    ['burlywood', '17', 'black'], ['burlywood1', '20', 'black'], ['burlywood2', '19', 'black'],
    ['burlywood3', '16', 'black'], ['burlywood4', '11', 'black'], ['cadet blue', '7', 'white'],
    ['CadetBlue1', '12', 'black'], ['CadetBlue2', '11', 'black'], ['CadetBlue3', '10', 'black'],
    ['CadetBlue4', '7', 'white'], ['chocolate', '16', 'black'], ['chocolate1', '20', 'black'],
    ['chocolate2', '19', 'black'], ['chocolate3', '16', 'black'], ['chocolate4', '11', 'white'],
    ['coral1', '20', 'black'], ['coral2', '19', 'black'], ['coral3', '16', 'black'],
    ['coral4', '11', 'white'], ['cornflower blue', '8', 'white'], ['cornsilk', '20', 'black'],
    ['cornsilk2', '19', 'black'], ['cornsilk3', '16', 'black']]

print("We have started with {} colours!".format(len(some_colours)))

# loop three times (ie: generate three rounds worth of colours)
for item in range(0, 3):
    round_colour_list = []
    colour_scores = []

    # get six unique colours
    while len(round_colour_list) < 6:
        # choose item
        chosen_colour = random.choice(some_colours)
        index_chosen = some_colours.index(chosen_colour)

        # check score is not already in list
        if chosen_colour[2] not in colour_scores:
            # add item to rounds list
            round_colour_list.append(chosen_colour)

            # remove item from master list
            some_colours.pop(index_chosen)

    print("Round Colours: ", round_colour_list)
    print("Colour List Length: ", len(some_colours))
    print()