import viddil
import many_viddils
import pr_v3_defs

t=viddil.Viddil()
print(t.get_title)

answer = answer2 = 0
collect_v = many_viddils.Many_viddils()
collect_v.read_from_file("viddil.txt")
print(collect_v)

menu = []
menu.append("щоб додати елемент в колекцію - введіть: 'add' ")
menu.append("щоб видалити елемент з колекції - введіть: 'del' ")
menu.append("щоб редагувати елемент в колекції - введіть: 'edit' ")
menu.append("щоб здійснити пошук - введіть: 'find'")
menu.append("щоб здійснити сортування - введіть: 'sort' ")
menu.append("щоб зчитати з файлу - введіть: 'read' ")
menu.append("щоб записати в файл - введіть: 'write' ")
menu.append("щоб вийти - введіть 'stop' ")


while answer != "stop":
    for elem in menu: print(elem)
    answer = input()
    match answer:
        case 'add':
            temp_v = viddil.Viddil()
            temp_v.set_with_keyboard()
            collect_v.add_item(temp_v)
            print("collection now: ", collect_v, '\n')
        case 'del':
            index = pr_v3_defs.input_number("вкажіть номер рядка для видалення: ")
            collect_v.delete_elem(index-1)
            print("collection now: ", collect_v, '\n')
        case'edit':
            print("Вводьте коректні дані!")
            old_data = input("введіть старі дані: ")
            new_data = input("введіть на що хочете змінити: ")
            collect_v.edit_viddil(old_data, new_data)
            print("collection now: ", collect_v, '\n')
        case 'find':
            what = input("Введіть, що шукаєте: ")
            collect_v.find_in_collection(what, 1)
        case 'sort':
            print("ДОСТУПНІ ПОЛЯ ПО ЯКИХ СОРТУВАТИ: 'ID', 'title', 'director_name', 'phone_number,'")
            print("'monthly_budget', 'yearly_budget', 'website_url' ")
            atr = input("введіть поле: ")
            collect_v.sort_in_collection(atr)
        case 'read':
            path = input("введіть назву txt файлу для зчитування: ")
            collect_v.read_from_file(path)
            print("collection now: ", collect_v, '\n')
        case 'write':
            path = input("введіть назву txt файлу для запису туди: ")
            collect_v.write_in_file(path)
        case 'stop':
            print("ЗДІЙСНЕНО ВИХІД")
        case _ :
            print("Ви ввели неіснуючий пункт меню")

