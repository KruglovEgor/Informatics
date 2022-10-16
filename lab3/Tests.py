#My ISU is 367327
# 367327 % 5 = 2, 367327 % 4 = 3, 367327 % 7 = 2
#My smile is "X<{O"
#367237 % 6 = 1
#367327 % 4 = 3



tests_smiles = [
    "You act different X<{O.  Whenever we are all hanging out, you put on this macho man type actX<{O.  You don’t act like you when you’re in front of your friends. X<{OX<{OX<{O",
    "X<{O Look, you don’t have to be…you don’t have to agree with me all the time, X<{O in order for me to like you more. X<{OX<{O I see what you’re doing and I just want you to know that you don’t need to try so hard for me to like you or for anyone else to like you. X<{OX<{OX<{OX<{OX<{O",
    "I’m just being me. I want to be more real in my life. I’ve gotten tired of trying to fit in and be accepted by everyone else. I’ve always felt like I’m lying to myself. If people don’t accept me for me, for who I truly am, then I don’t want to be friends with those people.",
    "That’s all you want, isn’t it? X<{O That’s what you do, it’s why you always create drama in this family. For the attention of it all X<{O! You’re just never happy, are you X<{O? Unless the world is talking about you.",
    "Everything is easy for you, Sally. I don’t have parents like yours… X<{O I can’t stand my mother and my father always has no more than two nickels X<{O to rub together X<{O X<{O."
]

answers_smiles = [5, 9, 0, 3, 4]

test_repeats = [
    "Довольно распространённая ошибка ошибка – это лишний повтор повтор слова слова. Смешно, не не правда ли? Не нужно портить хор хоровод",
    "Hi, my my name is Egor Egor. I'm 18 18 years years old. My my native city city - N. Novgorod Novgorod.",
    "A useful useful skill my father her taught me is is managing my myney. He taught taught me this this skill by by by giving me an allowance when when I I was in in school.",
    "Полезный навык навык, которому научил научил меня отец - управлять своими своими деньгами деньгами. Он научил научил меня этому навыку, давая давая мне карманные деньги, когда когда я учился в в школе.",
    "One difficult difficult experience that that I went through was was living alone in in another another city. I experienced this when when I moved in order order to go go to to school."

]

answers_repeats = [
    "Довольно распространённая ошибка – это лишний повтор слова. Смешно, не правда ли? Не нужно портить хор хоровод",
    "Hi, my name is Egor. I'm 18 years old. My my native city - N. Novgorod.",
    "A useful skill my father her taught me is managing my myney. He taught me this skill by by giving me an allowance when I was in school.",
    "Полезный навык, которому научил меня отец - управлять своими деньгами. Он научил меня этому навыку, давая мне карманные деньги, когда я учился в школе.",
    "One difficult experience that I went through was living alone in another city. I experienced this when I moved in order to go to school."
]

test_kick = [
    ["P000", "Петров П.П. P000\nАнищенко А.А. P33113\nПримеров Е.В. P000\nИванов И.И. P000"],
    ["P3124", "Ivanov A.V. P3122\nPetrova M.M. P3120\nVasilev K.K. P3124\nKostina A.A. P3124\nVerhov P.V. P3124\nErshov V.G. P3124"],
    ["13", "Хэрингтон Б.Г. 12\nЭрнандез Д.Д. 13\nМакГрегор К.К. 10\nКуплинов Д.В. 13"],
    ["P2222", "Messi L.L. P2221\nRonaldo C.J. P2222\nRamos S.S. P2222\nMbappe K.K. P2222\nNeymar J.J. P2210"],
    ["P12345", "House M.D. P1234\nChan D.D. P12345\nMask I.J. P12345\nJobs S.S. P123456\nBezos J.J. P12345"]

]

answers_kick = [
    "Анищенко А.А. P33113\nПримеров Е.В. P000",
    "Ivanov A.V. P3122\nPetrova M.M. P3120\nVerhov P.V. P3124\nErshov V.G. P3124",
    "Хэрингтон Б.Г. 12\nМакГрегор К.К. 10\nКуплинов Д.В. 13",
    "Messi L.L. P2221\nRonaldo C.J. P2222\nNeymar J.J. P2210",
    "House M.D. P1234\nMask I.J. P12345\nJobs S.S. P123456"
]