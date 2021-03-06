#-*- coding:utf-8 -*-


class Specialties(object):
    buttons = {'add': ("Добавить новую запись", '/specialty_add'),
               'edit': ("Редактировать", '/specialty_edit'),
               'del': ("Удалить", '/specialty_del')}
    table_name = {'specialties': "Специальности",
                  'specialty_add': "Добавить новую специальность ",
                  'specialty_edit': "Редактирование информации " +
                  "о специальности {} факультета {}"}
    answer = {'add': ("Специальность {} уже существует на факультете " +
                      "{}. Введите другое название специальности.",
                      "Специальность {} успешно добавлена на факультет {}."),
              'edit': ("Специальность {} уже существует на факультете {}. " +
                       "Введите другое название специальности.",
                       "В название специальности {} не было внесено " +
                       "изменений. Введите другое название специальности.",
                       "Специальность {} факультета {} успешно " +
                       "отредактирована."),
              'del': "Специальлность id {} успешно удалена"}


class Disciplines(object):
    buttons = {'add': ("Добавить новую запись", '/discipline_add'),
               'edit': ("Редактировать", '/discipline_edit'),
               'del': ("Удалить", '/discipline_del')}
    table_name = {'disciplines': "Дисциплины",
                  'discipline_add': "Добавить новую дисциплину"}
    answer = {'add': ("Выберите факультет и специальность",
                      "Дисцилпина {} уже существует на специальности {}. " +
                      "Введите другое название дисциплины.",
                      "Дисциплина {} успешно добавлена. "),
              'edit': ("Дисцилпина {} уже существует на специальности {}. " +
                       "Введите другое название дисциплины.",
                       "Дисциплина № {} успешно отредактирована. "),
              'del': "Дисциплина id {} успешно удалена"}


class Students(object):
    buttons = {'add': ("Добавить новую запись", '/student_add'),
               'edit': ("Редактировать", '/student_edit'),
               'del': ("Удалить", '/student_del'),
               'profile': ("Профиль", '/student_profile')}
    table_name = {'students': "Студенты",
                  'student_add': "Добавить нового студента "}
    answer = {'add': ("Введите полные корректные данные",
                      "Студент успешно добавлен. "),
              'edit': "Информация о студенте id={} успешно отредактирована.",
              'del': "Информация о студенте id={} успешно удалена"}


class Marks(object):
    buttons = {'add': ("Добавить новую запись", '/mark_add'),
               'edit': ("Редактировать", '/mark_edit'),
               'del': ("Удалить", '/mark_del')}
    table_name = {'marks': "Оценки",
                  'mark_add': "Добавить новую оценку "}
    answer = {'add': ("Оценка успешно добавлена. ",
                      "Оценка не была добавлена т.к. по дисциплине id={} у " +
                      "студента id={} уже есть оценка. Оценку можно " +
                      "отредактировать в этом меню."),
              'edit': "Оценка id={} успешно отредактирована.",
              'del': "Оценка id={} успешно удалена"}
