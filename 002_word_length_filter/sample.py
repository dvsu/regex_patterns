import re


def word_length_filter(text: str, min_length: int) -> list:
    return re.findall(r"\w{"+str(min_length)+r",}", text)


print(word_length_filter(
    text="The conversation soon grew animated enough. \
        Ludovic was a good talker when he had somebody to draw him out. \
        He was well read, and frequently surprised Anne by his shrewd comments on \
        men and matters out in the world, \
        of which only the faint echoes reached Deland River.", min_length=7))

# Expected result
# ['conversation', 'animated', 'Ludovic', 'somebody', 'frequently', 'surprised', 'comments', 'matters', 'reached']

print(word_length_filter(
    text="There were no Mayflowers in June; \
        but now the Old Lady’s garden was full of blossoms and \
        every morning Sylvia found a bouquet of them by the beech—\
        the perfumed ivory of white narcissus, the flame of tulips, \
        the fairy branches of bleeding-heart, the pink-and-snow of little, \
        thorny, single, sweetbreathed early roses. The Old Lady had no fear of discovery, \
        for the flowers that grew in her garden grew in every other Spencervale garden as well, \
        including the Stewart garden. .", min_length=10))

# Expected result
# ['Mayflowers', 'sweetbreathed', 'Spencervale']
