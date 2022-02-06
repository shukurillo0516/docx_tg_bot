import tkinter 
from tkinter import font as tkFont

# Enough to initialize resources

PAGE_WIDTH = 20500

RESULT = []

def measure_w(text) -> int:
    tkinter.Frame().destroy()
    settings = tkFont.Font(family='Arial', size=12)
    return settings.measure(text)


class FindEnd:
    def __init__(self):
        self.result = []


    def find_end(self, text):
        if len(text) < 1800:
            self.result.append(text)
            return ''

        res = text[:1000]
        g = text

        i = 1000
        while measure_w(res) <= (PAGE_WIDTH - 4500):
            res += text[i]
            g = text[i:]
            # print(g)
            i += 1

        self.result.append(res)
        return self.find_end(g)


# def main(text):
#     i = len(find_end(text))

#     while i 


# text = 'Ровно 64 года назад, в 1957 году, врач решил не патентовать свою вакцину, чтобы все фармацевтические компании могли ее производить и предлагать всем детям мира. Альберт Брюс Сабин родился в Белостоке в 1906 году. Еврейский медик и вирусолог, известный тем, что обнаружил вакцину от полиомиелита, отказался от патентных денег, разрешив распространяться на всех, включая малоимущих. Между 1959–1961 годами миллионы детей из восточных стран, Азии и Европы были привиты: вакцина от полиомиелита подавила эпидемию Полиомиелит унес с лица земли целые поколения. Его вакцина, введенная в сахарном кубике, изменила историю человечества. Он заявил: "Многие настаивали на том, чтобы я запатентовал вакцину, но я не хотел. Это мой подарок всем детям мира" — и это было его желание. Он был евреем, и две его внучки были убиты эсэсовцами. На вопрос, есть ли у него желание отомстить, он ответил: "Они убили двух замечательных внучек, но я спас детей по всей Европе. Разве вы не считаете это великолепной местью?" В годы холодной войны Сабин бесплатно пожертвовал свои вирусные штаммы советскому ученому Михаилу Чумакову, чтобы разрешить разработку его вакцины также в Советском Союзе. Он продолжал жить на зарплату, отнюдь не захватывающую, как профессор университета, но с сердцем, переполненным удовлетворением за то, что он сделал так много добра всему человечеству. (с.) Ровно 64 года назад, в 1957 году, врач решил не патентовать свою вакцину, чтобы все фармацевтические компании могли ее производить и предлагать всем детям мира. Альберт Брюс Сабин родился в Белостоке в 1906 году. Еврейский медик и вирусолог, известный тем, что обнаружил вакцину от полиомиелита, отказался от патентных денег, разрешив распространяться на всех, включая малоимущих. Между 1959–1961 годами миллионы детей из восточных стран, Азии и Европы были привиты: вакцина от полиомиелита подавила эпидемию Полиомиелит унес с лица земли целые поколения. Его вакцина, введенная в сахарном кубике, изменила историю человечества. Он заявил: "Многие настаивали на том, чтобы я запатентовал вакцину, но я не хотел. Это мой подарок всем детям мира" — и это было его желание. Он был евреем, и две его внучки были убиты эсэсовцами. На вопрос, есть ли у него желание отомстить, он ответил: "Они убили двух замечательных внучек, но я спас детей по всей Европе. Разве вы не считаете это великолепной местью?" В годы холодной войны Сабин бесплатно пожертвовал свои вирусные штаммы советскому ученому Михаилу Чумакову, чтобы разрешить разработку его вакцины также в Советском Союзе. Он продолжал жить на зарплату, отнюдь не захватывающую, как профессор университета, но с сердцем, переполненным удовлетворением за то, что он сделал так много добра всему человечеству. (с.)'
# # text = 'Ровно 64 года назад, в 1957 году, врач решил не патентовать'
# h = FindEnd()
# h.find_end(text)
# result = h.result
# print(len(result))
# for i in result:
#     print(i)
#     print()