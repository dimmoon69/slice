from tcs_pythonwhat.signatures import sig_from_params
from tcs_pythonwhat.test_exercise import prep_context

_, ctxt = prep_context()
globals().update(ctxt)
# pre_code - Что не видит студент ----------------------------------------------------------------------
'''

'''

# sample_code - Что видит студент в начале -------------------------------------------------------------
'''

'''

# sol_code - Код который верный ------------------------------------------------------------------------
sol_code = r'''

'''

# stu_code - Код который тестируем ---------------------------------------------------------------------
stu_code = r'''

'''

# Tests ------------------------------------------------------------------------------------------------
from tcs_pythonwhat.test_exercise import setup_state

setup_state(stu_code=stu_code, sol_code=sol_code)
# expectation ------------------------------------------------------------------------------------------

Ex()...


success_msg("""

            """)


