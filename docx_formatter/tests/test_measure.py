import sys
import os
  
# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))
  
# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)
  
# adding the parent directory to 
# the sys.path.
sys.path.append(parent)


from measure import find_end_index


text = 'Ровно 64 года назад, в 1957 году, врач решил не патентовать свою вакцину, чтобы все фармацевтические компании могли ее производить и предлагать всем детям мира. Альберт Брюс Сабин родился в Белостоке в 1906 году. Еврейский медик и вирусолог, известный тем, что обнаружил вакцину от полиомиелита, отказался от патентных денег, разрешив распространяться на всех, включая малоимущих. Между 1959–1961 годами миллионы детей из восточных стран, Азии и Европы были привиты: вакцина от полиомиелита подавила эпидемию Полиомиелит унес с лица земли целые поколения. Его вакцина, введенная в сахарном кубике, изменила историю человечества. Он заявил: "Многие настаивали на том, чтобы я запатентовал вакцину, но я не хотел. Это мой подарок всем детям мира" — и это было его желание. Он был евреем, и две его внучки были убиты эсэсовцами. На вопрос, есть ли у него желание отомстить, он ответил: "Они убили двух замечательных внучек, но я спас детей по всей Европе. Разве вы не считаете это великолепной местью?" В годы холодной войны Сабин бесплатно пожертвовал свои вирусные штаммы советскому ученому Михаилу Чумакову, чтобы разрешить разработку его вакцины также в Советском Союзе. Он продолжал жить на зарплату, отнюдь не захватывающую, как профессор университета, но с сердцем, переполненным удовлетворением за то, что он сделал так много добра всему человечеству. (с.) Ровно 64 года назад, в 1957 году, врач решил не патентовать свою вакцину, чтобы все фармацевтические компании могли ее производить и предлагать всем детям мира. Альберт Брюс Сабин родился в Белостоке в 1906 году. Еврейский медик и вирусолог, известный тем, что обнаружил вакцину от полиомиелита, отказался от патентных денег, разрешив распространяться на всех, включая малоимущих. Между 1959–1961 годами миллионы детей из восточных стран, Азии и Европы были привиты: вакцина от полиомиелита подавила эпидемию Полиомиелит унес с лица земли целые поколения. Его вакцина, введенная в сахарном кубике, изменила историю человечества. Он заявил: "Многие настаивали на том, чтобы я запатентовал вакцину, но я не хотел. Это мой подарок всем детям мира" — и это было его желание. Он был евреем, и две его внучки были убиты эсэсовцами. На вопрос, есть ли у него желание отомстить, он ответил: "Они убили двух замечательных внучек, но я спас детей по всей Европе. Разве вы не считаете это великолепной местью?" В годы холодной войны Сабин бесплатно пожертвовал свои вирусные штаммы советскому ученому Михаилу Чумакову, чтобы разрешить разработку его вакцины также в Советском Союзе. Он продолжал жить на зарплату, отнюдь не захватывающую, как профессор университета, но с сердцем, переполненным удовлетворением за то, что он сделал так много добра всему человечеству. (с.)'
print(find_end_index(text))