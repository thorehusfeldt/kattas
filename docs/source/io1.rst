Basic Input/Output
==================

.. _foo:

Read a line of input as a string
--------------------------------


.. code-block:: python3

   s = input()


Katta: Echo echo
----------------

Read a string, either “Hello” or “Hallo”, and repeat it twice.

Intended solution:

Use a variable to store input:

.. literalinclude:: ../../problems/echoecho/submissions/accepted/th.py
   :lines: 3-

Other solutions:

Since there are only two possible inputs, we can be less general, avoiding the variable but using selection:

.. literalinclude:: ../../problems/echoecho/submissions/accepted/th-if.py
   :lines: 3-

Wrong ideas:

.. literalinclude:: ../../problems/echoecho/submissions/wrong_answer/single-echo.py
   :lines: 3-

.. literalinclude:: ../../problems/echoecho/submissions/run_time_error/read_twice.py
   :lines: 3-
