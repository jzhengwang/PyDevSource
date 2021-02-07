import docx
import PyPDF2
import os
import errno
import docx
import docx2txt
import io

#################################################################
# print: format reference:
# print(f'The value of pi is approximately {math.pi:.3f}.')
# print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
################################################################
from datetime import datetime
from docx import *
from PyPDF2 import *
from nltk.tokenize import word_tokenize

from python_port_apis.platform_util_functions import platform_util

cur_platform = platform_util()
if cur_platform.is_platform_linux():
    from odf import *
    from odf import teletype
    from odf.opendocument import load


class QuizProblem:
    def __init__(self, question_text, score, correct_ans, given_answer, multi_choice_list, image_file_list):
        self.Question = question_text
        self.Score = score
        self.Answer = correct_ans
        self.LChoice = multi_choice_list
        self.LImages = image_file_list
        self.GivenAnswer = given_answer

    def check_answer(self):
        if self.Answer == self.GivenAnswer:
            return True
        else:
            return False

    def get_question_score(self):
        return self.Score


class MathQuizProblem(QuizProblem):  # inherent and override
    def question_solution(self, Solution1, Solution2, Solution3, Solution4, Solution5):
        self.Solution_List = [
            Solution1,
            Solution2,
            Solution3,
            Solution4,
            Solution5
        ]
        self.GivenSolution = None

    def select_solution(self, GivenSolution):
        self.GivenSolution = GivenSolution


def docx2word_process(Document):
    total_problems = 0
    math_test = []
    for paragraph in Document.paragraphs:
        print(paragraph.text)
        input("continue")
        total_problems += 1

    print("Total number of math problems : %d", total_problems)


def docx_questions(fileName):
    # docfile = docx.opendocx(fileName)
    document = docx.Document(fileName)
    # docx2word_process(document)
    image_dir = "..mage_folder/"
    if not os.path.exists(os.path.dirname(image_dir)):
        while (True):
            try:
                os.makedirs(os.path.dirname(image_dir))
                break
            except OSError as exc:  # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

    allProblemsText = docx2txt.process(fileName, image_dir)
    math_test = []
    allProblemsList = allProblemsText.split("Solution")
    print(len(allProblemsList))
    count = 0
    total_problems = len(allProblemsList)
    while count < total_problems:
        math_test.append(MathQuizProblem(allProblemsList[count], 0, 0, 0, 0, 0))
        count += 1
    print("Total Math Problem: %d", total_problems)
    total_correct = 0;

    for problem in math_test:
        print(problem.Question)
        while (True):
            ans = input("Please give your answer(A):") or "A"
            print("Your answer is %s:", ans.capitalize())
            bContinue = input("Yes / No (Y/N)?")
            if bContinue.upper() == 'Y':
                break;
        problem.GivenAnswer = ans
        if problem.check_answer():
            total_correct += 1
    print("You got %d corrects out of %d questions" % (total_correct, total_correct))


def find_pdf_token(text_str):
    ##nltk.download('punkt')
    tokens = word_tokenize(text_str)
    print(tokens)


def pdf_question_file(filesName):
    pdfName = filesName
    pdfFileObj = open(pdfName, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    num_of_pages = pdfReader.numPages
    for pageN in range(num_of_pages):
        page_text = pdfReader.getPage(pageN)
        page_content = page_text.extractText()
        for line in io.StringIO(page_content):
            find_pdf_token(line)


def odf_question_file(filesName):
    textdoc = load(filesName)
    # allparas = textdoc.getElementsByType()
    allText = teletype.extractText(textdoc.body)
    print(allText)
