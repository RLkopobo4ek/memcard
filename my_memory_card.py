#создай приложение для запоминания информации

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QGroupBox, QButtonGroup
from random import shuffle, randint

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
q_list = []
q_list.append(Question('im egor?', 'yes', 'no', 'no', 'no'))
q_list.append(Question('u r short?', 'yes', 'no', 'no', 'no'))
q_list.append(Question('ok?', 'ok', 'ne ok', 'net', 'pon'))
q_list.append(Question('Какого я цвета?', 'Черного', 'Голубово', 'белого', 'черного'))

app = QApplication([])

ok = QPushButton("decide")
question = QLabel('most harder question in the world!')


RadioGroupBox = QGroupBox("Варианты ответов:")
rbtn_1 = QRadioButton('Да')
rbtn_2 = QRadioButton('yes')
rbtn_3 = QRadioButton('+')
rbtn_4 = QRadioButton('Nu kaneshna!')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Не ждали? А результат здесь!')
res1 = QLabel('Прав или нет?')
correct = QLabel('онсвер тут!')

layout_res = QVBoxLayout()
layout_res.addWidget(res1, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()



layout_line1.addWidget(question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)

AnsGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(ok, stretch=2)
layout_line3.addStretch(1)
layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    ok.setText('next')



def show_ques():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    ok.setText('decide')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)


answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]


def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    res1.setText(q.right_answer)
    show_ques()


def show_correct(res):
    correct.setText(res)
    show_result()


def check_answer():
    if answers[0].isChecked():
        window.score += 1
        print('Stats. total questions:', window.total, 'total right answers:', window.score)
        print('rate:', window.score/window.total*100, '%')
        show_correct('Right!')
    else:
        if answers[1].isChecked or answers[2].isChecked or answers[3].isChecked:
            print('rate:', window.score/window.total*100, '%')
            show_correct('Wrong!')

def next_question():
    window.total += 1
    print('Stats. total questions:', window.total, 'total right answers:', window.score)
    cur_question = randint(0, len(q_list) - 1)
    q = q_list[cur_question]
    ask(q)

def click():
    if ok.text() == 'decide':
        check_answer()
    else:
        next_question()


window = QWidget()

window.setWindowTitle('Memory Card')
window.setLayout(layout_card)     


window.total = 0
window.score = 0
ok.clicked.connect(click)
next_question()



window.show()
app.exec_()