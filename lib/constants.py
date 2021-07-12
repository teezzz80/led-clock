SEG_A = 0
SEG_B = 1
SEG_C = 2
SEG_D = 3
SEG_E = 4
SEG_F = 5
SEG_G = 6

CHARS = {
    '0': [SEG_A, SEG_B, SEG_C, SEG_D, SEG_E, SEG_F],
    '1': [SEG_B, SEG_C],
    '2': [SEG_A, SEG_B, SEG_G, SEG_E, SEG_D],
    '3': [SEG_A, SEG_B, SEG_G, SEG_C, SEG_D],
    '4': [SEG_B, SEG_G, SEG_F, SEG_C],
    '5': [SEG_A, SEG_F, SEG_G, SEG_C, SEG_D],
    '6': [SEG_A, SEG_F, SEG_G, SEG_C, SEG_D, SEG_E],
    '7': [SEG_A, SEG_B, SEG_C],
    '8': [SEG_A, SEG_B, SEG_C, SEG_D, SEG_E, SEG_F, SEG_G],
    '9': [SEG_A, SEG_B, SEG_C, SEG_D, SEG_F, SEG_G],    
    'A': [SEG_A, SEG_B, SEG_C, SEG_E, SEG_F, SEG_G],
    'B': [SEG_C, SEG_D, SEG_E, SEG_F, SEG_G],
    'C': [SEG_D, SEG_E, SEG_G],
    'D': [SEG_B, SEG_C, SEG_D, SEG_E, SEG_G],
    'E': [SEG_A, SEG_F, SEG_E, SEG_D, SEG_G],
    'F': [SEG_A, SEG_F, SEG_G, SEG_E],
    'G': [SEG_A, SEG_B, SEG_F, SEG_G, SEG_C, SEG_D],
    'H': [SEG_B, SEG_F, SEG_G, SEG_C, SEG_E],
    'I': [SEG_E],
    'J': [SEG_B, SEG_C, SEG_D],
    'L': [SEG_F, SEG_E, SEG_D],
    'N': [SEG_C, SEG_G, SEG_E],
    'O': [SEG_G, SEG_C, SEG_D, SEG_E],
    'P': [SEG_A, SEG_B, SEG_G, SEG_F, SEG_E],
    'Q': [SEG_A, SEG_B, SEG_G, SEG_F, SEG_C],
    'R': [SEG_E, SEG_G],
    'S': [SEG_A, SEG_F, SEG_G, SEG_C, SEG_D],
    'U': [SEG_F, SEG_E, SEG_D, SEG_C, SEG_B],
    'Y': [SEG_F, SEG_G, SEG_B, SEG_C, SEG_D],
}

COLORS = {
    'red': (255, 0, 0),
    'orange': (255, 64, 0),
    'yellow': (255, 255, 0),
    'green': (0, 255, 0),
    'cyan': (0, 128, 255),
    'blue': (0, 0, 255),
    'purple': (191, 0, 255),
    'pink': (255, 0, 255),
    'white': (255, 255, 255),
}

THEMES = [
    ['white', 'white', 'green', 'green'],
    ['white', 'white', 'orange', 'orange'],
    ['white', 'white', 'blue', 'blue'],
    ['blue', 'blue', 'orange', 'orange'],
    ['red', 'red', 'blue', 'blue'],
    ['cyan', 'cyan', 'pink', 'pink'],
    ['red', 'green', 'blue', 'yellow'],
]

DATETIME_ENUM = {
    'year': 0,
    'month': 1,
    'day': 2,
    'day_of_week': 3,
    'hour': 4,
    'minute': 5,
    'second': 6,
    'millisecond': 7,
}