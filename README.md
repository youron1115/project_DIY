# pipeline流程
- 1-1.建立requirements.txt
<!-- - 1-2.建立.setup.py 此處還有問題 -->
- 2.建立src dir
- 2.1建立__init__.py:
即使是空的 __init__.py 文件，也是這些機制正常工作的基礎。在 Python 3.3 以後的版本中，引入了 Implicit Namespace Packages，這允許包沒有 __init__.py 文件也能被識別。然而，為了向後兼容和明確地標記包的界限，許多項目仍然選擇包含空的 __init__.py 文件。此外，使用 __init__.py 提供的功能（如初始化代碼執行）仍然需要這個文件的存在。另外若是在資料夾中加入__init__.py，則該資料夾會被視為一個package，及方便import
- 2.2建立logging.py
- 2.3建立exception.py
- 3.建立src.component dir存放資料前處理的程式
- 3.1建立__init__.py
- 3.2建立data_preprocess.py(split_data->set num_col and cat_col->preprocess)
- 3.3建立model_train.py(train_model class->choose_model(model list->model->record score->choose best model)->save model)
- 3.4建立model dir存放model
- 4.建立predict dir存放預測的程式