import time as ti

from common_utils.url_utility_functions import UrlLinkUtility
import common_utils.dbg_logging_util as dbg_logging_util
from common_utils.gui_utility_functions import GuiUtility

amc_math_wiki_link = ('https://artofproblemsolving.com', 'https://artofproblemsolving.com/wiki/index.php/')


class AmcMathContestUrl(UrlLinkUtility):
    solution_urls = []
    question_urls = []

    def build_test_lib(self, url_name: object):
        self.open_an_url_link(url_name)
        self.build_url_link_list("_AMC_")

    def select_amc_test( self, test_name):
        for test_question in self.url_list:
            self.logging.dbg_logging("DEBUG::" + test_question)
        self.logging.dbg_logging("INFO::Selected test is " + test_name)
        for test_question in self.url_list:
            self.logging.dbg_logging("DEBUG::" + test_question)
            if str(test_question).find(test_name) != -1:
                if self.open_an_url_link(test_name + "_Problems"):
                    self.build_url_link_list(test_name + "_Problems/Problem_")
                    self.solution_urls = self.url_list.copy()
                    self.build_url_link_list("#Problem")
                    self.question_urls = self.url_list.copy()
                    self.select_url = self.index_page_url + test_name + "_Problems"
                    self.logging.dbg_logging("INFO::Found!!!{url}".format(url=self.select_url))
                    break

    def collect_test_questions(self, question):
        # break into lines and remove leading and trailing space on each
        text = self.extract_text_from_xml()
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)
        self.logging.dbg_logging("DEBUG::" + text)
        ### another way
        # soup = BeautifulSoup(open(self.select_url), features="lxml")

    def show_solution_list(self):
        self.logging.dbg_logging("INFO::" + self.solution_urls)

    def show_question_list(self):
        self.logging.dbg_logging("INFO::" + self.question_urls)


class MathTestUtil:
    def __init__ ( self, math_test, test_gui, logging_util):
        self.math_test = math_test
        self.gui = test_gui
        self.logging = logging_util

    def create_test_lib ( self, url_name):
        self.math_test.build_test_lib(url_name)

    def open_selected_amc_test ( self, test_name ):
        self.math_test.select_amc_test(test_name)
        for question in range(len(self.math_test.question_urls)):
            self.math_test.collect_test_questions(question)

    def show_all_solutions ( self, math_test):
        for sol in self.math_test.solution_urls:
            self.logging.dbg_logging("DEBUG::" + sol)

    def show_all_questions ( self, math_test):
        for question in math_test.question_urls:
            self.logging.dbg_logging("DEBUG::" + question)

    def amc_contest_thread(self, arg0, arg1):
        while True:
            ti.sleep(5)
            self.logging.dbg_logging("INFO::{thread_name}:Start AMC Contest now".format(thread_name=arg1))


def initial_amc_test_thread():
    dbg_log_name = "../dbg_log/dbg_{file}log".format(file=__name__)
    amc_logging = dbg_logging_util.DbgUtilityApi('DEBUG', 'AMC',  dbg_log_name)
    amc_logging.dbg_set_level("DEBUG", 0)
    amc_math_test = AmcMathContestUrl(amc_math_wiki_link[0], amc_math_wiki_link[1], amc_logging)
    amc_math_test_gui = GuiUtility("AMC Contest Welcome", "Arial Bold", 50, 0, 0, "1000x200", amc_logging)
    amc_math_test_util = MathTestUtil(amc_math_test, amc_math_test_gui, amc_logging)
    # Build a test information window frame
    ent_texts = {"First Name": "Max", "Last Name": "Wang", "Student ID": "0000"}
    btn_texts = ["Submit", "Cancel"]
    entry_dict = amc_math_test_gui.open_entry_window(ent_texts, btn_texts)
    student_name = entry_dict.get("First Name")
    if student_name is not None:
        amc_math_test_gui.open_info_window('Hi %s ! \n Welcome to Math AMC test contest!!!\n' % student_name, 5000)
    else:
        exit()
    # Using the URL link
    ent_texts = {"Level(8/10/12)": "12", "Year(2020)": "2020", "Section(A/B)": "A"}
    btn_texts = ["Submit", "Cancel"]
    entry_dict = amc_math_test_gui.open_entry_window(ent_texts, btn_texts)

    test_level = entry_dict.get("Level(8/10/12)")
    if test_level is not None:
        amc_overall_url = "AMC_{test_level}_Problems_and_Solutions".format(test_level=test_level)
        amc_math_test_util.create_test_lib(amc_overall_url)
        test_year = entry_dict.get("Year(2020)")
        if test_year == "":
            test_year = "2020"  # default to used 2020 AMC
        test_ab = entry_dict.get("Section(A/B)")
        if test_ab == "":
            test_ab = "A"
        test_level = test_level + test_ab.upper()
        test_name = "{test_year}_AMC_{test_level}".format(test_year=test_year, test_level=test_level)
        amc_math_test_util.open_selected_amc_test(test_name)
        amc_logging.dbg_logging("DEBUG::All the question are as following:")
        amc_math_test_util.show_all_questions(amc_math_test)
        amc_logging.dbg_logging("DEBUG::All the solution are as following:")
        amc_math_test_util.show_all_solutions(amc_math_test)
    return amc_math_test_util

