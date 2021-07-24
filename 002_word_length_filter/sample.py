import re


def word_length_filter(text: str, min_length: int) -> list:
    return re.findall(r"\w{"+str(length)+r",}", text)


print(word_length_filter(
    text="The conversation soon grew animated enough. \
        Ludovic was a good talker when he had somebody to draw him out. \
        He was well read, and frequently surprised Anne by his shrewd comments on \
        men and matters out in the world, \
        of which only the faint echoes reached Deland River.", min_length=7))

# Expected result
# ['conversation', 'animated', 'Ludovic', 'somebody', 'frequently', 'surprised', 'comments', 'matters', 'reached']
