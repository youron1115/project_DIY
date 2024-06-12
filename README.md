#pipeline流程
- 1-1.建立requirements.txt
<!-- - 1-2.建立.setup.py 此處還有問題 -->
-2.建立src dir
-2.1建立__init__.py
即使是空的 __init__.py 文件，也是這些機制正常工作的基礎。在 Python 3.3 以後的版本中，引入了 Implicit Namespace Packages，這允許包沒有 __init__.py 文件也能被識別。然而，為了向後兼容和明確地標記包的界限，許多項目仍然選擇包含空的 __init__.py 文件。此外，使用 __init__.py 提供的功能（如初始化代碼執行）仍然需要這個文件的存在。
-2.2建立logging.py